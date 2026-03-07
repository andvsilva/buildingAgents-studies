#!/usr/bin/env python3
"""
Task 4: Prompt Engineering
Build the RAG prompt template that ensures accurate, context-based answers
"""

import os
from langchain_openai import ChatOpenAI
from config import get_api_key

print("📝 Task 4: Prompt Engineering")
print("=" * 50)

# Initialize LangChain ChatOpenAI client
client = ChatOpenAI(
    api_key=get_api_key(),
    model="gpt-4.1-mini",
    temperature=0.3,
    max_tokens=200
)

print("✅ OpenAI client ready")

def create_rag_prompt(context_chunks, user_question):
    """Create the RAG prompt with context and question"""

    # Complete the system prompt for context-based answers
    system_prompt = """You are TechCorp's helpful AI assistant.
Answer ___ based on the provided context.
If the answer is not in the context, say: 'I don't have that information in the provided documents.'
Be concise and accurate."""  # Replace ___ with "ONLY"

    # Build context section from retrieved chunks
    context_text = "Context from TechCorp documents:\n\n"
    for i, chunk in enumerate(context_chunks, 1):
        context_text += f"[Document {i}]\n{chunk}\n\n"

    # Create the user prompt with context and question
    user_prompt = f"""
{context_text}

Question: {user_question}

Answer:"""

    return system_prompt, user_prompt

# Test the prompt template
def test_prompt_engineering():
    """Test the prompt template with sample data"""

    # Sample retrieved chunks
    test_chunks = [
        "TechCorp allows employees to work remotely up to 3 days per week. Core hours are 10 AM to 3 PM.",
        "Remote work arrangements must be approved by your manager and documented with HR.",
        "VPN is mandatory when accessing company resources from home."
    ]

    test_question = "How many days can I work from home?"

    system_prompt, user_prompt = create_rag_prompt(test_chunks, test_question)

    print("📋 System Prompt:")
    print("-" * 40)
    print(system_prompt)

    print("\n📋 User Prompt (with context):")
    print("-" * 40)
    print(user_prompt[:500] + "..." if len(user_prompt) > 500 else user_prompt)

    # Test with LangChain ChatOpenAI
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.invoke(messages)
    answer = response.content
    print("\n🤖 Generated Answer:")
    print("-" * 40)
    print(answer)

    return True

# Run the test
try:
    success = test_prompt_engineering()

    print("\n" + "=" * 50)
    print("🎉 Prompt Engineering Complete!")
    print("   - System prompt: Context-aware")
    print("   - User prompt: Structured with context")
    print("   - Answer: Based on provided documents")
    print("   - Ready for complete RAG pipeline!")
    print("=" * 50)

    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task4_prompt_complete.txt", "w") as f:
        f.write("TASK4_COMPLETE:PROMPT_READY")

except Exception as e:
    print(f"\n❌ Error: {e}")

print("\n💡 The RAG prompt formula ensures accurate, context-based answers!")
print("\n✅ Task 4 completed!")