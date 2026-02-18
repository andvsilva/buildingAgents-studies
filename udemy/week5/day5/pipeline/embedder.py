from openai import OpenAI
from config import EMBEDDING_MODEL, BATCH_SIZE
from utils import batch
from logger import logger
import shelve

client = OpenAI()

def embed_texts(texts):
    vectors = []

    with shelve.open("embedding_cache") as cache:
        for batch_texts in batch(texts, BATCH_SIZE):
            batch_vectors = []

            to_embed = []
            indices = []

            for i, text in enumerate(batch_texts):
                if text in cache:
                    batch_vectors.append(cache[text])
                else:
                    to_embed.append(text)
                    indices.append(i)
                    batch_vectors.append(None)

            if to_embed:
                response = client.embeddings.create(
                    model=EMBEDDING_MODEL,
                    input=to_embed
                )
                new_vectors = [e.embedding for e in response.data]

                for idx, vec in zip(indices, new_vectors):
                    batch_vectors[idx] = vec
                    cache[batch_texts[idx]] = vec

            vectors.extend(batch_vectors)

    logger.info("Embeddings generated")
    return vectors
