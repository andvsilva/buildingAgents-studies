#!/usr/bin/env python3
"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
(Updated for the Responses API)
"""

from openai import OpenAI
import os
from dotenv import load_dotenv
import snoop

@snoop
def main():
    load_dotenv(override=True)

    client = OpenAI()

    # Make a simple API call
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="What is Python in one sentence?"
    )

    # ==========================================
    # THE MAGIC PATH TO THE AI'S ANSWER (MODERN)
    # ==========================================
    #
    # The easiest and recommended way:
    #
    #   response.output_text
    #
    # Under the hood, the full structure is:
    #
    # response
    # └── output
    #     └── [0]
    #         └── content
    #             └── [0]
    #                 └── text   ← AI's actual answer
    #
    # ==========================================

    # Golden path (simple and safe)
    ai_text = response.output_text

    # Display what we extracted
    print("🎯 Successfully extracted the AI's response!")
    print("\n" + "=" * 60)
    print("Question: What is Python in one sentence?")
    print("\nAI's Answer:")
    print(ai_text)
    print("=" * 60)

    # Show the new golden path
    print("\n🔑 THE GOLDEN PATH (MODERN API):")
    print("   response.output_text")

    # Create marker for completion tracking
    os.makedirs("markers", exist_ok=True)
    with open("markers/task4_extract_complete.txt", "w") as f:
        f.write("SUCCESS")

    print("\n✅ Task 4 completed! You now know how to extract AI responses!")

if __name__ == "__main__":
    main()