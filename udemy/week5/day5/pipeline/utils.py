import hashlib

def text_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

def batch(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
