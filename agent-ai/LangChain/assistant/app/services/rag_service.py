from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.tools import tool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

EMBEDDINGS = OpenAIEmbeddings()

VECTOR_PATH = "data/vectorstore"

def build_vectorstore():
    if os.path.exists(VECTOR_PATH):
        return FAISS.load_local(VECTOR_PATH, EMBEDDINGS)

    loader = TextLoader("data/documents/*.txt")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(splits, EMBEDDINGS)
    vectorstore.save_local(VECTOR_PATH)

    return vectorstore


vectorstore = build_vectorstore()
retriever = vectorstore.as_retriever()


@tool
def search_company_docs(question: str) -> str:
    """
    Use this tool for questions about company documents:
    policies, strategy, FAQ, manuals.
    """
    docs = retriever.get_relevant_documents(question)
    return "\n\n".join([doc.page_content for doc in docs])