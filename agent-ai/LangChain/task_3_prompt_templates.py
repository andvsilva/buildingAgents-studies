#!/usr/bin/env python3
"""
Task 3: Prompt Templates - Dynamic, Reusable Prompts
Show how ONE template can be reused with different variables.

Learning Goal: Master prompt templates for consistent, reusable prompts.
"""

# ============================================================
# Imports
# ============================================================

import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# ============================================================
# Environment
# ============================================================

load_dotenv(override=True)

# ============================================================
# Utilities
# ============================================================

def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return api_key

# ============================================================
# Main Execution
# ============================================================

def main():
    print("🎯 Task 3: Dynamic Prompt Templates")
    print("=" * 50)

    print("\n📝 Creating a Reusable Template")
    print("=" * 50)

    template = PromptTemplate(
        input_variables=["topic", "stype"],
        template="Explain {topic} in {style}"
    )

    # --------------------------------------------------------
    # Test with actual LLM
    # --------------------------------------------------------

    print("\n🤖 Testing Template with AI")
    print("=" * 50)

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=get_api_key,
        temperature=0.7
    )

    if template and llm:
        test_prompt = template.format(
            topic="artificial intelligence",
            style="exactly 5 words"
        )

        print(f"📝 Sending to AI: {test_prompt}")

        response = llm.invoke(test_prompt)
        print(f"\n🤖 AI Response: {response.content}")

    # --------------------------------------------------------
    # Benefits Summary
    # --------------------------------------------------------

    print("\n💡 Template Benefits:")
    print("  ✓ ONE template, INFINITE uses")
    print("  ✓ Variables make it dynamic")
    print("  ✓ Consistent structure across all prompts")
    print("  ✓ Change inputs, not code!")

    # --------------------------------------------------------
    # Completion Marker
    # --------------------------------------------------------

    os.makedirs("markers", exist_ok=True)
    with open("markers/task3_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 3 completed! One template, endless possibilities!")

# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    main()
