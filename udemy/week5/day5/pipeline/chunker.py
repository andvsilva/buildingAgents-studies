from concurrent.futures import ThreadPoolExecutor
from litellm import completion
from pydantic import BaseModel
from config import MODEL
from logger import logger

class Chunk(BaseModel):
    headline: str
    summary: str
    original_text: str
    source: str
    doc_type: str

class Chunks(BaseModel):
    chunks: list[Chunk]

def process_document(document):
    prompt = f"Split into chunks with overlap:\n\n{document['text']}"

    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format=Chunks
    )

    raw_chunks = Chunks.model_validate_json(
        response.choices[0].message.content
    ).chunks

    enriched_chunks = []

    for chunk in raw_chunks:
        enriched_chunks.append(
            Chunk(
                headline=chunk.headline,
                summary=chunk.summary,
                original_text=chunk.original_text,
                source=document["source"],
                doc_type=document["type"]
            )
        )

    return enriched_chunks

def create_chunks(documents):
    chunks = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(process_document, documents)

    for result in results:
        chunks.extend(result)

    logger.info(f"Generated {len(chunks)} chunks")
    return chunks
