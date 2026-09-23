<!-- Upload this README and assets/profile/ to JonSnow1807/JonSnow1807 together. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/hero-dark.svg">
  <img src="./assets/profile/hero-light.svg" width="100%" alt="Chinmay Shrivastava — Software Engineer. Backend, distributed systems and ML infrastructure.">
</picture>

<p>
  <a href="https://www.linkedin.com/in/cshrivastava/"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/linkedin-dark.svg"><img src="./assets/profile/linkedin-light.svg" width="100" alt="LinkedIn"></picture></a>
  <a href="mailto:cshrivastava2000@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/email-dark.svg"><img src="./assets/profile/email-light.svg" width="88" alt="Email Chinmay"></picture></a>
  <a href="https://huggingface.co/chinmays18"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/huggingface-dark.svg"><img src="./assets/profile/huggingface-light.svg" width="126" alt="Hugging Face"></picture></a>
</p>

**I build high-performance backend and ML infrastructure, and I validate it against references instead of trusting it.**

At **Reliance Jio**, I work on production 4G/5G analytics, deterministic query compilation and GPU-backed inference on Kubernetes/OpenShift, including a **13-node, air-gapped, IPv6-only deployment**. Outside work, I contribute to PyTorch and bpfilter, and build tools for GPU performance and distributed coordination.

## 01 / Upstream contributions

**PyTorch core** — two accepted changes  
Enabled existing dynamic-shape support for foreach operations by default under `torch.compile`, with a test update ([#158985](https://github.com/pytorch/pytorch/pull/158985)). Exposed `rearrange` through the `torch.func` public API, with tests and documentation ([#173183](https://github.com/pytorch/pytorch/pull/173183)).

**Meta’s bpfilter** — two merged pull requests  
Added IPv4 Type of Service and IPv6 Traffic Class matchers, including command-line parsing, BPF code generation and unit tests ([#364](https://github.com/facebook/bpfilter/pull/364), [#369](https://github.com/facebook/bpfilter/pull/369)). The IPv6 implementation uses endianness-safe byte loads.

<sub>PyTorch landing commits: <a href="https://github.com/pytorch/pytorch/commit/51eb41a57ef4365bece0c187f1d751221b88c135">foreach</a> · <a href="https://github.com/pytorch/pytorch/commit/cd59c879a7eb47de27e0eead455b0b0349c12488">rearrange</a>.</sub>

## 02 / Selected builds

<!-- Each project is one row made of two flush images: the body opens the source repository, the action panel opens the shipped or
     measured destination. The 77 % + 22 % widths match the artwork's 539:154 intrinsic ratio, so both halves render at the same height.
     Theme variants only — GitHub's theme-pinning script rewrites combined (max-width + prefers-color-scheme) media queries. -->
<p align="center">
  <a href="https://github.com/JonSnow1807/Mustard-Watch-Party"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/mustard-body-dark.svg"><img src="./assets/profile/mustard-body-light.svg" width="77%" alt="Mustard Watch Party — Multi-instance video synchronization. 48 ms; P95 player-reported drift. 3 Chrome clients / ~300 ms RTT. Steady state / 240-second test. Open the source repository."></picture></a><a href="https://mustard.watch"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/mustard-action-dark.svg"><img src="./assets/profile/mustard-action-light.svg" width="22%" alt="Mustard Watch Party — open Live: mustard.watch."></picture></a>
</p>
<details>
<summary><strong>Inside Mustard</strong> · Clock synchronization, protocol correctness and runtime trade-offs</summary>
<br>
<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/fig-mustard-dark.svg"><img src="./assets/profile/fig-mustard-light.svg" width="700" alt="Mustard: clients estimate a clock offset over the socket ack and correct drift with predictive rate control; room state lives in Redis behind atomic Lua scripts. Chart: steady-state P95 drift 49, 48, 79, 29 and 86 ms across five network scenarios; relay memory 14.5 KB (Rust) versus 40 KB (Go) per connection."></picture></p>

Mustard is a multi-instance watch-party platform: clients connect over WebSockets and use NTP-style clock estimation with predictive drift correction, and updates go through atomic Redis Lua scripts. The **48 ms P95** is a specific claim: **steady-state player-reported drift**, measured across **three Chrome clients** at approximately **300 ms RTT** during a **240-second test**. It is not a physical audio-output measurement.

Protocol correctness was a separate question. TLA+/TLC model checking exposed a stale-epoch bug after store resets, leading to an ordered-epoch fix, and idempotency keys plus atomic updates keep control commands from being applied twice within the deduplication window.

I also built **Go and Rust relays** to test protocol conformance and runtime costs. They are study implementations, not the production backend. In a local 10,000-connection test, the Rust relay used 14.5 KB of memory per connection versus 40 KB for Go; the extreme-tail latency comparison was inconclusive.

[Live site](https://mustard.watch) · [Source](https://github.com/JonSnow1807/Mustard-Watch-Party) · [Sync design](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/SYNC_DESIGN.md) · [TLA+ findings](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/FORMAL.md) · [Go/Rust study](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/relay-rs/README.md)

</details>

<p align="center">
  <a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/cuda-body-dark.svg"><img src="./assets/profile/cuda-body-light.svg" width="77%" alt="Fused CUDA Operators — LayerNorm / RMSNorm for PyTorch. 1.04–1.76×; vs. compiled PyTorch. RMSNorm-to-FP8 / A100 / FP16. Kernel-time comparison. Open the source repository."></picture></a><a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/tree/main/benchmarks/results/2026-08-25_a100-40gb_v050_ops"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/cuda-action-dark.svg"><img src="./assets/profile/cuda-action-light.svg" width="22%" alt="Fused CUDA Operators — open Results: A100 · kernel time."></picture></a>
</p>
<details>
<summary><strong>Inside Fused CUDA operators</strong> · Custom ops, deterministic gradients and FP8</summary>
<br>
<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/fig-cuda-dark.svg"><img src="./assets/profile/fig-cuda-light.svg" width="700" alt="Fused CUDA operators: the eager composite runs residual-add, normalization and an FP8 cast as three kernels with HBM round-trips; the fused version does all three in one kernel. Chart: dynamic RMSNorm to FP8 kernel time is 4.9 to 7.2 times faster than the eager composite and 1.04 to 1.76 times faster than the compiled composite across six shapes on an A100 in FP16."></picture></p>

These LayerNorm/RMSNorm kernels combine **fused residual-add**, **FP8 outputs** and **deterministic backward reductions**, and come as drop-in PyTorch modules that work under `torch.compile` without graph breaks. Parameter gradients use fixed-order reductions rather than atomic accumulation, which is where the determinism comes from.

For dynamic RMSNorm-to-FP8, I measured **4.9–7.2× over the eager PyTorch composite** and **1.04–1.76× over the compiled composite**, across tested **FP16 shapes on an NVIDIA A100**. Those are **kernel-time comparisons**, not end-to-end model speedups. For a fuller picture, the repository also documents H100 results and configurations where PyTorch wins.

[Source](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator) · [A100 results](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/tree/main/benchmarks/results/2026-08-25_a100-40gb_v050_ops) · [Methodology](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/blob/main/docs/methodology.md)

</details>

<p align="center">
  <a href="https://github.com/JonSnow1807/pytorch-autotune"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/autotune-body-dark.svg"><img src="./assets/profile/autotune-body-light.svg" width="77%" alt="PyTorch AutoTune — Workload-specific training optimization. 2.7–6.7×; training-step speedup after tuning. vs. PyTorch-default FP32 eager. 3 workloads / NVIDIA A100. Open the source repository."></picture></a><a href="https://pypi.org/project/pytorch-autotune/"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/autotune-action-dark.svg"><img src="./assets/profile/autotune-action-light.svg" width="22%" alt="PyTorch AutoTune — open PyPI: pytorch-autotune."></picture></a>
</p>
<details>
<summary><strong>Inside PyTorch AutoTune</strong> · Measure the configuration instead of guessing it</summary>
<br>
<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/fig-autotune-dark.svg"><img src="./assets/profile/fig-autotune-light.svg" width="700" alt="PyTorch AutoTune: the baseline is measured first, candidates across precision, compile mode, memory format and fused optimizer run real training steps under a budget, the winner must beat the incumbent by more than 3 percent, and the report and cache record every trial. Chart: 2.71 times on ResNet-50, 3.84 times on ResNet-18 and 6.65 times on a six-layer Transformer versus the PyTorch-default fp32 eager baseline; the Transformer gain is 2.55 times against an eager baseline with TF32 matmuls enabled."></picture></p>

Rather than guess at a training configuration, the tuner benchmarks **precision, compile mode, memory format and fused-optimizer configurations** on the target model and batch. Search runs under a budget, configurations are cached for reuse, and reports show trial results, compilation cost and estimated break-even time.

I measured **2.7–6.7× training-step speedups after tuning** versus the **PyTorch-default FP32 eager baseline** across **ResNet-50, ResNet-18 and a six-layer Transformer on an NVIDIA A100**, with the tuner using `torch.compile` alongside the other optimizations. The baseline matters, though: on the Transformer, the gain is **2.55×** against an eager baseline with TF32 matmuls enabled, rather than 6.65× against the defaults. Search costs and numerical trade-offs are documented as well.

[PyPI](https://pypi.org/project/pytorch-autotune/) · [Source](https://github.com/JonSnow1807/pytorch-autotune) · [Benchmark artifacts](https://github.com/JonSnow1807/pytorch-autotune/tree/main/benchmarks/results/2026-08-25_a100-40gb_v200)

</details>

<p align="center">
  <a href="https://github.com/JonSnow1807/chatgpt-memory-manager"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/spark-body-dark.svg"><img src="./assets/profile/spark-body-light.svg" width="77%" alt="ChatGPT Spark — Conversation capture and semantic search. Published; Chrome Web Store. React dashboard / FastAPI backend. ChromaDB vector search. Open the source repository."></picture></a><a href="https://chromewebstore.google.com/detail/chatgpt-spark/bieoffmnblcajoahiljjbhffeccojpop"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/spark-action-dark.svg"><img src="./assets/profile/spark-action-light.svg" width="22%" alt="ChatGPT Spark — open Web Store: Chrome extension."></picture></a>
</p>
<details>
<summary><strong>Inside ChatGPT Spark</strong> · A shipped extension and its retrieval backend</summary>
<br>
<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/fig-spark-dark.svg"><img src="./assets/profile/fig-spark-light.svg" width="700" alt="ChatGPT Spark: a Chrome extension captures a conversation, a FastAPI backend stores it, ChromaDB holds the embeddings, and a React dashboard browses and semantically searches them. Published on the Chrome Web Store."></picture></p>

Spark is a Chrome extension I built and published for capturing and searching conversation history. A **React/TypeScript dashboard** lets you browse saved conversations, **FastAPI** handles backend requests, and **ChromaDB** stores the embeddings behind semantic search.

[Source](https://github.com/JonSnow1807/chatgpt-memory-manager) · [Chrome Web Store](https://chromewebstore.google.com/detail/chatgpt-spark/bieoffmnblcajoahiljjbhffeccojpop)

</details>

Also built: **[3D Point Cloud Viewer](https://github.com/JonSnow1807/3D-Point-Cloud-Viewer)** — C++/OpenGL, octree-based culling and level-of-detail rendering.

## 03 / Toolbox

| Area | Tools I use |
| :--- | :--- |
| **Languages** | C++, C, Python, Rust, Go, CUDA, TypeScript, SQL |
| **Backend & data** | FastAPI, NestJS, WebSockets, SSE, ClickHouse, PostgreSQL/PostGIS, Redis, ChromaDB |
| **Infrastructure** | Linux, Docker, Kubernetes/OpenShift, AWS, CI/CD |
| **ML & performance** | PyTorch, `torch.compile`, vLLM, GPU profiling, kernel fusion, benchmark design |
| **Correctness** | TLA+/TLC, reference-based tests, regression tests, protocol-conformance checks |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/endmark-dark.svg">
  <img src="./assets/profile/endmark-light.svg" width="100%" alt="">
</picture>

**Have a systems problem worth digging into?**  
I’m interested in backend, distributed-systems, ML-infrastructure and performance-engineering work.

**Frisco, Texas · Open to relocation**  
[Email](mailto:cshrivastava2000@gmail.com) · [LinkedIn](https://www.linkedin.com/in/cshrivastava/) · [Hugging Face](https://huggingface.co/chinmays18)
