#!/usr/bin/env python3
"""
Task 4: Stop Sequences
Learn how to use stop sequences to control generation boundaries.
"""

import os
from openai import OpenAI
from config import get_api_key

def main():
    print("=" * 65)
    print("Task 4: Stop Sequences - Controlling Generation Boundaries")
    print("=" * 65)
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=get_api_key()
    )
    
    MODEL_ID = "gpt-4.1-mini"
    
    # Scenario: Drive-thru conversation generator
    # This prompt is designed to encourage the model to generate multiple turns
    prompt = """Continue this drive-thru ordering conversation. Generate at least 3 more exchanges between Agent and Customer:

Agent: Welcome to Taco Bell! May I take your order?
Customer: Yes, I'd like a Crunchy Taco.
Agent:"""
    
    print("\nScenario: Drive-Thru Conversation Generator")
    print("-" * 65)
    print("We want the Agent to respond, then STOP before generating")
    print("the Customer's next line.")
    
    # --- EXPERIMENT 1: Without Stop Sequence ---
    print("\n" + "=" * 65)
    print("[Without Stop Sequence] Generation continues...")
    print("=" * 65)
    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=250  # Increased to allow multi-turn generation
    )
    print(response.choices[0].message.content)
    
    # Check if Customer appears in output
    output_text = response.choices[0].message.content
    if "Customer:" in output_text or "Customer :" in output_text:
        print("\n✓ Notice: The model generated BOTH Agent and Customer lines!")
    else:
        print("\n⚠ Note: Model only generated Agent response this time.")
        print("   (This can vary - stop sequences ensure consistent control)")
    
    # --- EXPERIMENT 2: With Stop Sequence ---
    print("\n" + "=" * 65)
    print("[With Stop Sequence] Generation stops at boundary")
    print("=" * 65)
    
    # Set the stop sequence to stop before Customer's turn
    stop_sequence = "\nCustomer:"
    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=250,  # Same as without stop sequence for fair comparison
        stop=[stop_sequence]  # Stop when this pattern is found
    )
    
    print(response.choices[0].message.content)
    
    # Check the actual finish reason
    finish_reason = response.choices[0].finish_reason
    if finish_reason == "stop":
        print(f"\n✓ [STOPPED] - Stop sequence '{stop_sequence}' triggered!")
        print(f"   Finish reason: {finish_reason}")
    else:
        print(f"\n⚠ Stop sequence did NOT trigger. Finish reason: {finish_reason}")
        print(f"   (The model may not have generated '{stop_sequence}' in its output)")
    
    # --- EXPERIMENT 3: Multiple Stop Sequences ---
    print("\n" + "=" * 65)
    print("[Multiple Stop Sequences] Multiple boundaries")
    print("=" * 65)
    
    # TODO 2: Create a list with multiple stop sequences
    stop_sequences = ["Customer:", "Agent:", "---"]
    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": "Tell me a joke. Then say END."}],
        temperature=0.7,
        max_tokens=100,
        stop=stop_sequences
    )
    
    print(f"Output: {response.choices[0].message.content}")
    print(f"Stop sequences were: {stop_sequences}")
    
    # --- KEY INSIGHT ---
    print("\n" + "=" * 65)
    print("KEY INSIGHT:")
    print("-" * 65)
    print("Stop sequences allow you to:")
    print("  1. Control conversation turn boundaries")
    print("  2. Stop at specific patterns (e.g., 'END', '###')")
    print("  3. Prevent unwanted continuation")
    print("")
    print("Real-world use case:")
    print("  In a Taco Bell drive-thru AI, you want the Agent to respond")
    print("  and STOP, not generate what the Customer says next.")
    print("=" * 65)
    
    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task4_complete.txt", "w") as f:
        f.write("STOP_SEQUENCES_COMPLETE")
    
    print("\nTask 4 Complete!")

if __name__ == "__main__":
    main()
