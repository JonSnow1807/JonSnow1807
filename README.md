<!-- Clean, professional header inspired by AlgoExpert -->
<div align="center">
  <br><br><br>
  
  <!-- Name with clean typography -->
  <h1 style="font-weight: 600; font-size: 48px; margin-bottom: 0;">
    Chinmay Shrivastava
  </h1>
  
  <!-- Professional tagline -->
  <p style="font-size: 20px; color: #6B7280; margin-top: 10px;">
    Software Engineer × AI/ML Developer × Performance Architect
  </p>
  
  <br>
  
  <!-- Clean contact buttons -->
  <p>
    <a href="https://linkedin.com/in/cshrivastava">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
    </a>
    &nbsp;&nbsp;
    <a href="mailto:cshrivastava2000@gmail.com">
      <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
    </a>
    &nbsp;&nbsp;
    <a href="https://huggingface.co/chinmays18">
      <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face" />
    </a>
  </p>
  
  <br>
  
  <!-- Impact metrics in a clean row -->
  <p>
    <img src="https://img.shields.io/badge/1.46x-CUDA_Speedup-000000?style=flat&labelColor=E5E7EB" />
    &nbsp;
    <img src="https://img.shields.io/badge/858_FPS-3D_Rendering-000000?style=flat&labelColor=E5E7EB" />
    &nbsp;
    <img src="https://img.shields.io/badge/94%25-ML_Accuracy-000000?style=flat&labelColor=E5E7EB" />
    &nbsp;
    <img src="https://img.shields.io/badge/<500ms-Sync_Latency-000000?style=flat&labelColor=E5E7EB" />
  </p>
  
  <br>
</div>

---

## About

I transform complex challenges into elegant solutions that scale. From optimizing CUDA kernels with 1.46x speedups to building real-time platforms handling thousands of concurrent users, I thrive at the intersection of technical excellence and business impact.

My approach is simple: **measure twice, optimize once, ship constantly**. Whether it's achieving 94% accuracy in production ML systems or rendering 1M+ points at 858 FPS, I believe in pushing the boundaries of what's possible while keeping the user experience at the center.

Currently seeking opportunities to tackle meaningful challenges at companies building the future.

---

## Featured Projects

<br>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🤖 Intelligent Knowledge Assistant</h3>
      <p>
        <code>Production RAG</code> <code>94% accuracy</code> <code>Fine-tuned LLM</code>
      </p>
      <p>
        Built a production RAG system with fine-tuned Llama-3.1-8B that matches GPT-4 quality at a fraction of the cost. Implemented custom attention caching that reduced latency by 73%, enabling real-time responses.
      </p>
      <details>
        <summary><b>Technical Details</b></summary>
        <br>
        <ul>
          <li>Architecture: Hierarchical vector indexing with FAISS</li>
          <li>Innovation: Custom KV-cache optimization for transformers</li>
          <li>Stack: PyTorch, LangChain, FastAPI, PostgreSQL</li>
          <li>Deployment: Kubernetes with horizontal autoscaling</li>
        </ul>
      </details>
      <br>
      <a href="https://github.com/JonSnow1807/llm-knowledge-assistant">
        <img src="https://img.shields.io/badge/View_Project-000000?style=for-the-badge&logo=github&logoColor=white" />
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>🎬 Real-time Collaboration Platform</h3>
      <p>
        <code>&lt;500ms sync</code> <code>1000+ concurrent</code> <code>WebSocket protocol</code>
      </p>
      <p>
        Created a video watch party platform with perfect synchronization across distributed clients. Engineered a binary WebSocket protocol with delta compression, achieving sub-500ms latency at scale.
      </p>
      <details>
        <summary><b>Technical Details</b></summary>
        <br>
        <ul>
          <li>Protocol: Custom binary format over WebSocket</li>
          <li>Scaling: Redis pub/sub for horizontal distribution</li>
          <li>Stack: React, NestJS, Socket.IO, Redis</li>
          <li>Security: JWT with room-based permissions</li>
        </ul>
      </details>
      <br>
      <a href="https://github.com/JonSnow1807/Mustard-Watch-Party">
        <img src="https://img.shields.io/badge/View_Project-000000?style=for-the-badge&logo=github&logoColor=white" />
      </a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>⚡ GPU Performance Engineering</h3>
      <p>
        <code>1.46x speedup</code> <code>95.3% efficiency</code> <code>Kernel fusion</code>
      </p>
      <p>
        Developed fused CUDA kernels for transformer models, achieving near-theoretical memory bandwidth utilization. This optimization enables significant compute cost reductions for LLM inference.
      </p>
      <details>
        <summary><b>Technical Details</b></summary>
        <br>
        <ul>
          <li>Technique: Kernel fusion for LayerNorm + Activation</li>
          <li>Memory: Coalesced access patterns, shared memory</li>
          <li>Stack: CUDA C++, PyTorch extensions, nvprof</li>
          <li>Impact: 46% inference speedup for LLMs</li>
        </ul>
      </details>
      <br>
      <a href="https://github.com/JonSnow1807/Fused-LayerNorm-CUDA-Operator">
        <img src="https://img.shields.io/badge/View_Project-000000?style=for-the-badge&logo=github&logoColor=white" />
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>🎮 High-Performance 3D Visualization</h3>
      <p>
        <code>858 FPS</code> <code>1M+ points</code> <code>7.2x faster</code>
      </p>
      <p>
        Built a 3D point cloud viewer that outperforms industry standards by 7.2x. Implemented custom spatial indexing and SIMD optimizations to achieve real-time rendering of massive datasets.
      </p>
      <details>
        <summary><b>Technical Details</b></summary>
        <br>
        <ul>
          <li>Algorithm: Custom octree with frustum culling</li>
          <li>Rendering: Instanced drawing with GPU batching</li>
          <li>Stack: C++17, OpenGL 4.5, GLM, ImGui</li>
          <li>Optimization: SIMD intrinsics for transforms</li>
        </ul>
      </details>
      <br>
      <a href="https://github.com/JonSnow1807/3D-Point-Cloud-Viewer">
        <img src="https://img.shields.io/badge/View_Project-000000?style=for-the-badge&logo=github&logoColor=white" />
      </a>
    </td>
  </tr>
</table>

---

## Technical Stack

<div align="center">

### Languages & Core Technologies
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" />
</p>

### AI/ML Stack
<p>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/LangChain-121212?style=flat-square&logoColor=white" />
  <img src="https://img.shields.io/badge/RAG-4285F4?style=flat-square&logoColor=white" />
  <img src="https://img.shields.io/badge/FAISS-00A4EF?style=flat-square&logoColor=white" />
</p>

### Full-Stack & Infrastructure
<p>
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
</p>

</div>

<details>
<summary align="center"><b>View Complete Stack</b></summary>

<br>

```yaml
Core Languages:
  Expert: [Python, TypeScript, C++, JavaScript]
  Proficient: [CUDA, SQL, Bash]

AI/ML Stack:
  Frameworks: [PyTorch, Transformers, LangChain, scikit-learn]
  Techniques: [Fine-tuning, RAG, Embeddings, Vector Search]
  Production: [ONNX, TensorRT, Model Quantization, Batching]
  
Backend Engineering:
  Python: [FastAPI, Django, Flask, Celery]
  Node.js: [NestJS, Express, Socket.IO, Bull]
  APIs: [REST, GraphQL, gRPC, WebSockets]
  
Frontend Development:
  Core: [React, Next.js, Redux, TypeScript]
  UI: [Tailwind CSS, Material-UI, Framer Motion]
  Advanced: [Three.js, D3.js, WebRTC, Canvas API]
  
Data & Infrastructure:
  Databases: [PostgreSQL, MongoDB, Redis, Elasticsearch]
  Vector DBs: [Pinecone, FAISS, Chroma, Qdrant]
  Message Queues: [RabbitMQ, Kafka, Redis Pub/Sub]
  
DevOps & Cloud:
  Containers: [Docker, Docker Compose, Buildkit]
  Orchestration: [Kubernetes, Helm, ArgoCD]
  CI/CD: [GitHub Actions, GitLab CI, Jenkins]
  Cloud: [AWS (EC2, S3, Lambda), GCP, Vercel]
  
Performance & Systems:
  GPU: [CUDA, cuDNN, Thrust, OptiX]
  CPU: [SIMD, OpenMP, Threading, Profiling]
  Graphics: [OpenGL, Vulkan, Shaders]
```

</details>

---

## Engineering Philosophy

<table>
  <tr>
    <td width="25%" align="center">
      <h3>🎯</h3>
      <b>User First</b>
      <br>
      <sub>Every optimization should improve the user experience</sub>
    </td>
    <td width="25%" align="center">
      <h3>📊</h3>
      <b>Data Driven</b>
      <br>
      <sub>Measure twice, optimize once, validate always</sub>
    </td>
    <td width="25%" align="center">
      <h3>🚀</h3>
      <b>Ship Fast</b>
      <br>
      <sub>Perfect tomorrow loses to good today</sub>
    </td>
    <td width="25%" align="center">
      <h3>∞</h3>
      <b>Think Scale</b>
      <br>
      <sub>Build for 10x growth from day one</sub>
    </td>
  </tr>
</table>

---

## What I Bring to Your Team

<div align="center">

| Capability | Evidence |
|:-----------|:---------|
| **Full Product Ownership** | Shipped end-to-end solutions from concept to production |
| **Performance Excellence** | 1.46x-7.2x measurable improvements |
| **Production Experience** | Scalable systems with real-time performance |
| **Technical Depth** | From CUDA kernels to React components |
| **Rapid Execution** | Proven ability to deliver working solutions quickly |

</div>

---

## Looking For My Next Adventure

I'm excited about joining teams that are:

- **Building products that matter** - Real problems, real impact, real users
- **Pushing technical boundaries** - Where "impossible" is just another challenge
- **Moving fast with purpose** - Velocity with vision, not just for speed's sake
- **Creating the future** - Not just following trends, but setting them

<div align="center">
  <br>
  
  **Open to opportunities in:**
  
  `Software Engineering` • `AI/ML Engineering` • `Technical Leadership` • `Performance`
  
</div>

---

## Let's Connect

<div align="center">
  <br>
  
  I'm always excited to discuss challenging problems and explore how I can contribute to your team's success.
  
  Whether you're building the next breakthrough in AI, scaling systems to billions, or creating products that change lives - let's talk.
  
  <br><br>
  
  <a href="mailto:cshrivastava2000@gmail.com">
    <img src="https://img.shields.io/badge/Send_an_Email-000000?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://linkedin.com/in/cshrivastava">
    <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://huggingface.co/chinmays18">
    <img src="https://img.shields.io/badge/Hugging_Face_Profile-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  </a>
  
  <br><br>
  
  <img src="https://komarev.com/ghpvc/?username=JonSnow1807&label=Profile%20Views&color=374151&style=flat" />
  
  <br><br>
  
  ---
  
  <sub>
    <b>Status:</b> Actively seeking new opportunities | 
    <b>Availability:</b> Immediate | 
    <b>Location:</b> Flexible/Remote
  </sub>
</div>
