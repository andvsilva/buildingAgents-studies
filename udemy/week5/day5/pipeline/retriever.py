from rank_bm25 import BM25Okapi
import numpy as np
from embedder import embed_texts
from config import RETRIEVAL_K
from logger import logger

class HybridRetriever:

    def __init__(self, collection, documents):
        self.collection = collection
        self.documents = documents
        self.bm25 = BM25Okapi([doc.split() for doc in documents])

    def retrieve(self, query):
        query_embedding = embed_texts([query])[0]

        vector_results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=RETRIEVAL_K
        )

        vector_docs = vector_results["documents"][0]

        bm25_scores = self.bm25.get_scores(query.split())
        bm25_top = np.argsort(bm25_scores)[-RETRIEVAL_K:]

        hybrid_docs = list(set(vector_docs + [self.documents[i] for i in bm25_top]))

        logger.info("Hybrid retrieval completed")
        return hybrid_docs
