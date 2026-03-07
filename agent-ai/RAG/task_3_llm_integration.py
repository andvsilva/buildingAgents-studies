#!/usr/bin/env python3
"""
Task 3: LLM Integration
Configure the AI generation engine using pre-configured OpenAI API
"""

import os
from langchain_openai import ChatOpenAI
from config import get_api_key

# Test the LLM with a simple generation
def test_generation():
    """Test basic LLM generation"""

    print("🤖 Task 3: LLM Integration")
    print("=" * 50)

    print("✅ OpenAI client initialized")

    # Initialize LangChain ChatOpenAI client
    client = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=get_api_key()
    )

    # Set temperature for focused answers
    temperature = 0.3

    # Set max tokens for concise responses
    max_tokens = 500

    # Update client with temperature and max_tokens
    client.temperature = temperature
    client.max_tokens = max_tokens

    print(f"\n📝 Testing gpt-4.1-mini with temperature={temperature}")

    # Create messages for the query
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "What is RAG in AI? Answer in one sentence."}
    ]

    # Generate response using invoke method
    response = client.invoke(messages)
    answer = response.content

    print(f"\n🤖 Test Response: {answer}")

    return True

# Run the test
try:
    success = test_generation()

    print("\n" + "=" * 50)
    print("🎉 LLM Integration Successful!")
    print("   - Model: openai/gpt-4.1-mini")
    print("   - Temperature: 0.3 (focused)")
    print("   - Max tokens: 500 (concise)")
    print("   - LangChain integration ready for RAG!")
    print("=" * 50)

    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task3_llm_complete.txt", "w") as f:
        f.write("TASK3_COMPLETE:LLM_READY")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\n💡 Check that OPENAI_API_BASE and OPENAI_API_KEY are set!")

print("\n💡 LLM ready to generate answers from retrieved context!")
print("\n✅ Task 3 completed!")