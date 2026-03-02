def zero_shot(question: str) -> str:
    return f"""
You are a financial AI assistant.

Answer clearly and objectively.

Question:
{question}
"""

def few_shot(question: str) -> str:
    return f"""
You are a financial AI assistant.

Example:
Q: What is ROI?
A: ROI measures return on investment.

Now answer:

Q: {question}
A:
"""

def cot(question: str) -> str:
    return f"""
You are a reasoning assistant.

Solve step by step.

Question:
{question}

Let's think step by step.
"""

def tot(question: str) -> str:
    return f"""
You are an advanced reasoning AI.

Generate 3 solution approaches.
Compare them.
Select the best one.

Question:
{question}
"""