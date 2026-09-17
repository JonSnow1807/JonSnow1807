<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=90&color=0:8B5CF6,100:EC4899&section=header" width="100%" alt="" />
</p>

<h1 align="center">Chinmay Shrivastava</h1>

<p align="center">
  <strong>Software Engineer · Backend &amp; Distributed Systems · ML Infrastructure</strong>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/cshrivastava/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;
  <a href="mailto:cshrivastava2000@gmail.com">
    <img src="https://img.shields.io/badge/Email-8B5CF6?style=flat-square&logo=gmail&logoColor=white" alt="Email Chinmay" />
  </a>
  &nbsp;
  <a href="https://huggingface.co/chinmays18">
    <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" />
  </a>
</p>

## About

I build high-performance backend and ML infrastructure, and I validate it against references instead of trusting it.

At **Reliance Jio**, I work on production 4G/5G analytics, deterministic query compilation and GPU-backed inference services on Kubernetes/OpenShift. Outside work, I contribute to **PyTorch** and **Meta's bpfilter**, and build tools for GPU performance and distributed coordination.

## Upstream Contributions

### PyTorch Core

- Enabled existing dynamic-shape support for foreach operations by default under `torch.compile`, with a corresponding test update — [#158985](https://github.com/pytorch/pytorch/pull/158985).
- Exposed `rearrange` through the `torch.func` public API, with tests and documentation — [#173183](https://github.com/pytorch/pytorch/pull/173183).

### Meta's bpfilter

- Added an IPv4 Type of Service matcher, including command-line parsing, BPF code generation and unit tests — [#364](https://github.com/facebook/bpfilter/pull/364).
- Added an IPv6 Traffic Class matcher with endianness-safe byte loads, command-line support and unit tests — [#369](https://github.com/facebook/bpfilter/pull/369).

All four changes were accepted upstream. The PyTorch changes landed through the project's merge-bot workflow: [foreach commit](https://github.com/pytorch/pytorch/commit/51eb41a57ef4365bece0c187f1d751221b88c135) · [rearrange commit](https://github.com/pytorch/pytorch/commit/cd59c879a7eb47de27e0eead455b0b0349c12488).

## Selected Projects

### Mustard Watch Party — Distributed Video Synchronization

`TypeScript` `NestJS` `WebSockets` `Redis` `TLA+` `Go` `Rust`

Built a multi-instance watch-party platform with NTP-style clock estimation, predictive drift correction and atomic Redis Lua updates. Measured **48 ms P95 steady-state, player-reported drift** across three Chrome clients at approximately **300 ms round-trip latency** in a 240-second test scenario.

TLA+/TLC model checking exposed a stale-epoch bug that could roll clients back to old state after a store reset, leading to an ordered-epoch fix. Separate Go and Rust relays test protocol conformance and runtime costs; these are study implementations, not the production backend.

[Source](https://github.com/JonSnow1807/Mustard-Watch-Party) · [Sync Design](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/SYNC_DESIGN.md) · [Model-Checking Findings](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/docs/FORMAL.md) · [Go/Rust Study](https://github.com/JonSnow1807/Mustard-Watch-Party/blob/main/relay-rs/README.md)

---

### Fused LayerNorm / RMSNorm — CUDA Operators for PyTorch

`C++` `CUDA` `PyTorch` `torch.compile` `FP8`

Built normalization kernels with fused residual-add, FP8 outputs and deterministic backward reductions. Drop-in PyTorch modules work under `torch.compile` without graph breaks.

Dynamic RMSNorm-to-FP8 measured **4.9–7.2× kernel-time speedup over the eager PyTorch composite** and **1.04–1.76× over the compiled composite**, across tested FP16 shapes on an **NVIDIA A100**. These are operator-level results; the repository also documents H100 comparisons and configurations where PyTorch wins.

[Source](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator) · [A100 Benchmark Artifacts](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/tree/main/benchmarks/results/2026-08-25_a100-40gb_v050_ops) · [Methodology](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/blob/main/docs/methodology.md)

---

### PyTorch AutoTune — Measurement-Driven Training Optimization

`Python` `PyTorch` `CUDA` `Benchmarking`

Built a training autotuner that measures combinations of precision, `torch.compile` mode, memory format and fused optimizer on the target model and batch. It includes budgeted search, configuration caching and reports covering trial results, compilation cost and estimated break-even time.

Measured **2.7–6.7× training-step speedups after tuning** versus the **PyTorch-default FP32 eager baseline** across ResNet-50, ResNet-18 and a six-layer Transformer on an **NVIDIA A100**. The tuner uses `torch.compile` alongside the other optimizations. Search costs, numerical trade-offs and alternative baselines are documented with the results.

[Source](https://github.com/JonSnow1807/pytorch-autotune) · [Benchmark Artifacts and Validation](https://github.com/JonSnow1807/pytorch-autotune/tree/main/benchmarks/results/2026-08-25_a100-40gb_v200)

---

### Other Work

**[ChatGPT Spark](https://github.com/JonSnow1807/chatgpt-memory-manager)**  
A Chrome extension for capturing and searching conversation history, with a React/TypeScript dashboard, FastAPI and ChromaDB. [Chrome Web Store](https://chromewebstore.google.com/detail/chatgpt-spark/bieoffmnblcajoahiljjbhffeccojpop).

**[3D Point Cloud Viewer](https://github.com/JonSnow1807/3D-Point-Cloud-Viewer)**  
A C++/OpenGL viewer with octree-based spatial indexing, view-frustum culling and level-of-detail rendering.

## Toolbox

| Area | Technologies |
| :--- | :--- |
| Languages | C++, C, Python, Rust, Go, CUDA, TypeScript, SQL |
| Backend | FastAPI, NestJS, REST APIs, WebSockets, Server-Sent Events |
| Infrastructure | Linux, Docker, Kubernetes/OpenShift, AWS, CI/CD |
| Data | ClickHouse, PostgreSQL/PostGIS, Redis, ChromaDB |
| ML & performance | PyTorch, `torch.compile`, vLLM, GPU profiling, kernel fusion, benchmark design |
| Correctness | TLA+/TLC, reference-based testing, regression tests, protocol-conformance checks |

## Connect

Based in **Frisco, Texas** and open to relocation. Interested in backend, distributed-systems, ML-infrastructure and performance-engineering roles.

[Email](mailto:cshrivastava2000@gmail.com) · [LinkedIn](https://www.linkedin.com/in/cshrivastava/) · [Hugging Face](https://huggingface.co/chinmays18)
