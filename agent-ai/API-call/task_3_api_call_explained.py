#!/usr/bin/env python3
"""
Task 3: Making Your First API Call
Understand EVERY part of the OpenAI Responses API.
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
import snoop

@snoop
def main():
    load_dotenv(override=True)

    client = OpenAI()

    # ==========================================
    # UNDERSTANDING THE API CALL STRUCTURE
    # ==========================================
    #
    # To make an API call, you MUST provide:
    # 1. model - Which AI model to use (required)
    # 2. input - What you want the AI to respond to (required)
    #
    # The input can be:
    # - A simple string (most common)
    # - A structured object (advanced use cases)
    # ==========================================

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Hello AI, please introduce yourself" # prompt to the LLM.
    )

    # ==========================================
    # REAL RESPONSE OBJECT STRUCTURE (SIMPLIFIED)
    # ==========================================
    #
    # response
    # ├── id
    # ├── model
    # ├── output_text        ← Shortcut to the AI text
    # ├── output[]           ← Full structured output
    # └── usage
    #     ├── input_tokens
    #     ├── output_tokens
    #     └── total_tokens
    # ==========================================

    try:
        if response:
            ai_text = response.output_text

            print("✅ API Call Successful!")
            print(f"\n🤖 AI said:\n{ai_text}")
            print(f"\n📊 Total tokens used: {response.usage.total_tokens}")

            # Create marker
            os.makedirs("markers", exist_ok=True)
            with open("markers/task3_api_call_complete.txt", "w") as f:
                f.write("SUCCESS")
        else:
            print("❌ API call did not return a response")

    except Exception as e:
        print("❌ Error while making API call")
        print(str(e))

if __name__ == "__main__":
    main()