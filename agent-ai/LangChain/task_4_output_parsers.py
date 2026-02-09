#!/usr/bin/env python3
"""
Task 4: Output Parsers - From Text to Structured Data
Transform AI responses into structured formats your application can use.

Learning Goal: Extract structured data from unstructured AI responses.
"""

# ============================================================
# Imports
# ============================================================

import os
import json

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    CommaSeparatedListOutputParser,
)


# ============================================================
# Main Execution
# ============================================================

def main():
    # --------------------------------------------------------
    # Environment
    # --------------------------------------------------------

    load_dotenv(override=True)

    def get_api_key() -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set")
        return api_key

    print("🎯 Task 4: Output Parsers - Text to Data")
    print("=" * 50)

    # --------------------------------------------------------
    # LLM Initialization
    # --------------------------------------------------------

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=get_api_key,
        temperature=0
    )

    # ========================================================
    # Example 1: List Output Parser
    # ========================================================

    print("\n📋 List Output Parser")
    print("=" * 50)

    list_parser = CommaSeparatedListOutputParser()

    list_prompt = PromptTemplate(
        template="List 3 benefits of {technology} (comma-separated):",
        input_variables=["technology"]
    )

    list_chain = list_prompt | llm | list_parser

    if list_chain:
        result = list_chain.invoke({
            "technology": "cloud computing"
        })

        print("✅ Input: 'List 3 benefits of cloud computing'")
        print(f"✅ Parsed Output: {result}")
        print(f"✅ Type: {type(result)} - It's a Python list!")
        print(f"✅ Access items: result[0] = '{result[0] if result else ''}'")

    # ========================================================
    # Example 2: JSON Output Parser
    # ========================================================

    print("\n📦 JSON Output Parser")
    print("=" * 50)

    json_parser = JsonOutputParser()

    json_prompt = PromptTemplate(
        template="""Analyze {technology} and respond with JSON containing:
        - benefits: array of 2 benefits
        - complexity: low/medium/high
        - use_case: one main use case

        Technology: {technology}

        {format_instructions}""",
        input_variables=["technology"],
        partial_variables={
            "format_instructions": json_parser.get_format_instructions()
        }
    )

    json_chain = json_prompt | llm | json_parser

    if json_chain:
        result = json_chain.invoke({
            "technology": "machine learning"
        })

        print("✅ Input: 'Analyze machine learning'")

        try:
            parsed = result

            print("✅ Parsed JSON Output:")
            print(f"   Benefits: {parsed.get('benefits', [])}")
            print(f"   Complexity: {parsed.get('complexity', 'N/A')}")
            print(f"   Use Case: {parsed.get('use_case', 'N/A')}")
            print(f"✅ Type: {type(parsed)} - It's a Python dict!")
        except (json.JSONDecodeError, TypeError, AttributeError):
            print(f"⚠️ Parsing failed (rare with JsonOutputParser): {result}")

    # ========================================================
    # Summary
    # ========================================================

    print("\n💡 Parser Magic:")
    print("  ✓ List parser: Text → Python list")
    print("  ✓ JSON parser: Text → Python dict")
    print("  ✓ Direct data access: result[0], parsed['benefits']")
    print("  ✓ Ready for your application!")

    # --------------------------------------------------------
    # Completion Marker
    # --------------------------------------------------------

    os.makedirs("markers", exist_ok=True)
    with open("markers/task4_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 4 completed! You can now parse AI outputs into data structures!")


# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    main()
