from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from tools import search_tool, wiki_tool, save_tool

# 2️⃣ Tools list
tools = [search_tool, wiki_tool, save_tool]

# 3️⃣ Prompt (new format)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI agent."),
    ("human", "{input}")
])

# 4️⃣ Create agent (NEW API)
agent = create_agent(
    model="gpt-4o-mini",
    tools=tools
)

# 5️⃣ Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# 6️⃣ Run
response = agent_executor.invoke({
    "input": "Search Python agents and save a summary"
})

print(response)
