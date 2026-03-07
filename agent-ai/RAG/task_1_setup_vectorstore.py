#!/usr/bin/env python3
"""
Task 1: Environment & Vector Store Setup
Bridge your Vector Databases Lab knowledge to create the foundation for RAG
"""

import os
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import logging

logging.set_verbosity_error()

print("🔧 Task 1: Setting up Vector Store for RAG")
print("=" * 50)

# Initialize ChromaDB client for persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

print("✅ ChromaDB client initialized")

# Create or get collection named "techcorp_rag"
collection = client.get_or_create_collection(name="techcorp_rag")

print(f"✅ Collection '{collection.name}' ready")

# Initialize embedding model for 384-dimension vectors
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

print("✅ Embedding model loaded")

# Test the setup
test_text = "Testing RAG setup"
test_embedding = model.encode(test_text)
print(f"✅ Test embedding created: {len(test_embedding)} dimensions")

# Verify everything works
print("\n" + "=" * 50)
print("🎉 SUCCESS! Your vector store is ready for RAG!")
print(f"   - ChromaDB initialized")
print(f"   - Collection: {collection.name}")
print(f"   - Embedding model: all-MiniLM-L6-v2")
print(f"   - Vector dimensions: {len(test_embedding)}")
print("=" * 50)

# Create marker file
os.makedirs("markers", exist_ok=True)
with open("markers/task1_setup_complete.txt", "w") as f:
    f.write("TASK1_COMPLETE")

print("\n💡 Remember: You learned this in Vector Databases Lab - now applying it for RAG!")
print("\n✅ Task 1 completed!")