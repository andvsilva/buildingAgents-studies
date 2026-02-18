from litellm import completion
from pydantic import BaseModel
from config import MODEL

class RankOrder(BaseModel):
    order: list[int]

def rerank(question, chunks):
    prompt = f"Rank relevance to: {question}\n\n"

    for i, chunk in enumerate(chunks):
        preview = chunk[:400]
        prompt += f"ID {i+1}: {preview}\n\n"

    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format=RankOrder
    )

    order = RankOrder.model_validate_json(
        response.choices[0].message.content
    ).order

    return [chunks[i-1] for i in order]
