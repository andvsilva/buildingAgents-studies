def cot_prompt(question: str) -> str:
    return f"""
You are a financial reasoning assistant.

Solve the problem step by step.

Question:
{question}

Let's think step by step.
"""