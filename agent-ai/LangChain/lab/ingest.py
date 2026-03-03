from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config import get_api_key
import os

embedding = OpenAIEmbeddings(model="text-embedding-3-small", 
                             api_key=get_api_key())

docs = []
for file in os.listdir("data"):
    loader = TextLoader(f"data/{file}")
    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

db = Chroma(
    collection_name="techcorp_docs",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)

db.add_documents(chunks)

print("Data successfully indexed.")