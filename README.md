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

At **Reliance Jio**, I work on production 4G/5G analytics, deterministic query compilation and GPU-backed inference on Kubernetes/OpenShift, including a **13-node, air-gapped, IPv6-only deployment**. Outside work, I contribute to vLLM, PyTorch, DuckDB, bpfilter and other C++ and ML projects, and build tools for GPU performance and distributed coordination.

## 01 / Upstream contributions

**Seventeen merged changes across eight upstream projects** (vLLM, PyTorch, DuckDB, bpfilter, Apache Arrow nanoarrow, Apache Arrow Rust, OpenTelemetry C++, unordered_dense); the ten 2026 bug fixes each carry a regression test that fails without the fix, and every GPU claim below was measured on rented hardware and published.

**vLLM** — one merged pull request  
With the ARC eviction policy, the CPU KV-cache offload tier evicted a running request's first chunks before its last ones, so the chunks it kept could never be hit, since lookup needs a contiguous prefix from chunk 0. ARC now evicts a running request's chunks tail first, as LRU does. After 16 concurrent 2,048-token prompts on an RTX 4090, resident but unreachable chunks fell from 252 to 0, and replaying the prompts hit 8,016 cached tokens instead of 4,096, the same as LRU ([#67098](https://github.com/vllm-project/vllm/pull/67098)).

**PyTorch core** — four accepted changes  
Enabled existing dynamic-shape support for foreach operations by default under `torch.compile`, with a test update ([#158985](https://github.com/pytorch/pytorch/pull/158985)). Exposed `rearrange` through the `torch.func` public API, with tests and documentation ([#173183](https://github.com/pytorch/pytorch/pull/173183)). Fixed the cuDNN CTC loss for strided `log_probs` and zero-initialized its gradient buffer, which cuDNN leaves unwritten past each sequence's length, with tests that compare loss and gradient against the native kernel ([#203097](https://github.com/pytorch/pytorch/pull/203097)). Fixed sparse CSR `add`, `addmm`, `mm` and `sampled_addmm` with `out=`, which wrote into the wrong elements of a strided `out.values()` view, by applying the fix the sparse maintainer posted on the issue, with two corrections and regression tests ([#203228](https://github.com/pytorch/pytorch/pull/203228)).

**DuckDB** — three merged pull requests  
A `CASE` or `IF` that passed a hash join's dictionary column through for some chunks only made the operator cache throw an INTERNAL error that invalidated the database; the cache now demotes such a column to flat ([#27979](https://github.com/duckdb/duckdb/pull/27979)). `SELECT DISTINCT` over an unnested struct covered only the columns as written, not the expanded fields, so rows collapsed wrongly; the binder now regenerates the targets after binding ([#27973](https://github.com/duckdb/duckdb/pull/27973)). The deprecated materialized C API left a result half-initialized when it met an untyped `SQLNULL` column, so later accessors read a missing null mask and segfaulted on `SELECT NULL, 42`; translation now handles `SQLNULL` ([#27707](https://github.com/duckdb/duckdb/pull/27707)).

**Meta’s bpfilter** — three merged pull requests  
Added IPv4 Type of Service and IPv6 Traffic Class matchers, including command-line parsing, BPF code generation and unit tests ([#364](https://github.com/facebook/bpfilter/pull/364), [#369](https://github.com/facebook/bpfilter/pull/369)); the IPv6 implementation uses endianness-safe byte loads. Fixed `meta.probability` above 50 %, where a sign-extended 32-bit immediate in a 64-bit BPF compare made every such rule match 100 % of packets ([#597](https://github.com/facebook/bpfilter/pull/597)).

**Apache Arrow Rust** — three merged pull requests  
The Parquet Arrow writer counted every row, nulls included, when deciding whether to build a dictionary cache, so mostly-null or all-null dictionary columns allocated a cache they never used; it now counts the selected non-null values across the whole write, and an all-null 131,072-row column retains 168 bytes instead of 524,456 ([#12122](https://github.com/apache/arrow-rs/pull/12122)). Added benchmarks for Parquet level encoding and nested writer cases, the baseline for encoding levels a group at a time ([#12213](https://github.com/apache/arrow-rs/pull/12213)). Sped up sparse-dictionary row encoding in `arrow-row` by gathering Utf8, LargeUtf8, Binary and LargeBinary dictionary values with typed kernels instead of a per-row dynamic extend: about 21–24 % lower mean time on the prepared 8,192-row string-dictionary benchmark for dictionaries of 32K–4M values ([#12113](https://github.com/apache/arrow-rs/pull/12113)).

**Apache Arrow nanoarrow and OpenTelemetry C++** — one merged pull request each  
Made nanoarrow's testing JSON comparison recurse into nested and dictionary child fields' metadata ([#993](https://github.com/apache/arrow-nanoarrow/pull/993)). Removed a misaligned `sockaddr_in` access in OpenTelemetry C++'s `SocketAddr`, with a regression test that fails on the original header even without sanitizers ([#4725](https://github.com/open-telemetry/opentelemetry-cpp/pull/4725)).

**unordered_dense** — one merged pull request  
`clear()` writes the whole index, so it costs as much as the largest size the table ever had. Added an opt-in `clear(clear_mode::sparse)` that, below one entry per 16 groups, empties each entry by its own probe walk: 16 entries left after a 4M-entry peak clear in about 95 ns instead of about 820 µs (Ryzen 9 7950X). Plain `clear()` is unchanged, since it must still work after keys were moved out ([#387](https://github.com/martinus/unordered_dense/pull/387)).

<sub>Landing commits: vLLM <a href="https://github.com/vllm-project/vllm/commit/19812fa0be0ae219004e25c25ed10126a07a8bb5">ARC eviction</a> · PyTorch <a href="https://github.com/pytorch/pytorch/commit/51eb41a57ef4365bece0c187f1d751221b88c135">foreach</a> · <a href="https://github.com/pytorch/pytorch/commit/cd59c879a7eb47de27e0eead455b0b0349c12488">rearrange</a> · <a href="https://github.com/pytorch/pytorch/commit/6baba5af876ef727695ff50ae91d8375640e5c71">CTC loss</a> · <a href="https://github.com/pytorch/pytorch/commit/125d69e00d18be14a7b003c0da96828aad779da0">sparse CSR out=</a> · DuckDB <a href="https://github.com/duckdb/duckdb/commit/5b97627c8e0e372a4b0bade9b8a757e2c91bde33">dictionary cache</a> · <a href="https://github.com/duckdb/duckdb/commit/9adc99d292377c206a4bc8940ce45034abd4076c">DISTINCT</a> · <a href="https://github.com/duckdb/duckdb/commit/698d813711525223b6b5c45b3c51588520085498">SQLNULL</a> · bpfilter <a href="https://github.com/facebook/bpfilter/commit/bcae69370eecd1cd939f9ab8d316d3ed363cf9d0">probability</a> · arrow-rs <a href="https://github.com/apache/arrow-rs/commit/da51f1468a52e411f3eec31e7bd929ddd2f5ab88">dictionary cache</a> · <a href="https://github.com/apache/arrow-rs/commit/cd91f89509f42e3984b9adac86ebb9fe83498c81">level benchmarks</a> · <a href="https://github.com/apache/arrow-rs/commit/f2d96279c5145c357e4faec5577a055f39693d74">dictionary gather</a> · nanoarrow <a href="https://github.com/apache/arrow-nanoarrow/commit/08d23f647c4a81b20bf3af902c93d23401a76b24">metadata</a> · OpenTelemetry <a href="https://github.com/open-telemetry/opentelemetry-cpp/commit/23786b7889960041a5cd77ca0bfd501eff01eb99">sockaddr</a> · unordered_dense <a href="https://github.com/martinus/unordered_dense/commit/e90ee4e05b62f8c2c3bdfbdc43ecc33b44563fa4">sparse clear</a>.</sub>

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

For dynamic RMSNorm-to-FP8, I measured **4.9–7.2× over the eager PyTorch composite** and **1.04–1.76× over the compiled composite**, across tested **FP16 shapes on an NVIDIA A100**. Those are **kernel-time comparisons**, not end-to-end model speedups. For a fuller picture, the repository also documents H100 results and configurations where PyTorch wins. v0.6.0 (October 2026) adds a register-resident few-row RMSNorm kernel and a warp-per-row dynamic-FP8 path for Hopper; in an A/B against v0.5.0 on an H100 NVL, the few-row kernel is faster at every measured shape of width ≥ 4096 in all three dtypes, with per-op medians of 0.62–0.85× the v0.5.0 kernel time ([results](https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator/tree/main/benchmarks/results/2026-10-29_h100-nvl_v060_fastpaths)).

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

**[infer-determinism](https://github.com/JonSnow1807/infer-determinism)** — finds where LLM-inference GPU kernels stop being deterministic or batch-invariant, by comparing raw output bits for a fixed probe request under batch-size, position, padding, split-KV and CUDA-graph perturbations. The first run on an **H100 NVL** covered seven targets (PyTorch, vLLM, FlashInfer, vLLM FlashAttention, fused MoE). No divergence was recorded for the runnable `torch_sdpa` backends, vLLM's direct batch-invariant kernels, fused MoE, or FA2/FA3 with `num_splits=1`; it recorded two candidates: float32 `torch.mm` after vLLM's `init_batch_invariance()` (low severity, since model `Linear` layers use the Triton path), and FlashInfer CUDA-core decode with `disable_split_kv=True`, already reported upstream as [flashinfer#7981](https://github.com/flashinfer-ai/flashinfer/issues/7981). That run's attention probes used head dimension 64. A second H100 run added GQA, head dimensions 128 and 256, sliding windows and FP8 KV cache: vLLM FlashAttention with `num_splits=1` and FlashInfer tensor-core decode with `disable_split_kv=True` showed no divergence, and one low-severity candidate turned up, FlashInfer prefill at head dimension 128 giving different bits under CUDA-graph replay than in eager mode. Both runs used one GPU. [Source](https://github.com/JonSnow1807/infer-determinism) · [Run 1 results](https://github.com/JonSnow1807/infer-determinism/tree/master/results/2026-11-06_h100) · [Run 2 results](https://github.com/JonSnow1807/infer-determinism/tree/master/results/2026-11-09_h100)

**[spsc-latency](https://github.com/JonSnow1807/spsc-latency)** — four bounded single-producer/single-consumer ring buffers in C++20, written from scratch (sequentially consistent indices on one cache line, acquire/release on one line, separate lines, and separate lines with a cached peer index), with a throughput and round-trip-latency harness and stress and ThreadSanitizer tests of 100 million transfers per design. On a pinned **Threadripper PRO 3995WX** (shared rented host), the cached design moved 133.8 M items/s with a one-way p99.9 of 140.5 ns for 8-byte messages at capacity 1024, median of 3 trials, clock overhead not subtracted. An unpinned Apple M2 Pro run is also committed. [Source](https://github.com/JonSnow1807/spsc-latency) · [x86 results](https://github.com/JonSnow1807/spsc-latency/tree/master/results/x86-threadripper-3995wx) · [M2 results](https://github.com/JonSnow1807/spsc-latency/tree/master/results/macbook-m2)

**[orderbook-latency](https://github.com/JonSnow1807/orderbook-latency)** — a single-instrument limit order book in C++20 with a `std::map` baseline and a preallocated engine that does not allocate on the hot path; a differential test replays 500,000 messages through both and checks they agree, under normal and ASan/UBSan builds. On a pinned **Threadripper PRO 3995WX** (shared rented host), the fast engine's p99.9 was 281 ns against 471 ns, and its batched throughput 20.8 against 10.7 M messages/s, median of 3 repeats on the default synthetic stream, timer overhead not subtracted. Single-threaded, not an exchange gateway. [Source](https://github.com/JonSnow1807/orderbook-latency) · [x86 results](https://github.com/JonSnow1807/orderbook-latency/tree/master/results/x86-threadripper-3995wx) · [M2 results](https://github.com/JonSnow1807/orderbook-latency/tree/master/results/macbook-m2)

Also built: **[3D Point Cloud Viewer](https://github.com/JonSnow1807/3D-Point-Cloud-Viewer)** — C++/OpenGL, octree-based culling and level-of-detail rendering.

## 03 / Toolbox

| Area | Tools I use |
| :--- | :--- |
| **Languages** | C++, C, Python, Rust, Go, CUDA, TypeScript, SQL |
| **Backend & data** | FastAPI, NestJS, WebSockets, SSE, ClickHouse, PostgreSQL/PostGIS, Redis, ChromaDB |
| **Infrastructure** | Linux, Docker, Kubernetes/OpenShift, AWS, CI/CD |
| **ML & performance** | PyTorch internals, `torch.compile`, vLLM, cuSPARSE/cuDNN, GPU profiling, kernel fusion, benchmark design |
| **Correctness** | TLA+/TLC, reference-based tests, failing-first regression tests, deterministic-mode checks, protocol-conformance checks |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/endmark-dark.svg">
  <img src="./assets/profile/endmark-light.svg" width="100%" alt="">
</picture>

**Have a systems problem worth digging into?**  
I’m interested in backend, distributed-systems, ML-infrastructure and performance-engineering work.

**Frisco, Texas · Open to relocation**  
[Email](mailto:cshrivastava2000@gmail.com) · [LinkedIn](https://www.linkedin.com/in/cshrivastava/) · [Hugging Face](https://huggingface.co/chinmays18)
