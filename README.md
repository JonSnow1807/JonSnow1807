<!-- HERO -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:6D28D9,45:8B5CF6,100:EC4899&amp;height=220&amp;section=header&amp;text=Chinmay%20Shrivastava&amp;fontSize=44&amp;fontColor=FFFFFF&amp;fontAlignY=36&amp;desc=Software%20Engineer&amp;descSize=20&amp;descAlignY=55&amp;animation=fadeIn" width="100%" alt="Chinmay Shrivastava — Software Engineer" />
</p>

<p align="center">
  <strong>Backend &amp; Distributed Systems &nbsp;·&nbsp; ML Infrastructure &nbsp;·&nbsp; GPU Performance</strong>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&amp;size=18&amp;duration=3200&amp;pause=1300&amp;color=A78BFA&amp;center=true&amp;vCenter=true&amp;width=680&amp;height=40&amp;lines=Building+systems.+Measuring+what+matters.;PyTorch+contributions+to+production+infrastructure.;Correctness+first.+Performance+with+evidence." width="680" alt="Building systems. Measuring what matters." />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/cshrivastava/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" height="28" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="mailto:cshrivastava2000@gmail.com">
    <img src="https://img.shields.io/badge/Email-8B5CF6?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" height="28" alt="Email" />
  </a>
  &nbsp;
  <a href="https://huggingface.co/chinmays18">
    <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&amp;logo=huggingface&amp;logoColor=black" height="28" alt="Hugging Face" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-2_upstream_changes-8B5CF6?style=flat-square&amp;labelColor=1F2937" alt="PyTorch: 2 upstream changes" />
  <img src="https://img.shields.io/badge/bpfilter-2_merged_PRs-EC4899?style=flat-square&amp;labelColor=1F2937" alt="bpfilter: 2 merged PRs" />
  <img src="https://img.shields.io/badge/OpenShift-13_node_deployment-10B981?style=flat-square&amp;labelColor=1F2937" alt="OpenShift: 13-node deployment" />
</p>

<br>

<!-- ABOUT -->
<h2 align="center">👋 About Me</h2>

<p align="center">
  <strong>I build high-performance backend and ML infrastructure,<br>and I validate it against references instead of trusting it.</strong>
</p>

<p>
  At <strong>Reliance Jio</strong>, I work on production 4G/5G analytics, deterministic query compilation and GPU-backed inference services on Kubernetes/OpenShift. Outside work, I contribute to <strong>PyTorch</strong> and <strong>Meta's bpfilter</strong>, and build tools for GPU performance and distributed coordination.
</p>

<br>

<!-- UPSTREAM CONTRIBUTIONS -->
<h2 align="center">🔀 Upstream Contributions</h2>

<table align="center" width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🔥 PyTorch Core</h3>
      <p align="center"><code>torch.compile</code> <code>torch.func</code></p>
      <p>Enabled existing dynamic-shape support for foreach operations by default, with a corresponding test update.</p>
      <p>Exposed <code>rearrange</code> through the <code>torch.func</code> public API, with tests and documentation.</p>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">🌐 Meta's bpfilter</h3>
      <p align="center"><code>C</code> <code>BPF</code> <code>IPv4 / IPv6</code></p>
      <p>Added IPv4 Type of Service and IPv6 Traffic Class matchers for packet filtering.</p>
      <p>Implemented command-line parsing, BPF code generation and unit tests, including endianness-safe byte loads for IPv6.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/pytorch/pytorch/pull/158985"><img src="https://img.shields.io/badge/PR-%23158985-8B5CF6?style=flat-square&amp;logo=github&amp;logoColor=white" alt="PyTorch PR 158985" /></a>
      <a href="https://github.com/pytorch/pytorch/pull/173183"><img src="https://img.shields.io/badge/PR-%23173183-8B5CF6?style=flat-square&amp;logo=github&amp;logoColor=white" alt="PyTorch PR 173183" /></a>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/facebook/bpfilter/pull/364"><img src="https://img.shields.io/badge/PR-%23364-EC4899?style=flat-square&amp;logo=github&amp;logoColor=white" alt="bpfilter PR 364" /></a>
      <a href="https://github.com/facebook/bpfilter/pull/369"><img src="https://img.shields.io/badge/PR-%23369-EC4899?style=flat-square&amp;logo=github&amp;logoColor=white" alt="bpfilter PR 369" /></a>
    </td>
  </tr>
</table>

<p align="center">
  <sub>All four changes were accepted upstream. PyTorch landing commits: <a href="https://github.com/pytorch/pytorch/commit/51eb41a57ef4365bece0c187f1d751221b88c135">foreach</a> · <a href="https://github.com/pytorch/pytorch/commit/cd59c879a7eb47de27e0eead455b0b0349c12488">rearrange</a>.</sub>
</p>

<br>

<!-- PROJECTS: ACTION BUTTONS HAVE THEIR OWN ROW TO KEEP THEM ALIGNED -->
<h2 align="center">🚀 Selected Projects</h2>

<table align="center" width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🎬 Mustard Watch Party</h3>
      <p align="center"><strong>Distributed Video Synchronization</strong></p>
      <p align="center"><code>TypeScript</code> <code>Redis</code> <code>TLA+</code></p>
      <p>Built a multi-instance platform with NTP-style clock estimation, predictive drift correction and atomic Redis Lua updates.</p>
      <p><strong>48 ms P95 steady-state, player-reported drift</strong> across three Chrome clients at approximately 300 ms RTT in a 240-second test scenario.</p>
      <details>
        <summary><strong>Engineering details</strong></summary>
        <ul>
          <li>TLA+/TLC exposed a stale-epoch bug after store resets, leading to an ordered-epoch fix.</li>
          <li>Idempotency keys and atomic updates prevent duplicate control commands from being applied again within the deduplication window.</li>
          <li>Separate Go and Rust relays test protocol conformance and runtime costs; they are study implementations, not the production backend.</li>
        </ul>
      </details>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">⚡ Fused CUDA Operators</h3>
      <p align="center"><strong>LayerNorm / RMSNorm for PyTorch</strong></p>
      <p align="center"><code>C++</code> <code>CUDA</code> <code>PyTorch</code></p>
      <p>Built normalization kernels with fused residual-add, FP8 outputs and deterministic backward reductions, integrated with <code>torch.compile</code>.</p>
      <p><strong>1.04–1.76× kernel-time speedup</strong> over the compiled PyTorch composite for dynamic RMSNorm-to-FP8 across tested FP16 shapes on an A100.</p>
      <details>
        <summary><strong>Engineering details</strong></summary>
        <ul>
          <li>Drop-in PyTorch modules work under <code>torch.compile</code> without graph breaks.</li>
          <li>Deterministic gradients use fixed-order reductions rather than atomic accumulation.</li>
          <li>Published A100/H100 results, including cases where PyTorch wins. These are operator-level measurements, not end-to-end model speedups.</li>
        </ul>
      </details>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/JonSnow1807/Mustard-Watch-Party"><img src="https://img.shields.io/badge/View_Code-8B5CF6?style=for-the-badge&amp;logo=github&amp;logoColor=white" height="28" alt="View Mustard source code" /></a>
      <br><sub><a href="https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/SYNC_DESIGN.md">Sync design</a> · <a href="https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/FORMAL.md">Model-checking findings</a></sub>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator"><img src="https://img.shields.io/badge/View_Code-EC4899?style=for-the-badge&amp;logo=github&amp;logoColor=white" height="28" alt="View CUDA operator source code" /></a>
      <br><sub><a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/tree/main/benchmarks/results/2026-08-25_a100-40gb_v050_ops">A100 benchmarks</a> · <a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/blob/main/docs/methodology.md">Methodology</a></sub>
    </td>
  </tr>
</table>

<table align="center" width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3 align="center">🔬 PyTorch AutoTune</h3>
      <p align="center"><strong>Measurement-Driven Training Optimization</strong></p>
      <p align="center"><code>Python</code> <code>PyTorch</code> <code>CUDA</code></p>
      <p>Built an autotuner that benchmarks precision, compile mode, memory format and fused-optimizer configurations on the target model and batch.</p>
      <p><strong>2.7–6.7× training-step speedups after tuning</strong> versus the PyTorch-default FP32 eager baseline across three workloads on an A100.</p>
      <details>
        <summary><strong>Engineering details</strong></summary>
        <ul>
          <li>Benchmarked ResNet-50, ResNet-18 and a six-layer Transformer.</li>
          <li>Added budgeted search, configuration caching and reports showing compilation cost and estimated break-even time.</li>
          <li>The tuner uses <code>torch.compile</code> alongside other optimizations. Numerical trade-offs and alternative baselines are documented.</li>
        </ul>
      </details>
    </td>
    <td width="50%" valign="top">
      <h3 align="center">💬 ChatGPT Spark</h3>
      <p align="center"><strong>Conversation Capture &amp; Semantic Search</strong></p>
      <p align="center"><code>TypeScript</code> <code>FastAPI</code> <code>ChromaDB</code></p>
      <p>Built a Chrome extension for capturing and searching conversation history, with a React/TypeScript dashboard and a FastAPI backend.</p>
      <p><strong>Published on the Chrome Web Store.</strong> Combines conversation summaries and vector search to make saved conversations easier to find.</p>
      <details>
        <summary><strong>Engineering details</strong></summary>
        <ul>
          <li>Chrome extension captures conversations for storage and retrieval.</li>
          <li>FastAPI handles backend requests; ChromaDB stores embeddings for semantic search.</li>
          <li>A React dashboard supports browsing and searching saved conversations.</li>
        </ul>
      </details>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/JonSnow1807/pytorch-autotune"><img src="https://img.shields.io/badge/View_Code-10B981?style=for-the-badge&amp;logo=github&amp;logoColor=white" height="28" alt="View AutoTune source code" /></a>
      <br><sub><a href="https://github.com/JonSnow1807/pytorch-autotune/tree/main/benchmarks/results/2026-08-25_a100-40gb_v200">Benchmark artifacts and validation</a></sub>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/JonSnow1807/chatgpt-memory-manager"><img src="https://img.shields.io/badge/View_Code-0EA5E9?style=for-the-badge&amp;logo=github&amp;logoColor=white" height="28" alt="View ChatGPT Spark source code" /></a>
      <br><sub><a href="https://chromewebstore.google.com/detail/chatgpt-spark/bieoffmnblcajoahiljjbhffeccojpop">Chrome Web Store listing</a></sub>
    </td>
  </tr>
</table>

<p align="center">
  <strong>Also built:</strong> <a href="https://github.com/JonSnow1807/3D-Point-Cloud-Viewer">3D Point Cloud Viewer</a><br>
  <sub>C++ / OpenGL · Octree-based spatial indexing · View-frustum culling · Level-of-detail rendering</sub>
</p>

<br>

<!-- TOOLBOX -->
<h2 align="center">🛠 Technical Toolbox</h2>

<table align="center" width="100%">
  <tr>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" width="44" height="44" alt="C++" /><br><sub><strong>C++</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="44" height="44" alt="Python" /><br><sub><strong>Python</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.simpleicons.org/rust/A78BFA" width="44" height="44" alt="Rust" /><br><sub><strong>Rust</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.simpleicons.org/nvidia/76B900" width="44" height="44" alt="NVIDIA CUDA" /><br><sub><strong>CUDA</strong></sub><br><br></td>
  </tr>
  <tr>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" width="44" height="44" alt="PyTorch" /><br><sub><strong>PyTorch</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-original.svg" width="44" height="44" alt="Kubernetes" /><br><sub><strong>Kubernetes</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="44" height="44" alt="Docker" /><br><sub><strong>Docker</strong></sub><br><br></td>
    <td width="200" align="center"><br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="44" height="44" alt="Redis" /><br><sub><strong>Redis</strong></sub><br><br></td>
  </tr>
</table>

<details>
<summary><strong>📚 Full stack and tooling</strong></summary>

| Area | Technologies |
| :--- | :--- |
| Languages | C++, C, Python, Rust, Go, CUDA, TypeScript, SQL |
| Backend | FastAPI, NestJS, REST APIs, WebSockets, Server-Sent Events |
| Infrastructure | Linux, Docker, Kubernetes/OpenShift, AWS, CI/CD |
| Data | ClickHouse, PostgreSQL/PostGIS, Redis, ChromaDB |
| ML & performance | PyTorch, `torch.compile`, vLLM, GPU profiling, kernel fusion, benchmark design |
| Correctness | TLA+/TLC, reference-based testing, regression tests, protocol-conformance checks |

</details>

<br>

<!-- WORKING STYLE -->
<h2 align="center">💡 How I Work</h2>

<table align="center" width="100%">
  <tr>
    <td width="33%" align="center" valign="top">
      <h3>🎯 Check the Reference</h3>
      <p>Compare outputs, test failure cases and make correctness assumptions explicit.</p>
    </td>
    <td width="34%" align="center" valign="top">
      <h3>📊 Measure the Baseline</h3>
      <p>Profile the actual workload before deciding what to optimize.</p>
    </td>
    <td width="33%" align="center" valign="top">
      <h3>🔍 Show the Trade-offs</h3>
      <p>Publish the setup, the results and the cases where another approach wins.</p>
    </td>
  </tr>
</table>

<br>

<!-- CONTACT -->
<h2 align="center">📬 Let's Connect</h2>

<p align="center">
  Interested in <strong>backend, distributed systems, ML infrastructure</strong><br>
  and <strong>performance engineering</strong>.<br><br>
  Based in <strong>Frisco, Texas</strong> · Open to relocation
</p>

<p align="center">
  <a href="mailto:cshrivastava2000@gmail.com"><img src="https://img.shields.io/badge/Send_an_Email-8B5CF6?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" height="28" alt="Send an email" /></a>
  &nbsp;
  <a href="https://www.linkedin.com/in/cshrivastava/"><img src="https://img.shields.io/badge/Connect_on_LinkedIn-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" height="28" alt="Connect on LinkedIn" /></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:6D28D9,45:8B5CF6,100:EC4899&amp;height=100&amp;section=footer" width="100%" alt="" />
</p>
