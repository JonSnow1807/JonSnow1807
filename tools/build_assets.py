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

def endmark(theme,t):
    b=line(0,24,998,24,t['line'])
    b+=path('M 1020 20 L 1034 12 L 1048 20 L 1034 28 Z',t['violet'],1.3)
    b+=path('M 1034 28 L 1048 20 L 1062 28 L 1048 36 Z',t['teal'],1.3)
    b+=line(1075,24,1120,24,t['line'])
    save(f'endmark-{theme}.svg',1120,48,'',b)

# ---------------------------------------------------------------------------
# Split project banners. Each project is one full-width row made of two images
# that sit flush against each other: the body (links to the source repository)
# and the action panel (links to the shipped or measured destination). Their
# intrinsic widths are in the same 77:22 ratio as the README's percentage
# widths, so the two halves always render at the same height.
# No phone-specific variants: GitHub's theme-pinning script collapses combined
# media queries, so every image ships one artwork per theme.
# ---------------------------------------------------------------------------
BW, PW, BH, R = 539, 154, 250, 14
DEST = {'mustard': ('Live', 'mustard.watch'), 'cuda': ('Results', 'A100 · kernel time'),
        'autotune': ('PyPI', 'pytorch-autotune'), 'spark': ('Web Store', 'Chrome extension')}
MOTIF_CENTER = {'sync': (647, 312), 'chip': (657, 295), 'search': (653, 307), 'conversation': (658, 293)}

def arrow_ne(x, y, c, s=1.0, w=1.6):
    return path(f'M {x} {y+8*s} L {x+8*s} {y} M {x+2*s} {y} H {x+8*s} V {y+6*s}', c, w)

def banners(theme, t):
    for c in CARDS:
        a = t[c['accent']]
        # Body: the rounded right corners fall outside the viewBox, so the right edge is a clean cut.
        b = rect(1, 1, BW + R + 10, BH - 2, t['panel'], t['line'], R)
        b += rect(28, 30, 24, 3, a, r=1.5)
        b += txt(60, 34, c['area'], 12, t['muted'], mono=True, spacing=1.6)
        b += txt(28, 78, c['name'], 34, t['text'], 700, spacing=-.8)
        b += txt(28, 104, c['desc'], 17, t['muted'])
        ms = round(c['m_size'] * .66)
        b += txt(27, 172, c['metric'], ms, a, 700, spacing=-1.2)
        sx = 28 + text_width(c['metric'], ms, 700) * .92 + 26
        for i, sc in enumerate(c['scope']):
            b += txt(sx, 146 + i * 21, sc, 15 if i == 0 else 14, t['text'] if i == 0 else t['muted'])
        b += line(28, 206, BW, 206, t['line'])
        b += txt(28, 233, c['stack'], 12, t['muted'], mono=True, spacing=.1)
        b += txt(BW - 46, 233, 'Source', 14, t['text'], 600, anchor='end')
        b += arrow_ne(BW - 40, 221, a, 1.1)
        save(f'{c["slug"]}-body-{theme}.svg', BW, BH,
             f'{c["name"]} — {c["desc"]}. {c["metric"]}; ' + '. '.join(c['scope']) + '. Open the source repository.', b)
        # Action panel: rounded left corners fall outside; a hairline seam marks the join.
        label, sub = DEST[c['slug']]
        b = rect(-R - 10, 1, PW + R + 9, BH - 2, t['panel2'], t['line'], R)
        b += line(.5, 1, .5, BH - 1, t['line'])
        b += txt(PW - 14, 34, c['n'], 13, a, mono=True, anchor='end')
        s = .40; cx, cy = MOTIF_CENTER[c['kind']]
        b += f'<g transform="translate({77 - cx*s:.1f} {98 - cy*s:.1f}) scale({s})">' + motif(c['kind'], t, a) + '</g>'
        b += circle(24, 195, 4, a)
        b += txt(36, 200, label, 16, t['text'], 700)
        b += arrow_ne(36 + text_width(label, 16, 700) + 9, 190, a, 1.15)
        b += txt(24, 221, sub, 11, t['muted'], mono=True)
        save(f'{c["slug"]}-action-{theme}.svg', PW, BH, f'{c["name"]} — open {label}: {sub}.', b)

# ---------------------------------------------------------------------------
# Explainer figures for the expandable sections: how each system works, and
# what was measured. Numbers come from the project repositories' committed
# results; each figure names its scope in a caption.
# ---------------------------------------------------------------------------
def node(x, y, w, h, t, title, sub=None, accent=None, size=15, sub_size=12):
    b = rect(x, y, w, h, t['panel2'], accent or t['line'], 9)
    b += txt(x + w/2, y + h/2 + (1 if sub else 5), title, size, t['text'], 700, anchor='middle')
    if sub: b += txt(x + w/2, y + h/2 + 19, sub, sub_size, t['muted'], mono=True, anchor='middle')
    return b

def arrow(x1, y1, x2, y2, c, w=1.5, head=6):
    ang = math.atan2(y2 - y1, x2 - x1)
    h1 = (x2 - head*math.cos(ang - .5), y2 - head*math.sin(ang - .5))
    h2 = (x2 - head*math.cos(ang + .5), y2 - head*math.sin(ang + .5))
    return path(f'M {x1} {y1} L {x2} {y2} M {h1[0]:.1f} {h1[1]:.1f} L {x2} {y2} L {h2[0]:.1f} {h2[1]:.1f}', c, w)

def zone(x, y, label, t): return txt(x, y, label, 11, t['quiet'], mono=True, spacing=1.8)

def hbar(x, y, w, c, h=14, opacity=1):
    r = min(4, w / 2)
    return f'<path d="M {x} {y} H {x+w-r:.1f} Q {x+w:.1f} {y} {x+w:.1f} {y+r} V {y+h-r} Q {x+w:.1f} {y+h} {x+w-r:.1f} {y+h} H {x} Z" fill="{c}" opacity="{opacity}"/>'

def rangebar(x1, x2, y, c, h=14):
    r = h / 2
    return f'<rect x="{x1:.1f}" y="{y}" width="{x2-x1:.1f}" height="{h}" rx="{r}" fill="{c}"/>'

def figure(name, w, h, t, title, body):
    b = rect(1, 1, w - 2, h - 2, t['panel'], t['line'], 16) + body
    save(name, w, h, title, b)

def fig_mustard(theme, t):
    a = t['gold']; W = 700
    b = zone(28, 34, 'HOW IT WORKS', t)
    for i, y in enumerate((62, 118, 174)):
        b += node(28, y, 124, 42, t, 'Chrome ' + 'ABC'[i], size=14)
        b += arrow(152, y + 21, 296, 138, t['muted'])
    b += node(298, 104, 150, 68, t, 'Sync server', 'Socket.IO', a)
    b += node(548, 104, 124, 68, t, 'Redis', 'atomic Lua')
    b += arrow(448, 138, 546, 138, t['muted'])
    b += txt(160, 50, 'clock offset θ over the socket ack (NTP-style)', 12, t['muted'])
    b += txt(160, 240, 'each client: drift = player time − expected time, corrected by', 12, t['muted'])
    b += txt(160, 256, 'predictive rate control; seeks only for gross error', 12, t['muted'])
    b += txt(548, 92, 'ordered epochs', 11, t['muted'], mono=True)
    b += txt(548, 192, 'idempotency keys', 11, t['muted'], mono=True)
    b += circle(304, 190, 3, a) + txt(313, 194, 'protocol model-checked with TLA+/TLC', 12, t['muted'])
    b += line(28, 278, W - 28, 278, t['line'])
    b += zone(28, 306, 'WHAT WAS MEASURED', t)
    b += txt(28, 330, 'Steady-state P95 drift by network scenario', 13, t['text'], 700)
    rows = [('clean loopback', 49), ('+150 ms each way (~300 ms RTT)', 48), ('50 ± 30 ms jitter', 79), ('25 ms + 5 % packet loss', 29), ('asymmetric 120 / 20 ms', 86)]
    x0, scale = 232, 1.55
    b += line(x0, 342, x0, 452, t['line'])
    for i, (lab, v) in enumerate(rows):
        y = 346 + i * 21; hi = (i == 1)
        b += txt(x0 - 8, y + 11, lab, 12, t['text'] if hi else t['muted'], 600 if hi else 400, anchor='end')
        b += hbar(x0, y, v * scale, a if hi else t['line'], 14, 1 if hi else .9)
        b += txt(x0 + v * scale + 6, y + 11, f'{v} ms', 12, t['text'], 600 if hi else 400)
    b += txt(28, 474, '3 Chrome clients · 240 s · player-reported drift · predictive servo (shipped default) · docs/SYNC_DESIGN.md §8', 11, t['quiet'])
    b += txt(452, 330, 'Relay memory per connection', 13, t['text'], 700)
    for i, (lab, v, hi) in enumerate((('Rust', 14.5, True), ('Go', 40, False))):
        y = 350 + i * 26
        b += txt(492, y + 11, lab, 12, t['text'] if hi else t['muted'], 600 if hi else 400, anchor='end')
        b += hbar(500, y, v * 3.4, a if hi else t['line'], 14, 1 if hi else .9)
        b += txt(500 + v * 3.4 + 6, y + 11, f'{v:g} KB', 12, t['text'], 600 if hi else 400)
    b += txt(452, 420, 'local 10,000-connection test', 11, t['quiet'])
    b += txt(452, 436, 'study relays, not the production backend;', 11, t['quiet'])
    b += txt(452, 452, 'extreme-tail latency comparison inconclusive', 11, t['quiet'])
    figure(f'fig-mustard-{theme}.svg', W, 496, t, 'Mustard: clients estimate a clock offset over the socket ack and correct drift with predictive rate control; room state lives in Redis behind atomic Lua scripts. Chart: steady-state P95 drift 49, 48, 79, 29 and 86 ms across five network scenarios; relay memory 14.5 KB (Rust) versus 40 KB (Go) per connection.', b)

def fig_cuda(theme, t):
    a = t['teal']; W = 700
    b = zone(28, 34, 'HOW IT WORKS', t)
    b += txt(28, 62, 'EAGER COMPOSITE', 11, t['muted'], mono=True, spacing=1.4)
    b += node(28, 72, 150, 42, t, 'x + residual', size=14)
    b += node(262, 72, 176, 42, t, 'LayerNorm / RMSNorm', size=14)
    b += node(522, 72, 150, 42, t, 'cast → FP8', size=14)
    for x1, x2 in ((178, 262), (438, 522)):
        b += arrow(x1, 93, x2, 93, t['muted'])
        b += txt((x1 + x2) / 2, 87, 'HBM', 10, t['quiet'], mono=True, anchor='middle')
    b += txt(28, 136, 'three launches; the hidden state round-trips through HBM between them', 12, t['muted'])
    b += txt(28, 174, 'FUSED', 11, t['muted'], mono=True, spacing=1.4)
    b += node(28, 184, 410, 56, t, 'residual-add + norm + FP8 quantize', 'one kernel · one read of x and residual', a, 15)
    b += arrow(438, 204, 522, 204, t['muted']) + arrow(438, 220, 522, 236, t['muted'])
    b += node(522, 190, 150, 28, t, 'fp8 out + scale', size=13)
    b += node(522, 224, 150, 28, t, 'new residual', size=13)
    b += circle(34, 270, 3, a) + txt(43, 274, 'backward: fixed-chunk partials → fixed-order finalize, no atomics', 12, t['muted'])
    b += circle(34, 292, 3, a) + txt(43, 296, 'torch.compile traces each op as one custom-op node: zero graph breaks', 12, t['muted'])
    b += line(28, 318, W - 28, 318, t['line'])
    b += zone(28, 346, 'WHAT WAS MEASURED', t)
    b += txt(28, 370, 'Dynamic RMSNorm → FP8: kernel-time speedup, min–max across six shapes', 13, t['text'], 700)
    x0, sc = 236, 52
    b += line(x0, 384, x0, 456, t['line'])
    one = x0 + 1 * sc
    b += line(one, 384, one, 456, t['quiet'], 1) + txt(one, 470, '1× parity', 10, t['quiet'], mono=True, anchor='middle')
    for i, (lab, lo, hi, em) in enumerate((('vs eager PyTorch composite', 4.9, 7.2, False), ('vs torch.compile’d composite', 1.04, 1.76, True))):
        y = 392 + i * 30
        b += txt(x0 - 8, y + 11, lab, 12, t['text'] if em else t['muted'], 600 if em else 400, anchor='end')
        b += rangebar(x0 + lo * sc, x0 + hi * sc, y, a if em else t['line'])
        b += txt(x0 + lo * sc - 6, y + 11, f'{lo:g}×', 12, t['text'], 600 if em else 400, anchor='end')
        b += txt(x0 + hi * sc + 6, y + 11, f'{hi:g}×', 12, t['text'], 600 if em else 400)
    b += txt(28, 488, 'NVIDIA A100 · FP16 · six shapes, 512×1024 … 4096×8192 · kernel time, not end-to-end model speed', 11, t['quiet'])
    b += txt(28, 504, 'H100 results and the configurations where PyTorch wins are documented in the repository', 11, t['quiet'])
    figure(f'fig-cuda-{theme}.svg', W, 524, t, 'Fused CUDA operators: the eager composite runs residual-add, normalization and an FP8 cast as three kernels with HBM round-trips; the fused version does all three in one kernel. Chart: dynamic RMSNorm to FP8 kernel time is 4.9 to 7.2 times faster than the eager composite and 1.04 to 1.76 times faster than the compiled composite across six shapes on an A100 in FP16.', b)

def fig_autotune(theme, t):
    a = t['violet']; W = 700
    b = zone(28, 34, 'HOW IT WORKS', t)
    b += node(28, 62, 130, 56, t, 'Your model', 'and batch', size=14)
    b += node(196, 62, 150, 56, t, 'Baseline first', 'fp32 eager', size=14)
    b += node(384, 62, 150, 56, t, 'Candidate grid', 'precision × compile', size=14)
    b += node(572, 62, 100, 56, t, 'Measure', 'real steps', size=14)
    for x1, x2 in ((158, 196), (346, 384), (534, 572)): b += arrow(x1, 90, x2, 90, t['muted'])
    b += txt(459, 136, '× memory format × fused optimizer', 11, t['muted'], mono=True, anchor='middle')
    b += path('M 622 118 V 150 H 126 V 166', t['muted'], 1.5) + arrow(126, 160, 126, 168, t['muted'])
    b += node(28, 170, 196, 56, t, 'Keep the winner', '> 3 % over the incumbent', a, 14, 10.5)
    b += node(254, 170, 200, 56, t, 'Report', 'trials · compile · break-even', size=14, sub_size=10.5)
    b += node(484, 170, 188, 56, t, 'Cache', 'model · shapes · GPU · torch', size=14, sub_size=10.5)
    b += arrow(224, 198, 254, 198, t['muted']) + arrow(454, 198, 484, 198, t['muted'])
    b += circle(34, 254, 3, a) + txt(43, 258, 'the search is budgeted; a candidate slower than the baseline is never returned', 12, t['muted'])
    b += line(28, 280, W - 28, 280, t['line'])
    b += zone(28, 308, 'WHAT WAS MEASURED', t)
    b += txt(28, 332, 'Training-step speedup after tuning', 13, t['text'], 700)
    x0, sc = 168, 62
    b += line(x0, 346, x0, 452, t['line'])
    one = x0 + sc
    b += line(one, 346, one, 452, t['quiet'], 1)
    rows = (('ResNet-50', 2.71, None), ('ResNet-18', 3.84, None), ('Transformer 6L', 6.65, 2.55))
    y = 350
    for lab, v, alt in rows:
        b += txt(x0 - 8, y + 11, lab, 12, t['text'], anchor='end')
        b += hbar(x0, y, v * sc, a, 14)
        b += txt(x0 + v * sc + 6, y + 11, f'{v:g}×', 12, t['text'], 600)
        y += 21
        if alt is not None:
            b += hbar(x0, y, alt * sc, t['line'], 14, .9)
            b += txt(x0 + alt * sc + 6, y + 11, f'{alt:g}× vs eager with TF32 matmuls enabled', 12, t['muted'])
            y += 21
        y += 6
    b += rect(28, 462, 12, 12, a, r=3) + txt(46, 472, 'vs PyTorch-default fp32 eager baseline', 12, t['muted'])
    b += rect(300, 462, 12, 12, t['line'], r=3, opacity=.9) + txt(318, 472, 'vs an informed eager baseline (TF32 matmuls on)', 12, t['muted'])
    b += txt(28, 494, 'NVIDIA A100-SXM4-40GB · full training step: forward + loss + backward + optimizer', 11, t['quiet'])
    b += txt(28, 510, 'winning configs use torch.compile together with precision, memory-format and fused-optimizer choices', 11, t['quiet'])
    figure(f'fig-autotune-{theme}.svg', W, 530, t, 'PyTorch AutoTune: the baseline is measured first, candidates across precision, compile mode, memory format and fused optimizer run real training steps under a budget, the winner must beat the incumbent by more than 3 percent, and the report and cache record every trial. Chart: 2.71 times on ResNet-50, 3.84 times on ResNet-18 and 6.65 times on a six-layer Transformer versus the PyTorch-default fp32 eager baseline; the Transformer gain is 2.55 times against an eager baseline with TF32 matmuls enabled.', b)

def fig_spark(theme, t):
    a = t['coral']; W = 700
    b = zone(28, 34, 'HOW IT WORKS', t)
    steps = (('Chrome extension', 'captures a chat'), ('FastAPI backend', 'stores + serves'), ('ChromaDB', 'embeddings'), ('React dashboard', 'browse · search'))
    for i, (ti, su) in enumerate(steps):
        x = 28 + i * 168
        b += node(x, 64, 128, 58, t, ti, su, a if i == 3 else None, 14)
        if i: b += arrow(x - 40, 93, x, 93, t['muted'])
    b += circle(34, 160, 3, a) + txt(43, 164, 'semantic search runs over stored embeddings; the dashboard is React + TypeScript', 12, t['muted'])
    b += circle(34, 182, 3, a) + txt(43, 186, 'published on the Chrome Web Store', 12, t['muted'])
    figure(f'fig-spark-{theme}.svg', W, 212, t, 'ChatGPT Spark: a Chrome extension captures a conversation, a FastAPI backend stores it, ChromaDB holds the embeddings, and a React dashboard browses and semantically searches them. Published on the Chrome Web Store.', b)

def figures(theme, t):
    fig_mustard(theme, t); fig_cuda(theme, t); fig_autotune(theme, t); fig_spark(theme, t)

for old in OUT.glob('*.svg'): old.unlink()
for theme, t in THEMES.items():
    hero(theme, t); buttons(theme, t); banners(theme, t); figures(theme, t); endmark(theme, t)
for stale in OUT.glob('*-mobile-*.svg'): stale.unlink()
print(f'Built {len(list(OUT.glob("*.svg")))} SVG assets in {OUT}')
