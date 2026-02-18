from litellm import completion
from config import MODEL

def generate_answer(question, context):
    prompt = f"""
Answer the question based only on this context:

{context}

Question: {question}
"""

    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
