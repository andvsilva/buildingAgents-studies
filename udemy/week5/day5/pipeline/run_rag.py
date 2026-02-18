import os
import time
import argparse

from loader import load_documents
from chunker import create_chunks
from embedder import embed_texts
from vectorstore import get_collection, add_embeddings
from retriever import HybridRetriever
from reranker import rerank
from generator import generate_answer
from config import RETRIEVAL_K
from logger import logger


# =========================
# BUILD PIPELINE
# =========================

def build_vectorstore(force_rebuild=False):

    collection = get_collection()

    if collection.count() > 0 and not force_rebuild:
        logger.info("Vectorstore already exists. Skipping rebuild.")
        return collection

    logger.info("Building vectorstore...")

    documents = load_documents()
    chunks = create_chunks(documents)

    texts = [c.original_text for c in chunks]
    metas = [
        {"source": c.source, "type": c.doc_type}
        for c in chunks
    ]

    vectors = embed_texts(texts)

    ids = [str(i) for i in range(len(texts))]

    add_embeddings(collection, ids, vectors, texts, metas)

    logger.info("Vectorstore built successfully.")
    return collection


# =========================
# RAG PIPELINE
# =========================

def rag_answer(question, collection):

    start_time = time.time()

    retriever = HybridRetriever(collection, collection.get()["documents"])

    retrieved = retriever.retrieve(question)

    reranked = rerank(question, retrieved)

    context = "\n\n".join(reranked[:5])

    answer = generate_answer(question, context)

    elapsed = time.time() - start_time

    print("\n" + "="*60)
    print("QUESTION:")
    print(question)
    print("\nANSWER:")
    print(answer)
    print("\nTime:", round(elapsed, 2), "seconds")
    print("="*60 + "\n")

    return answer


# =========================
# CLI
# =========================

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true",
                        help="Force rebuild of vectorstore")
    parser.add_argument("--question", type=str,
                        help="Ask a single question and exit")
    args = parser.parse_args()

    collection = build_vectorstore(force_rebuild=args.rebuild)

    # Single question mode
    if args.question:
        rag_answer(args.question, collection)
        return

    # Interactive mode
    print("\n🚀 RAG System Ready (type 'exit' to quit)\n")

    while True:
        question = input("Ask: ")

        if question.lower() in ["exit", "quit"]:
            break

        rag_answer(question, collection)


if __name__ == "__main__":
    main()
