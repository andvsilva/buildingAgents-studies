# app/services/agent_service.py

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from app.core.config import settings


def ask_agent(question: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY
    )

    tools = [
        Tool(
            name="Basic QA",
            func=lambda q: "This is a placeholder answer.",
            description="Simple question answering tool"
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )

    response = agent.run(question)

    return response