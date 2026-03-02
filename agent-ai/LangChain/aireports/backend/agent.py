from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return api_key

# -------- DATABASE --------
DATABASE_URL = "sqlite:///data/finance.db"
engine = create_engine(DATABASE_URL)

db = SQLDatabase(engine)

# -------- LLM --------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=get_api_key(),
    temperature=0
)

# -------- SQL AGENT --------
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

# -------- TEST --------
question = "Which investment has the highest annual return?"

response = agent.invoke({"input": question})

print("\nFinal Answer:")
print(response["output"])