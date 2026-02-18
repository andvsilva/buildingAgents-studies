def evaluate(retrieved, ground_truth):
    hits = sum(1 for doc in retrieved if ground_truth in doc)
    return hits / len(retrieved)
