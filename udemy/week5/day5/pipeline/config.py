import os
from pathlib import Path

MODEL = "gpt-4.1-nano"
EMBEDDING_MODEL = "text-embedding-3-small"

BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "vector_db")

KNOWLEDGE_BASE_PATH = Path("../../knowledge-base")

AVERAGE_CHUNK_SIZE = 500
RETRIEVAL_K = 15
RERANK_TOP_K = 8
BATCH_SIZE = 100