#!/usr/bin/env python3
"""
Task 6: Production Scenarios - Apply All Settings
Configure LLM for different real-world use cases.
"""

import os
import subprocess
import sys
from openai import OpenAI
from config import get_api_key

def launch_visualizer():
    """Launch the Gradio visualizer in background."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(script_dir, "app.py")
    
    subprocess.Popen(
        [sys.executable, app_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

def main():
    print("=" * 65)
    print("Task 6: Production Scenarios - Apply All Settings")
    print("=" * 65)
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=get_api_key()
    )
    
    MODEL_ID = "gpt-4.1-mini"
    
    # ===================================================================
    # SCENARIO 1: Drive-Thru Ordering Agent
    # ===================================================================
    print("\n" + "=" * 65)
    print("SCENARIO 1: Drive-Thru Ordering Agent")
    print("=" * 65)
    print("Goal: Consistent, menu-focused, stops at turn boundaries")
    
    drive_thru_prompt = """You are a Taco Bell drive-thru ordering agent.
Customer: Hi, I'd like to order a Crunchy Taco.
Agent:"""
    
    # Configure for CONSISTENCY (low temperature)
    drive_thru_response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": drive_thru_prompt}],
        temperature=0,             # for consistency
        top_p=0.3,                 # Narrow vocabulary
        max_tokens=50,
        stop=["Customer:"],        # Stop at turn boundary
        frequency_penalty=0,       # Repetition OK for scripts
        presence_penalty=0
    )
    
    print(f"\nAgent Response:\n{drive_thru_response.choices[0].message.content}")
    print(f"Finish reason: {drive_thru_response.choices[0].finish_reason}")
    
    print("\nSettings used:")
    print("  Temperature: 0 (deterministic)")
    print("  Top P: 0.3 (narrow vocabulary)")
    print("  Stop Sequence: 'Customer:'")
    print("  Penalties: 0 (consistency over variety)")
    
    # ===================================================================
    # SCENARIO 2: Creative Story Writer
    # ===================================================================
    print("\n" + "=" * 65)
    print("SCENARIO 2: Creative Story Writer")
    print("=" * 65)
    print("Goal: Varied, imaginative, no repetition")
    
    creative_prompt = "Write a creative opening paragraph for a fantasy novel."
    
    # Configure for CREATIVITY (high temperature)
    creative_response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": creative_prompt}],
        temperature=0.9,           # Set to 0.9 for creativity
        top_p=0.95,                # Wide vocabulary
        max_tokens=100,
        frequency_penalty=0.8,     # Avoid word repetition
        presence_penalty=0.6       # Encourage new topics
    )
    
    print(f"\nStory Opening:\n{creative_response.choices[0].message.content}")
    
    print("\nSettings used:")
    print("  Temperature: 0.9 (creative)")
    print("  Top P: 0.95 (wide vocabulary)")
    print("  Frequency Penalty: 0.8 (varied words)")
    print("  Presence Penalty: 0.6 (new concepts)")
    
    # ===================================================================
    # SCENARIO 3: Code Documentation Generator
    # ===================================================================
    print("\n" + "=" * 65)
    print("SCENARIO 3: Code Documentation Generator")
    print("=" * 65)
    print("Goal: Accurate, consistent, technical")
    
    code_prompt = """Write a docstring for this Python function:
def calculate_tax(amount, rate):
    return amount * rate"""
    
    # Configure for ACCURACY (low temperature, moderate penalties)
    code_response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": code_prompt}],
        temperature=0.2,           # Set to 0.2 for accuracy
        top_p=0.8,
        max_tokens=80,
        frequency_penalty=0.3,
        presence_penalty=0.1
    )
    
    print(f"\nDocumentation:\n{code_response.choices[0].message.content}")
    
    print("\nSettings used:")
    print("  Temperature: 0.2 (accurate but not rigid)")
    print("  Top P: 0.8 (mostly standard vocabulary)")
    print("  Low penalties (technical consistency)")
    
    # ===================================================================
    # SUMMARY
    # ===================================================================
    print("\n" + "=" * 65)
    print("PRODUCTION SETTINGS SUMMARY")
    print("=" * 65)
    print("""
    | Use Case          | Temp | Top P | Freq Pen | Pres Pen |
    |-------------------|------|-------|----------|----------|
    | Customer Service  | 0    | 0.3   | 0        | 0        |
    | Creative Writing  | 0.9  | 0.95  | 0.8      | 0.6      |
    | Code/Technical    | 0.2  | 0.8   | 0.3      | 0.1      |
    | Summarization     | 0.3  | 0.9   | 0.5      | 0.2      |
    | Brainstorming     | 1.0  | 0.95  | 0.5      | 0.8      |
    """)
    
    print("KEY TAKEAWAY:")
    print("There is no 'best' setting - it depends on your use case!")
    print("  - Consistency needed? Low temperature, narrow Top P")
    print("  - Creativity needed? High temperature, wide Top P, penalties")
    
    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task6_complete.txt", "w") as f:
        f.write("PRODUCTION_SCENARIOS_COMPLETE")
    
    print("\n" + "=" * 65)
    print("Task 6 Complete! You've mastered LLM settings!")
    print("=" * 65)
    
    # Launch visualizer and prompt user
    print("\n" + "=" * 65)
    print("VISUALIZER: LLM Tuning Studio")
    print("=" * 65)
    launch_visualizer()
    print("\nTo explore all production scenarios:")
    print("  1. In the Gradio UI (already open from Task 1)")
    print("  2. Go to 'Production Scenarios' tab")
    print("  3. See recommended settings for different use cases!")
    print("=" * 65)

if __name__ == "__main__":
    main()
