from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine

from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType

import os

# --- CONFIG ---
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/finance_db"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- FastAPI ---
app = FastAPI()

class Question(BaseModel):
    question: str

# --- Database ---
engine = create_engine(DATABASE_URL)
db = SQLDatabase(engine)

# --- LLM ---
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini"
)

# --- SQL Agent ---
agent = create_sql_agent(
    llm=llm,
    db=db,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

@app.post("/ask")
def ask_question(payload: Question):

    result = agent.run(payload.question)

    return {"answer": result}