#!/usr/bin/env python3

"""
Create a Vector Database from PDFs and query it.
"""

import os
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import logging

logging.set_verbosity_error()

PDF_FOLDER = "books"
VECTOR_DB_DIR = "vector_db"


# -------------------------
# Load PDFs
# -------------------------
def load_pdfs(folder):

    documents = []

    for file in sorted(os.listdir(folder)):

        if not file.endswith(".pdf"):
            continue

        path = os.path.join(folder, file)

        print(f"Loading {file}")

        try:

            loader = PyPDFLoader(path)
            docs = loader.load()

            for d in docs:
                d.metadata["source"] = file

            documents.extend(docs)

        except Exception as e:

            print(f"⚠️ Failed loading {file}: {e}")

    return documents


# -------------------------
# Split Documents
# -------------------------
def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    clean_chunks = []

    for c in chunks:

        text = c.page_content

        if text is None:
            continue

        text = str(text).strip()

        if len(text) < 20:
            continue

        c.page_content = text
        clean_chunks.append(c)

    print(f"Valid chunks: {len(clean_chunks)}")

    return clean_chunks


# -------------------------
# Embedding Model
# -------------------------
def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return embeddings


# -------------------------
# Create Vector DB
# -------------------------
def create_vector_db(chunks, embeddings):

    valid_chunks = [
        c for c in chunks
        if isinstance(c.page_content, str) and len(c.page_content.strip()) > 10
    ]

    print(f"Embedding {len(valid_chunks)} chunks")

    db = Chroma.from_documents(
        documents=valid_chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_DIR
    )

    return db


# -------------------------
# Load Existing DB
# -------------------------
def load_vector_db(embeddings):

    db = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )

    return db


# -------------------------
# Query Interface
# -------------------------
def ask_question(db):

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        results = db.similarity_search(question, k=3)

        print("\nTop Results:\n")

        for i, doc in enumerate(results):

            source = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "?")

            print("=" * 60)
            print(f"Result {i+1}")
            print(f"Source: {source} | Page: {page}")
            print(doc.page_content[:800])
            print()


# -------------------------
# Main
# -------------------------
def main():

    print("\nLoading embedding model...\n")

    embeddings = create_embeddings()

    if Path(VECTOR_DB_DIR).exists():

        print("Vector DB already exists. Loading...")

        db = load_vector_db(embeddings)

    else:

        print("\nLoading PDFs...\n")

        documents = load_pdfs(PDF_FOLDER)

        print(f"Loaded {len(documents)} pages")

        print("\nSplitting documents...\n")

        chunks = split_documents(documents)

        print(f"Created {len(chunks)} chunks")

        print("\nCreating vector database...\n")

        db = create_vector_db(chunks, embeddings)

        print("\nVector database created!")

    ask_question(db)


if __name__ == "__main__":
    main()