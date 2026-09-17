"""Build the self-contained vector artwork used by this profile.
Python 3 standard library only. Run from anywhere: python tools/build_assets.py
No font files, network services, tracking, or JavaScript are embedded in assets.
"""
from pathlib import Path
from html import escape
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'profile'
OUT.mkdir(parents=True, exist_ok=True)
FONT = "Arial, Helvetica, sans-serif"
MONO = "'Courier New', monospace"
THEMES = {
    'dark': dict(bg='#0D1117', panel='#121923', panel2='#18222F', line='#2C3A4C', text='#F0F3F8', muted='#A8B5C8', quiet='#8394AC', violet='#BBA8FF', teal='#83DCD0', gold='#EDC17D', coral='#F3A6B0', glow='#9D7BEF'),
    'light': dict(bg='#FFFFFF', panel='#F6F8FC', panel2='#EDF1F7', line='#CCD5E2', text='#192438', muted='#52617A', quiet='#5D6F88', violet='#6540B4', teal='#116B64', gold='#865900', coral='#A83F5A', glow='#A391ED'),
}

def txt(x, y, s, size=28, color=None, weight=400, mono=False, spacing=None, anchor=None):
    attrs = f'x="{x}" y="{y}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" fill="{color or "#F0F3F8"}"'
    if spacing is not None: attrs += f' letter-spacing="{spacing}"'
    if anchor: attrs += f' text-anchor="{anchor}"'
    return f'<text {attrs}>{escape(s)}</text>'

def line(x1,y1,x2,y2,c,w=1,opacity=1):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{w}" opacity="{opacity}"/>'

def rect(x,y,w,h,c,stroke=None,r=0,opacity=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"'+(f' stroke="{stroke}"' if stroke else '')+f' opacity="{opacity}"/>'

def circle(x,y,r,c,stroke=None,w=1,opacity=1):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{w}"' if stroke else '')+f' opacity="{opacity}"/>'

def path(d,c,w=1,fill='none',opacity=1):
    return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>'

def svg(w,h,title,body,defs=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs>{defs}</defs>
{body}
</svg>\n'''

def save(name,w,h,title,body,defs=''):
    (OUT/name).write_text(svg(w,h,title,body,defs), encoding='utf-8')

def iso_tile(x,y,size,c,t,fill=True):
    hh=size*.52
    d=f'M{x} {y-hh} L{x+size} {y} L{x} {y+hh} L{x-size} {y} Z'
    return path(d,c,1.4,t['panel2'] if fill else 'none',.95)

def hero(theme,t):
    w,h=1120,408
    defs=f'''<radialGradient id="halo"><stop stop-color="{t['glow']}" stop-opacity=".18"/><stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/></radialGradient>
    <linearGradient id="edge"><stop stop-color="{t['violet']}"/><stop offset="1" stop-color="{t['teal']}"/></linearGradient>
    <clipPath id="clip"><rect x="1" y="1" width="1118" height="406" rx="22"/></clipPath>
    <style>@keyframes travel{{0%{{stroke-dashoffset:120;opacity:0}}12%,70%{{opacity:.8}}100%{{stroke-dashoffset:-200;opacity:0}}}} .signal{{animation:travel 9s linear infinite;stroke-dasharray:20 300}} @media(prefers-reduced-motion:reduce){{.signal{{animation:none;opacity:0}}}}</style>'''
    b=rect(1,1,1118,406,t['panel'],t['line'],22)
    b+='<g clip-path="url(#clip)">'
    b+='<ellipse cx="907" cy="210" rx="270" ry="235" fill="url(#halo)"/>'
    # Registration marks / small deliberate typographic detail.
    b+=path('M 38 56 V 38 H 56',t['violet'],2)
    b+=txt(72,52,'SOFTWARE ENGINEER',18,t['muted'],mono=True,spacing=2)
    b+=txt(1058,52,'CS /',18,t['quiet'],mono=True,anchor='end')
    b+=txt(51,150,'Chinmay',92,t['text'],700,spacing=-4.2)
    b+=txt(49,242,'Shrivastava',92,t['text'],700,spacing=-4.2)
    b+=rect(56,275,72,4,t['violet'],r=2)
    b+=rect(137,275,30,4,t['teal'],r=2)
    # Isometric array. Decorative computation / coordination motif, not a plot.
    ox,oy=881,176
    for layer in [2,1,0]:
        z=layer*29
        for row in range(3):
            for col in range(3):
                x=ox+(col-row)*36
                y=oy+(col+row)*19+z
                cc=t['line'] if layer else (t['teal'] if (row+col)%3==0 else t['violet'])
                b+=iso_tile(x,y,32,cc,t)
    for x,y in [(773,233),(989,233),(881,176),(881,309)]:
        b+=circle(x,y,4,t['teal'])
    b+=path('M 773 233 H 726 Q 710 233 710 217 V 141 Q 710 125 694 125 H 679',t['line'],1.5)
    b+=path('M 989 233 H 1033 Q 1049 233 1049 217 V 144',t['line'],1.5)
    b+=path('M 881 309 V 326 H 1018',t['line'],1.5)
    b+='<path class="signal" d="M 679 125 H 694 Q 710 125 710 141 V 217 Q 710 233 726 233 H 773" fill="none" stroke="url(#edge)" stroke-width="2.5"/>'
    b+=circle(1049,139,5,'none',t['violet'],1.5)
    b+=line(56,321,1064,321,t['line'])
    b+=txt(56,366,'BACKEND',19,t['text'],mono=True,spacing=1.3)
    b+=txt(215,366,'/ DISTRIBUTED SYSTEMS',19,t['muted'],mono=True,spacing=.3)
    b+=txt(539,366,'/ ML INFRASTRUCTURE',19,t['muted'],mono=True,spacing=.3)
    b+=path('M 1036 352 H 1062 V 378 M 1062 352 L 1036 378',t['teal'],2)
    b+='</g>'
    save(f'hero-{theme}.svg',w,h,'Chinmay Shrivastava — Software Engineer. Backend, distributed systems and ML infrastructure.',b,defs)
    # Phone-specific variant keeps the identity large, not a scaled-down desktop banner.
    b=rect(1,1,599,349,t['panel'],t['line'],20)
    b+=txt(32,46,'SOFTWARE ENGINEER',20,t['muted'],mono=True,spacing=1.8)
    b+=txt(29,132,'Chinmay',77,t['text'],700,spacing=-3)
    b+=txt(27,211,'Shrivastava',77,t['text'],700,spacing=-3.5)
    b+=rect(32,244,68,4,t['violet'],r=2)+rect(110,244,28,4,t['teal'],r=2)
    b+=line(32,274,568,274,t['line'])
    b+=txt(32,316,'BACKEND / SYSTEMS / ML INFRA',22,t['muted'],mono=True)
    b+=path('M 536 35 H 565 V 64 M 565 35 L 539 61',t['teal'],2)
    save(f'hero-mobile-{theme}.svg',600,350,'Chinmay Shrivastava — Software Engineer.',b)

CARDS=[
 dict(slug='mustard',n='01',area='DISTRIBUTED SYSTEMS',name='Mustard Watch Party',desc='Multi-instance video synchronization',metric='48 ms',m_size=70,scope=['P95 player-reported drift','3 Chrome clients / ~300 ms RTT','Steady state / 240-second test'],stack='TYPESCRIPT  /  REDIS  /  TLA+',accent='gold',kind='sync',short='Mustard',links=[('live','Live'),('source','Source')]),
 dict(slug='cuda',n='02',area='GPU PERFORMANCE',name='Fused CUDA Operators',desc='LayerNorm / RMSNorm for PyTorch',metric='1.04–1.76×',m_size=63,scope=['vs. compiled PyTorch','RMSNorm-to-FP8 / A100 / FP16','Kernel-time comparison'],stack='C++  /  CUDA  /  PYTORCH',accent='teal',kind='chip',short='CUDA ops',links=[('benchmarks','Benchmarks'),('source','Source')]),
 dict(slug='autotune',n='03',area='ML TOOLING',name='PyTorch AutoTune',desc='Workload-specific training optimization',metric='2.7–6.7×',m_size=67,scope=['training-step speedup after tuning','vs. PyTorch-default FP32 eager','3 workloads / NVIDIA A100'],stack='PYTHON  /  PYTORCH  /  CUDA',accent='violet',kind='search',short='AutoTune',links=[('pypi','PyPI'),('source','Source')]),
 dict(slug='spark',n='04',area='DEVELOPER TOOLS',name='ChatGPT Spark',desc='Conversation capture and semantic search',metric='Published',m_size=64,scope=['Chrome Web Store','React dashboard / FastAPI backend','ChromaDB vector search'],stack='TYPESCRIPT  /  FASTAPI  /  CHROMADB',accent='coral',kind='conversation',short='Spark',links=[('webstore','Web Store'),('source','Source')]),
]

def motif(kind,t,accent):
    # Artwork confined to the right side. These are decorative glyphs, not benchmark charts.
    b=''
    if kind=='sync':
        for i,y in enumerate([206,286,366]):
            b+=rect(592,y,148,52,t['panel2'],t['line'],8)
            b+=circle(610,y+16,3,accent)
            b+=line(624,y+16,722,y+16,t['line'],2)
            b+=line(610,y+34,704-(i%2)*18,y+34,t['quiet'],2,.5)
        b+=path('M 568 218 H 554 V 392 H 568 M 554 310 H 577',accent,2)
        b+=line(666,258,666,286,accent,2)+line(666,338,666,366,accent,2)
        b+=circle(666,272,4,t['panel'],accent,1.5)+circle(666,352,4,t['panel'],accent,1.5)
    elif kind=='chip':
        b+=rect(582,220,150,150,t['panel2'],accent,12)
        b+=rect(613,251,88,88,t['panel'],t['line'],5)
        for i in range(5):
            y=236+i*29
            b+=line(568,y,582,y,accent,2)+line(732,y,746,y,accent,2)
            x=599+i*29
            b+=line(x,206,x,220,accent,2)+line(x,370,x,384,accent,2)
        for i in range(3):
            for j in range(3):
                b+=rect(626+i*22,264+j*22,15,15,accent if i==j else t['line'],r=3,opacity=.85 if i==j else .6)
    elif kind=='search':
        for i,y in enumerate([219,286,353]):
            b+=rect(565,y,180,42,t['panel2'],t['line'],7)
            for j in range(3):
                b+=rect(580+j*38,y+13,25,16,accent if (i,j) in [(0,1),(1,2),(2,0)] else t['line'],r=4,opacity=.85)
        b+=path('M 550 240 H 537 V 373 H 550',t['line'],2)
        b+=path('M 755 240 H 770 V 307 H 755 M 770 307 V 373 H 755',accent,2)
        b+=circle(770,307,5,accent)
    else:
        b+=rect(578,207,160,59,t['panel2'],t['line'],11)
        b+=path('M 593 264 V 276 L 607 264',t['line'],1.6,t['panel2'])
        b+=line(598,228,715,228,t['quiet'],2,.8)+line(598,246,682,246,t['quiet'],2,.5)
        b+=rect(552,301,160,59,t['panel2'],accent,11)
        b+=circle(731,345,34,t['panel'],accent,2)
        b+=circle(727,341,12,'none',accent,2)+line(736,350,746,360,accent,3)
        b+=line(573,322,684,322,t['quiet'],2,.8)+line(573,342,654,342,t['quiet'],2,.5)
    return b

def cards(theme,t):
    w,h=840,540
    for c in CARDS:
        a=t[c['accent']]
        defs=f'<radialGradient id="tint"><stop stop-color="{a}" stop-opacity=".08"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>'
        b=rect(1,1,w-2,h-2,t['panel'],t['line'],20)
        b+='<ellipse cx="683" cy="296" rx="190" ry="195" fill="url(#tint)"/>'
        b+=rect(40,39,37,4,a,r=2)
        b+=txt(92,49,c['area'],20,t['muted'],mono=True,spacing=2)
        b+=txt(793,51,c['n'],22,a,mono=True,anchor='end')
        b+=txt(39,112,c['name'],44,t['text'],700,spacing=-1.2)
        b+=txt(40,154,c['desc'],27,t['muted'])
        b+=txt(38,252,c['metric'],c['m_size'],a,700,spacing=-2)
        for i,s in enumerate(c['scope']):
            b+=txt(40,297+i*37,s,27 if i==0 else 25,t['text'] if i==0 else t['muted'])
        b+=motif(c['kind'],t,a)
        b+=line(40,446,800,446,t['line'])
        b+=txt(40,491,c['stack'],21,t['muted'],mono=True,spacing=.15)
        b+=path('M 759 473 H 785 V 499 M 785 473 L 760 498',a,2.8)
        save(f'{c["slug"]}-{theme}.svg',w,h,c['name']+' — '+c['desc']+'. '+c['metric']+'; '+'. '.join(c['scope'])+'.',b,defs)


def mobile_cards(theme,t):
    for c in CARDS:
        a=t[c['accent']]
        b=rect(1,1,598,438,t['panel'],t['line'],18)
        b+=rect(28,29,28,3,a,r=1.5)
        b+=txt(67,37,c['area'],17,t['muted'],mono=True,spacing=1.5)
        b+=txt(567,38,c['n'],18,a,mono=True,anchor='end')
        b+=txt(27,94,c['name'],38,t['text'],700,spacing=-1)
        b+=txt(28,129,c['desc'],22,t['muted'])
        b+=txt(26,217,c['metric'],62,a,700,spacing=-1.8)
        for i,scope in enumerate(c['scope']):
            b+=txt(28,261+i*34,scope,25 if i==0 else 23,t['text'] if i==0 else t['muted'])
        b+=path('M 554 175 H 568 V 340 H 554',t['line'],1.5)
        b+=circle(568,256,4,a)
        b+=line(28,375,572,375,t['line'])
        b+=txt(28,409,c['stack'],16,t['muted'],mono=True)
        b+=path('M 543 393 H 563 V 413 M 563 393 L 543 413',a,2)
        save(f"{c['slug']}-mobile-{theme}.svg",600,440,c['name']+' — '+c['desc']+'. '+c['metric']+'; '+'. '.join(c['scope'])+'.',b)

def buttons(theme,t):
    for slug,label,w in [('linkedin','LinkedIn',128),('email','Email',112),('huggingface','Hugging Face',159)]:
        b=rect(1,1,w-2,38,t['panel'],t['line'],8)
        if slug=='email':
            b+=rect(13,13,16,12,'none',t['muted'],2)+path('M 14 14 L 21 20 L 28 14',t['muted'],1.1)
        elif slug=='linkedin':
            # Generic professional ID glyph rather than a vendor-dependent logo.
            b+=rect(13,12,15,15,'none',t['muted'],2)+circle(17,16,1.1,t['muted'])+line(17,20,17,24,t['muted'],1.4)+path('M 22 24 V 20 Q 26 18 26 22 V 24',t['muted'],1.4)
        else:
            b+=circle(21,20,7,'none',t['muted'],1.2)+path('M 21 13 C 16 18 16 22 21 27 M 21 13 C 26 18 26 22 21 27 M 14 20 H 28',t['muted'],1)
        b+=txt(38,25,label,14,t['text'],600)
        b+=path(f'M {w-23} 15 H {w-17} V 21 M {w-17} 15 L {w-24} 22',t['violet'],1.4)
        save(f'{slug}-{theme}.svg',w,40,label,b)

def text_width(s,size,weight=400):
    """Rough Arial advance width, used only to size button boxes; real clipping is checked in a browser."""
    w=0
    for ch in s:
        if ch==' ' or ch=='\u00b7': w+=.28
        elif ch.isupper(): w+=.68
        elif ch.isdigit(): w+=.56
        elif ch in 'ilj.,:;\'|': w+=.26
        elif ch in 'mw': w+=.82
        else: w+=.54
    return w*size*(1.04 if weight>=600 else 1)

def card_links(theme,t):
    """Two link buttons per project card: the shipped/measured destination and the source repository."""
    for c in CARDS:
        a=t[c['accent']]
        for kind,label in c['links']:
            x=27
            name_w=text_width(c['short'],14,600); label_w=text_width(label,14,600)
            w=int(round(x+name_w+16+label_w+34))
            b=rect(1,1,w-2,38,t['panel'],t['line'],8)
            b+=circle(16,20,3.6,a)
            b+=txt(x,25,c['short'],14,t['muted'],600)
            b+=txt(x+name_w+5,25,'\u00b7',14,t['quiet'],600)
            b+=txt(x+name_w+16,25,label,14,t['text'],600)
            b+=path(f'M {w-23} 15 H {w-17} V 21 M {w-17} 15 L {w-24} 22',a,1.4)
            dest='source repository on GitHub' if kind=='source' else label
            save(f'link-{c["slug"]}-{kind}-{theme}.svg',w,40,f'{c["name"]} — {dest}',b)

def endmark(theme,t):
    b=line(0,24,998,24,t['line'])
    b+=path('M 1020 20 L 1034 12 L 1048 20 L 1034 28 Z',t['violet'],1.3)
    b+=path('M 1034 28 L 1048 20 L 1062 28 L 1048 36 Z',t['teal'],1.3)
    b+=line(1075,24,1120,24,t['line'])
    save(f'endmark-{theme}.svg',1120,48,'',b)

for theme,t in THEMES.items():
    hero(theme,t); cards(theme,t); mobile_cards(theme,t); buttons(theme,t); card_links(theme,t); endmark(theme,t)
print(f'Built {len(list(OUT.glob("*.svg")))} SVG assets in {OUT}')
