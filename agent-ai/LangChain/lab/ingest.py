from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config import get_api_key
from tqdm import tqdm
import os
import shutil

DATA_DIR = "data"
PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "techcorp_docs"

# ---------- Optional: Reset DB ----------
# Uncomment if you want a fresh database each run
# if os.path.exists(PERSIST_DIR):
#     shutil.rmtree(PERSIST_DIR)

# ---------- Embeddings ----------
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=get_api_key()
)

# ---------- Load Documents ----------
docs = []
files = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]

print(f"📂 Loading {len(files)} files...")

for file in tqdm(files, desc="Loading files"):
    file_path = os.path.join(DATA_DIR, file)
    loader = TextLoader(file_path, encoding="utf-8")
    docs.extend(loader.load())

print(f"✅ Loaded {len(docs)} documents.")

# ---------- Split Documents ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"✂️ Created {len(chunks)} chunks.")

# ---------- Create / Load Vector DB ----------
db = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embedding,
    persist_directory=PERSIST_DIR
)

# ---------- Index with Progress Bar ----------
print("📥 Indexing chunks...")

for chunk in tqdm(chunks, desc="Embedding + Storing"):
    db.add_documents([chunk])   # add one at a time to visualize progress

print("✅ Data successfully indexed and persisted.")