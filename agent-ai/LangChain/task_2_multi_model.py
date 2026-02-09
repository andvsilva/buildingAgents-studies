#!/usr/bin/env python3
"""
Task 2: Multi-Model Support - One Interface, Many Providers!
Test multiple OpenAI models using the same LangChain interface,
with logical provider aliases (OpenAI, Google-style, XAI-style).

Learning Goal: Provider flexibility without changing code structure.
"""

# ============================================================
# Imports
# ============================================================

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr


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
# Model Registry
# ============================================================

# Logical provider → real OpenAI model
MODEL_REGISTRY = {
    "openai": "gpt-4o",
    "google": "gpt-4o-mini",   # fast / cheap (Google-style)
    "xai": "gpt-4o",           # stronger reasoning (XAI-style)
}


def create_llm(provider: str, temperature: float = 0.2) -> ChatOpenAI:
    model = MODEL_REGISTRY.get(provider)
    if not model:
        raise ValueError(f"Provider '{provider}' not registered")

    return ChatOpenAI(
        model=model,
        temperature=temperature,
        api_key=get_api_key
    )


# ============================================================
# Main Execution
# ============================================================

def main():
    print("🎯 Task 2: Multi-Model Support with LangChain")
    print("=" * 50)

    load_dotenv(override=True)

    print("\n🌐 Initializing logical providers (OpenAI backend only)")
    print("=" * 50)

    openai_llm = create_llm("openai")
    google_llm = create_llm("google")
    xai_llm = create_llm("xai")

    print("✅ All models initialized!")

    print("\n🧪 Model Comparison - Same Prompt, Different Models")
    print("=" * 50)

    test_prompt = "Explain cloud computing in one sentence."
    print(f"📝 Prompt: '{test_prompt}'\n")

    for name, llm in [
        ("OpenAI", openai_llm),
        ("Google-style", google_llm),
        ("XAI-style", xai_llm),
    ]:
        response = llm.invoke(test_prompt)
        print(f"{name}: {response.content}")
        print("*" * 50)

    print("\n💡 Same interface, different model behavior — perfect for A/B testing!")

    # Marker for completion
    os.makedirs("markers", exist_ok=True)
    with open("markers/task2_complete.txt", "w") as f:
        f.write("COMPLETED")

    print("\n✅ Task 2 completed!")
    print("🎉 Multi-model architecture working correctly!")


# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    main()
