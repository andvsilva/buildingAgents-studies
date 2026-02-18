from config import KNOWLEDGE_BASE_PATH
from logger import logger

def load_documents():
    documents = []

    for folder in KNOWLEDGE_BASE_PATH.iterdir():
        doc_type = folder.name
        for file in folder.rglob("*.md"):
            with open(file, "r", encoding="utf-8") as f:
                documents.append({
                    "type": doc_type,
                    "source": file.as_posix(),
                    "text": f.read()
                })

    logger.info(f"Loaded {len(documents)} documents")
    return documents