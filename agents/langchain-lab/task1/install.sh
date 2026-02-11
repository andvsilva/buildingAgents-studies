python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip uv

# Core LangChain packages
uv pip install langchain langchain-community langchain-core langchain-text-splitters langchain-huggingface

# LLM Providers
uv pip install langchain-openai langchain-anthropic langchain-google-genai

# Vector store and embeddings
uv pip install faiss-cpu sentence-transformers

# UI and utilities
uv pip install python-dotenv gradio

echo "LANGCHAIN_INSTALLED" > /root/langchain-ready.txt