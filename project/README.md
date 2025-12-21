
---

# 🧠 12-Week AI Engineering Study Plan (Engineer Track)

⏱️ **Suggested load**: 10–15 h/week
🛠️ **Core stack**: Python, FastAPI, Docker, PyTorch, LLM APIs, Vector DBs

Below is a **12-week AI Engineering study plan** designed for **application-level mastery**, not academic theory.
It assumes:

* Strong **Python backend background**
* Goal: **build production-ready AI systems (LLMs, RAG, agents)**
* End result: **portfolio-grade AI engineering projects**

Each week includes **concepts, engineering skills, hands-on deliverables, and evaluation criteria**.


---

## 📅 WEEK 1 — AI Engineering Foundations

### 🎯 Objectives

* Understand what AI engineers build
* Differentiate ML research vs AI systems

### 📚 Topics

* AI Engineering lifecycle
* LLMs vs classical ML
* Model-as-a-service
* Failure modes of AI systems

### 🛠️ Hands-on

* Set up environment:

  * Python 3.11
  * venv / poetry
  * FastAPI
* Call LLM via API (OpenAI / local Ollama)

### 📦 Deliverable

✔ Minimal LLM-powered API endpoint

---

## 📅 WEEK 2 — Math & ML Essentials (Engineer View)

### 🎯 Objectives

* Understand math only where it affects systems

### 📚 Topics

* Linear algebra for embeddings
* Probability & entropy
* Loss functions
* Gradient descent intuition

### 🛠️ Hands-on

* Implement:

  * Cosine similarity
  * Simple SGD from scratch
* Visualize embeddings

### 📦 Deliverable

✔ Embedding similarity service

---

## 📅 WEEK 3 — Self-Supervised Learning & Transformers

### 🎯 Objectives

* Understand why LLMs work

### 📚 Topics

* Self-supervised learning
* Transformer architecture
* Attention math
* Tokenization

### 🛠️ Hands-on

* Implement attention in NumPy
* Train a tiny transformer on text

### 📦 Deliverable

✔ Mini transformer demo

---

## 📅 WEEK 4 — Prompt Engineering as Software

### 🎯 Objectives

* Treat prompts like production code

### 📚 Topics

* Prompt patterns
* ReAct
* Chain-of-Thought
* Prompt injection

### 🛠️ Hands-on

* Prompt versioning
* Prompt unit tests
* Deterministic outputs

### 📦 Deliverable

✔ Prompt test suite

---

## 📅 WEEK 5 — Retrieval-Augmented Generation (RAG)

### 🎯 Objectives

* Eliminate hallucinations
* Ground LLMs in data

### 📚 Topics

* Embeddings
* Vector databases
* Chunking strategies
* Reranking

### 🛠️ Hands-on

* Build RAG system:

  * FAISS
  * PDF ingestion
  * Query pipeline

### 📦 Deliverable

✔ RAG API (documents → answers)

---

## 📅 WEEK 6 — Evaluation & Observability

### 🎯 Objectives

* Measure AI system quality

### 📚 Topics

* Offline vs online eval
* Metrics for LLMs
* Cost tracking
* Drift detection

### 🛠️ Hands-on

* Build evaluation harness
* Log prompts & outputs
* Token cost monitoring

### 📦 Deliverable

✔ AI evaluation dashboard

---

## 📅 WEEK 7 — Multi-Agent Systems

### 🎯 Objectives

* Move beyond single LLM calls

### 📚 Topics

* Agent architectures
* Planning vs execution
* Agent communication
* Failure recovery

### 🛠️ Hands-on

* Build agents:

  * Planner
  * Researcher
  * Critic
* Use LangGraph or custom orchestration

### 📦 Deliverable

✔ Multi-agent task solver

---

## 📅 WEEK 8 — Tool Use & Function Calling

### 🎯 Objectives

* Let LLMs interact with the real world

### 📚 Topics

* Function calling
* Tool routing
* Validation
* Sandboxing

### 🛠️ Hands-on

* LLM + tools:

  * DB queries
  * Python execution
* Secure tool access

### 📦 Deliverable

✔ Tool-using AI agent

---

## 📅 WEEK 9 — Fine-Tuning & Adaptation

### 🎯 Objectives

* Customize LLM behavior

### 📚 Topics

* Fine-tuning vs prompting
* LoRA
* Embedding tuning
* Overfitting risks

### 🛠️ Hands-on

* Fine-tune small model
* Compare with RAG

### 📦 Deliverable

✔ Adapted domain model

---

## 📅 WEEK 🔟 — Deployment & Scaling

### 🎯 Objectives

* Make AI systems production-ready

### 📚 Topics

* FastAPI + async
* Docker
* Load balancing
* GPU vs CPU inference

### 🛠️ Hands-on

* Dockerize AI service
* Add caching
* Stress test endpoints

### 📦 Deliverable

✔ Scalable AI API

---

## 📅 WEEK 1️⃣1️⃣ — Safety, Security & Governance

### 🎯 Objectives

* Prevent costly AI failures

### 📚 Topics

* Prompt injection defense
* Bias detection
* Logging & audit
* Compliance (finance context)

### 🛠️ Hands-on

* Input validation
* Safety filters
* Explainability logs

### 📦 Deliverable

✔ Secure AI system

---

## 📅 WEEK 1️⃣2️⃣ — Capstone Project

### 🎯 Objectives

* Demonstrate AI engineering mastery

### 🛠️ Capstone Options

Choose one:

1️⃣ **Multi-Agent Investment Assistant**
2️⃣ **Enterprise Knowledge Copilot**
3️⃣ **Autonomous Research Agent**

### 📦 Final Deliverables

✔ Architecture diagram
✔ Codebase (clean & modular)
✔ Evaluation report
✔ Cost analysis

---

## 🧪 Evaluation Criteria (Real-World)

| Category    | Measure              |
| ----------- | -------------------- |
| Reliability | Error rate           |
| Cost        | Tokens / request     |
| Latency     | P95 response         |
| Accuracy    | Eval scores          |
| Safety      | Injection resistance |

---

## 🚀 After 12 Weeks You Will Be Able To:

* Design AI system architectures
* Build multi-agent LLM systems
* Deploy scalable AI services
* Evaluate & optimize cost/performance
* Speak **AI engineering fluently** in interviews

---