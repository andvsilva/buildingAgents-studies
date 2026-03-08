#!/usr/bin/env python3
"""
Task 2: Top P Exploration
Learn how Top P (nucleus sampling) filters the token pool.
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
    print("Task 2: Top P - Cumulative Probability Filter")
    print("=" * 65)
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=get_api_key()
    )
    
    MODEL_ID = "gpt-4.1-mini"
    
    prompt = "Complete this sentence: The capital of France is"
    
    print(f"\nPrompt: {prompt}")
    print("-" * 65)
    
    # --- EXPERIMENT 1: Top P = 1.0 (All tokens considered) ---
    print("\n[Top P = 1.0] All tokens are candidates")
    print("The model considers ALL possible next tokens...")
    
    # Set top_p to 1.0 (all tokens)
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=1,
        max_tokens=20
    )
    print(f"  Output: {response.choices[0].message.content}")
    
    # --- EXPERIMENT 2: Top P = 0.5 (Only high-prob tokens) ---
    print("\n" + "-" * 65)
    print("[Top P = 0.5] Only high-probability tokens")
    print("Tokens are sorted by probability, only those adding up to 50% are kept...")
    
    # Set top_p to 0.5 (narrow pool)
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=0.5,
        max_tokens=20
    )
    print(f"  Output: {response.choices[0].message.content}")
    
    # --- EXPERIMENT 3: Very narrow Top P ---
    print("\n" + "-" * 65)
    print("[Top P = 0.1] Very narrow - only most likely token(s)")
    
    # Set top_p to 0.1 (very narrow)
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        top_p=0.1,
        max_tokens=20
    )
    print(f"  Output: {response.choices[0].message.content}")
    
    # --- VISUALIZATION EXPLANATION ---
    print("\n" + "=" * 65)
    print("HOW TOP P WORKS:")
    print("-" * 65)
    print("Token Probabilities for 'The capital of France is ___':")
    print("  Paris:  72%  |########################################|")
    print("  the:    12%  |######                                  |")
    print("  a:       5%  |##                                      |")
    print("  known:   3%  |#                                       |")
    print("  one:     2%  |#                                       |")
    print("-" * 65)
    print("Top P = 0.84 cutoff: Only 'Paris' and 'the' are considered")
    print("                     (72% + 12% = 84%)")
    print("=" * 65)
    
    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task2_complete.txt", "w") as f:
        f.write("TOP_P_EXPLORATION_COMPLETE")
    
    print("\nTask 2 Complete!")
    
    # Launch visualizer and prompt user
    print("\n" + "=" * 65)
    print("VISUALIZER: LLM Tuning Studio")
    print("=" * 65)
    launch_visualizer()
    print("\nTo see Top P filtering visually:")
    print("  1. In the Gradio UI (already open from Task 1)")
    print("  2. Go to 'Token Visualization' tab")
    print("  3. Adjust the Top P slider and see which tokens are filtered!")
    print("=" * 65)

if __name__ == "__main__":
    main()

