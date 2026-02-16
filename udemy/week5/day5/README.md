# 10 RAG Advanced Techniques

1. **Chunking R&D**: experiment with chunking strategy  
2. **Encoder R&D**: select the best Encoder model based on a test set  
3. **Improve Prompts**: general content, the current date, relevant context and history  
4. **Document pre-processing**: use an LLM to make the chunks and/or text for encoding  
5. **Query rewriting**: use an LLM to convert the user’s question to a RAG query  
6. **Query expansion**: use an LLM to turn the question into multiple RAG queries  
7. **Re-ranking**: use an LLM to sub-select from RAG results  
8. **Hierarchical**: use an LLM to summarize at multiple levels  
9. **Graph RAG**: retrieve content closely related to similar documents  
10. **Agentic RAG**: use Agents for retrieval, combining with Memory and Tools such as SQL

---
# 1. **Chunking R&D**

Chunking R&D means systematically experimenting with how you split documents into chunks to maximize retrieval quality in a RAG system.

## What is Chunking in RAG?

In **Retrieval-Augmented Generation (RAG)**, large documents are split into smaller pieces called **chunks** before being embedded and stored in a vector database.

When a user asks a question:

1. The query is embedded.
2. The system retrieves the most similar chunks.
3. The LLM generates an answer using those chunks.

If chunking is bad → retrieval is bad → answers degrade.

---

# What “Chunking R&D” Actually Means

It means **testing different chunking strategies** and measuring which one produces the best retrieval performance.

Instead of randomly picking:

* “500 tokens per chunk”
* “100 token overlap”

You experiment and evaluate.

---

# Why Chunking Strategy Matters

Poor chunking can cause:

* ❌ Missing important context
* ❌ Splitting definitions from explanations
* ❌ Mixing unrelated topics in one chunk
* ❌ Retrieving incomplete information

Good chunking improves:

* ✅ Recall (retrieves relevant info)
* ✅ Precision (retrieves only relevant info)
* ✅ Answer accuracy
* ✅ Lower hallucination rate

---

# What You Experiment With

## 1️⃣ Chunk Size

* Small chunks (100–300 tokens)

  * More precise
  * Risk losing context

* Medium chunks (400–800 tokens)

  * Balanced
  * Most common default

* Large chunks (1000+ tokens)

  * More context
  * Lower embedding specificity

You test different sizes and measure retrieval quality.

---

## 2️⃣ Overlap Size

Overlap means repeating some tokens between chunks.

Example:

* Chunk 1: tokens 0–500
* Chunk 2: tokens 450–950

Overlap helps preserve context across boundaries.

You test:

* 0 overlap
* 10%
* 20%
* 30%

---

## 3️⃣ Semantic Chunking vs Fixed Token Chunking

### Fixed Token Chunking

Split every N tokens.

Simple but may cut sentences or ideas.

---

### Semantic Chunking

Split:

* By paragraphs
* By headings
* By sections
* By topic shifts
* By sentence similarity

Often better for:

* Technical docs
* Legal docs
* Research papers

---

## 4️⃣ Structure-Aware Chunking

For structured data:

* Markdown → split by headers
* HTML → split by DOM sections
* PDFs → split by sections
* Code → split by functions/classes

This often dramatically improves retrieval quality.

---

## 5️⃣ Dynamic / LLM-Based Chunking

Use an LLM to:

* Detect logical sections
* Create summaries per chunk
* Rewrite chunks for better embedding

More expensive — but sometimes powerful.

---

# How to Evaluate Chunking (Very Important)

Chunking R&D must be measured.

You typically evaluate:

### 🔹 Retrieval metrics

* Recall@k
* Precision@k
* MRR
* nDCG

### 🔹 End-to-end metrics

* Answer accuracy
* Faithfulness
* Hallucination rate

---

# Example (Practical)

Imagine a documentation site:

Bad chunking:

```
Chunk 1: API intro + half authentication section
Chunk 2: second half authentication + half rate limits
```

User question:

> “How do I authenticate?”

You might retrieve incomplete info.

Better chunking:

* One chunk per section
* Heading-aware splitting

Now retrieval improves significantly.

---

# Why Advanced RAG Systems Invest in Chunking R&D

Top RAG systems (production-grade) treat chunking as:

> A core optimization problem — not a preprocessing afterthought.

In many real-world systems, improving chunking yields more gains than:

* Changing the LLM
* Increasing model size
* Using more expensive embeddings

---

# If You’re Building RAG in Python

You should experiment with:

* Different token sizes
* Different overlap ratios
* Header-based splitting
* Semantic splitting
* Evaluating retrieval performance automatically

---

If you’d like, I can next show:

* 🔬 A Python experiment framework for chunking evaluation
* 📊 How to benchmark chunking strategies
* 🧠 When to use semantic vs fixed chunking
* 🚀 How chunking interacts with embedding model choice

Which direction do you want to go?
