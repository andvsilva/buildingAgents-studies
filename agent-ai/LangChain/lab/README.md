Here is a clean and professional **README.md** for your project:

---

# 📚 Compliance RAG Assistant

A **Retrieval-Augmented Generation (RAG)** compliance assistant built with **Streamlit**, **LangChain**, **OpenAI**, and **ChromaDB**.

This application allows users to ask compliance-related questions and receive answers strictly based on internal company documents stored in a vector database.

---

## 🚀 Features

* 💬 Chat-based interface (Streamlit)
* 🧠 GPT-powered responses using `gpt-4o-mini`
* 📂 Vector search using ChromaDB
* 🔎 Semantic retrieval with OpenAI embeddings (`text-embedding-3-small`)
* 🧾 Context-restricted answers (no hallucinations)
* 💾 Persistent vector database (`./chroma_db`)
* 🗂 Chat session memory inside Streamlit session

---

## 🏗 Architecture Overview

The assistant follows a **RAG (Retrieval-Augmented Generation)** pipeline:

1. User submits a compliance question.
2. The question is embedded using OpenAI embeddings.
3. ChromaDB retrieves the top 4 most relevant documents.
4. Retrieved documents are formatted as context.
5. A structured prompt instructs the LLM to:

   * Answer only using provided context
   * Refuse if the answer is not found
6. GPT generates the response.
7. Chat history is preserved during the session.

---

## 📦 Tech Stack

* **Frontend**: Streamlit
* **LLM**: OpenAI `gpt-4o-mini`
* **Embeddings**: `text-embedding-3-small`
* **Vector Database**: Chroma
* **Orchestration**: LangChain

---

## 📁 Project Structure

```
.
├── app.py
├── config.py
├── chroma_db/
└── README.md
```

* `app.py` → Main Streamlit application
* `config.py` → Contains `get_api_key()` function
* `chroma_db/` → Persisted Chroma vector store

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have one yet, typical dependencies:

```txt
streamlit
langchain
langchain-openai
langchain-chroma
chromadb
openai
```

---

## 🔐 API Key Configuration

Create a `config.py` file:

```python
import os

def get_api_key():
    return os.getenv("OPENAI_API_KEY")
```

Then export your key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 🧠 How the RAG Chain Works

```python
rag_chain = (
    {
        "context": itemgetter("question") | retriever | RunnableLambda(format_docs),
        "question": itemgetter("question"),
        "chat_history": itemgetter("chat_history"),
    }
    | prompt
    | llm
)
```

### Step Breakdown

* `retriever` → Retrieves top 4 relevant documents
* `format_docs` → Combines document contents
* `prompt` → Injects:

  * Chat history
  * Retrieved context
  * User question
* `llm` → Generates final answer

---

## 🛡 Hallucination Protection

The prompt explicitly forces the model to respond:

```
"I cannot find this information in the provided documents."
```

If the answer is not present in retrieved context.

This makes the system safer for compliance usage.

---

## 📌 Example Questions

* What encryption is required for customer PII?
* What is the retention period for audit logs?
* Who is responsible for approving access to confidential data?
* What is the incident response escalation timeline?

---

## 📊 Customization Options

You can modify:

| Component         | How                                          |
| ----------------- | -------------------------------------------- |
| Top-K retrieval   | Change `search_kwargs={"k": 4}`              |
| LLM model         | Replace `"gpt-4o-mini"`                      |
| Embedding model   | Replace `"text-embedding-3-small"`           |
| Prompt strictness | Modify template                              |
| Memory strategy   | Replace session memory with LangChain memory |

---

## 🔄 How to Add Documents

Before running the assistant, you must ingest documents into Chroma.

Example:

```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("policy.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = splitter.split_documents(docs)

db = Chroma.from_documents(
    splits,
    embedding=embedding,
    persist_directory="./chroma_db",
    collection_name="techcorp_docs"
)
db.persist()
```

---

## 🏢 Intended Use Case

Designed for:

* Internal compliance teams
* Security policy assistants
* Governance & risk management
* Enterprise document Q&A

---

## ⚠️ Important Notes

* This system only answers based on stored documents.
* It does not replace legal review.
* Accuracy depends on document quality and chunking strategy.

---
