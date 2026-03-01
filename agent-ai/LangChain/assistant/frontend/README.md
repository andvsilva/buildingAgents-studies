# A Streamlit frontend that searches directly in the vector database (RAG only, no API yet).

We’ll use:

- Streamlit for frontend
- Chroma as vector DB
- LangChain retriever
- OpenAI embeddings

🎯 Goal (Phase 1)

- User types a question →
- Streamlit queries Chroma →
- Retriever returns relevant policy chunks →
- LLM generates final answer →
- Streamlit displays response