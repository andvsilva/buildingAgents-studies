def tot_prompt(question: str) -> str:
    return f"""
You are an advanced reasoning AI.

Generate 3 different solution approaches.
Evaluate them.
Select the best one.

Question:
{question}
"""