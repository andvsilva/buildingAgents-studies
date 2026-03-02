def few_shot_prompt(question: str) -> str:
    return f"""
You are a financial AI assistant.

Example 1:
Q: What is ROI?
A: ROI means Return on Investment. It measures profitability.

Example 2:
Q: What is EBITDA?
A: EBITDA measures operational performance before interest, taxes, depreciation and amortization.

Now answer:

Q: {question}
A:
"""