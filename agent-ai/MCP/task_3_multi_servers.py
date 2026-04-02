#!/usr/bin/env python3
"""Task 3: Multiple MCP Servers - Orchestrating calculator and weather servers"""

import os
import asyncio
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from config import get_api_key

print("🌐 Task 3: Multiple MCP Servers\n")

# =========================
# LLM CONFIG
# =========================
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    api_key=get_api_key(),
    temperature=0
)

print("Configuring multiple MCP servers:\n")

# =========================
# MCP SERVERS CONFIG
# =========================
client = MultiServerMCPClient(
    {
        "calculator": {
            "command": "python",
            "args": ["mcp_servers/calculator_server.py"],
            "transport": "stdio",
        },
        "weather": {
            "command": "python",
            "args": ["mcp_servers/weather_server.py"],
            "transport": "stdio",
        }
    }
)


# =========================
# MAIN AGENT FUNCTION
# =========================
async def run_multi_server_agent():
    """Create and run agent with multiple MCP servers"""

    print("📦 Loading tools from multiple servers...")

    try:
        tools = await client.get_tools()
    except Exception as e:
        print(f"❌ Error loading tools: {e}")
        return

    print(f"✅ Loaded {len(tools)} tools from MCP servers")

    # Create agent
    agent = create_agent(model=model, tools=tools)

    print("\n" + "=" * 60)
    print("TESTING MULTI-SERVER ORCHESTRATION:")
    print("=" * 60)

    # Helper to run tests safely
    async def run_test(title, query):
        print(f"\n{title}")
        try:
            response = await agent.ainvoke({
                "messages": [{"role": "user", "content": query}]
            })
            print(f"Response: {response['messages'][-1].content}")
        except Exception as e:
            print(f"❌ Error: {e}")

    # =========================
    # TESTS
    # =========================

    await run_test("Test 1: Calculator MCP", "What is 42 plus 58?")
    await run_test("Test 2: Weather MCP", "What's the weather in London?")
    await run_test("Test 3: Complex Math", "What's (3 + 5) * 12?")
    await run_test("Test 4: Weather Comparison", "Compare the weather in New York and Tokyo")
    await run_test("Test 5: Mixed Query", "If it's 20°C in Paris and temperature rises by 5 degrees, what will it be?")


# =========================
# ENTRYPOINT
# =========================
if __name__ == "__main__":
    print("Starting Multi-Server MCP Orchestration...")
    print("This demonstrates how a single agent can use multiple MCP servers\n")

    try:
        asyncio.run(run_multi_server_agent())
    except KeyboardInterrupt:
        print("\n🛑 Execution stopped by user")

    print("\n" + "=" * 60)
    print("💡 KEY CONCEPTS:")
    print("- MultiServerMCPClient manages multiple MCP servers")
    print("- Each server exposes different tools")
    print("- Agent automatically selects appropriate tools")
    print("- Seamless orchestration across servers")
    print("- Extensible to many servers and domains")
    print("=" * 60)

    # Marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task3_multi_servers_complete.txt", "w") as f:
        f.write("TASK3_COMPLETE")