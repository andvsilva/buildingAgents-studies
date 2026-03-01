#!/usr/bin/env python3
"""
Task 1: OpenAI SDK vs LangChain - See the Difference!
Compare the complexity of raw OpenAI SDK with LangChain's clean abstraction.

Learning Goal: Understand why LangChain simplifies AI development.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI

# -------------------------------------------------------------------
# 🔴 RAW OPENAI SDK APPROACH (Modern Responses API)
# -------------------------------------------------------------------
def raw_openai_approach():
    """Raw OpenAI SDK - explicit and verbose"""
    print("\n🔴 RAW OPENAI SDK APPROACH")

    load_dotenv(override=True)

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE")  # optional
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain machine learning in one sentence." # prompt to the LLM
    )

    if response and response.output_text:
        text = response.output_text
        print(f"Response: {text[:-1]}...")
        return text

    print("No response from OpenAI SDK.")
    return None


# -------------------------------------------------------------------
# 🟢 LANGCHAIN APPROACH (Clean abstraction)
# -------------------------------------------------------------------
def langchain_approach():
    """LangChain - clean and simple"""
    print("\n🟢 LANGCHAIN APPROACH")

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_BASE"),  # optional
        temperature=0.2
    )

    response = llm.invoke("Explain machine learning in one sentence.")

    if response:
        print(f"Response: {response.content[:-1]}...")
        return response.content

    print("No response from LangChain.")
    return None

# -------------------------------------------------------------------
# 🚀 MAIN
# -------------------------------------------------------------------
def main():
    print("🎯 Task 1: OpenAI SDK vs LangChain Comparison")
    print("=" * 50)

    raw_result = raw_openai_approach()
    langchain_result = langchain_approach()

    if raw_result and langchain_result:
        print("\n📊 COMPARISON RESULT")
        print("✅ Both approaches work!")
        print("LangChain advantages:")
        print("  • Less boilerplate code")
        print("  • Cleaner response handling")
        print("  • Easier configuration")
        print("  • Provider-agnostic design")

        # Marker file
        os.makedirs("markers", exist_ok=True)
        with open("markers/task1_complete.txt", "w") as f:
            f.write("COMPLETED")

        print("\n✅ Task 1 completed successfully!")


if __name__ == "__main__":
    main()
