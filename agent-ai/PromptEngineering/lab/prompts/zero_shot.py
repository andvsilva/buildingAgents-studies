from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def zero_shot_prompt(question: str) -> str:
    return f"""
You are a financial AI assistant.

Answer the question clearly and concisely.

Question:
{question}

Answer:
"""

def run_zero_shot(question: str):

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = PromptTemplate.from_template(zero_shot_prompt("{question}"))

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"question": question})