#!/usr/bin/env python3
"""
Task 5: Complete Chain - Combining Everything!
Build complete AI pipelines using LangChain's chain composition.

Learning Goal: Master chain composition with the pipe operator (|).
"""

# =========================
# Standard library imports
# =========================
import os

# =========================
# Third-party imports
# =========================
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    CommaSeparatedListOutputParser,
)

# =========================
# Environment setup
# =========================
load_dotenv(override=True)

MODEL_NAME = "gpt-4.1-mini"
TEMPERATURE = 0.3
MARKERS_DIR = "markers"


# =========================
# Utility functions
# =========================
def ensure_api_key() -> None:
    """Fail fast if the API key is missing."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY not set")

def create_markers_dir() -> None:
    os.makedirs(MARKERS_DIR, exist_ok=True)

# =========================
# Chain builders
# =========================
def build_analysis_chain(llm: ChatOpenAI):
    prompt = PromptTemplate(
        template=(
            "Analyze {technology} and provide pros and cons "
            "in 2-3 sentences."
        ),
        input_variables=["technology"],
    )
    return prompt | llm | StrOutputParser()


def build_list_chain(llm: ChatOpenAI):
    prompt = PromptTemplate(
        template="List 3 use cases for {technology} (comma-separated):",
        input_variables=["technology"],
    )
    return prompt | llm | CommaSeparatedListOutputParser()


# =========================
# Main execution
# =========================
def main() -> None:
    print("🎯 Task 5: Chain Composition with |")
    print("=" * 50)

    ensure_api_key()
    create_markers_dir()

    # Initialize LLM once (reads API key from env)
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
    )

    # -------------------------
    # Chain 1: Analysis
    # -------------------------
    print("\n⛓️ Chain 1: Simple Analysis")
    print("=" * 50)

    analysis_chain = build_analysis_chain(llm)

    analysis_result = analysis_chain.invoke(
        {"technology": "blockchain"}
    )

    print("📝 Input: Analyze blockchain")
    print(f"✅ Output: {analysis_result}")

    # -------------------------
    # Chain 2: List generation
    # -------------------------
    print("\n⛓️ Chain 2: List Generation with Parser")
    print("=" * 50)

    list_chain = build_list_chain(llm)

    list_result = list_chain.invoke(
        {"technology": "blockchain"}
    )

    print("📝 Input: List use cases for blockchain")
    print(f"✅ Output: {list_result}")
    print(f"✅ Type: {type(list_result)} — Python list!")

    # -------------------------
    # Full pipeline demo
    # -------------------------
    print("\n🎉 Complete Pipeline Example")
    print("=" * 50)

    test_tech = "artificial intelligence"
    print(f"Technology: {test_tech}\n")

    analysis = analysis_chain.invoke({"technology": test_tech})
    use_cases = list_chain.invoke({"technology": test_tech})

    print("1️⃣ Analysis:")
    print(f"   {analysis}")

    print("\n2️⃣ Use Cases:")
    for i, use_case in enumerate(use_cases, start=1):
        print(f"   {i}. {use_case}")

    # -------------------------
    # Final notes
    # -------------------------
    print("\n💡 Chain Composition Magic:")
    print("  ✓ The | operator connects everything")
    print("  ✓ prompt | llm | parser = complete pipeline")
    print("  ✓ Different parsers = different output formats")
    print("  ✓ Same LLM, infinite possibilities!")

    with open(os.path.join(MARKERS_DIR, "task5_complete.txt"), "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 5 completed! You've mastered LangChain chains!")
    print("🏆 You can now build AI pipelines with confidence!")


if __name__ == "__main__":
    main()
