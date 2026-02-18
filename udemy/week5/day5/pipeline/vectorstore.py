from chromadb import PersistentClient
from config import DB_PATH
from logger import logger

client = PersistentClient(path=DB_PATH)

def get_collection(name="docs"):
    return client.get_or_create_collection(name)

def add_embeddings(collection, ids, vectors, texts, metas):
    collection.add(
        ids=ids,
        embeddings=vectors,
        documents=texts,
        metadatas=metas
    )

    logger.info(f"Collection size: {collection.count()}")
