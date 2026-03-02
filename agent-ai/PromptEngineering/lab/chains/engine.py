from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from config import get_api_key

def run_prompt(prompt_text: str, temperature: float = 0):

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        api_key=get_api_key()
    )

    prompt = PromptTemplate.from_template("{input}")

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"input": prompt_text})