#!/usr/bin/env python3
"""
Task 3: Top K Exploration
Learn how Top K provides a hard quantity cutoff for token selection.
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
    print("Task 3: Top K - Hard Quantity Cutoff")
    print("=" * 65)
    
    # Initialize OpenAI client
    client = OpenAI(
        api_key=get_api_key()
    )
    
    MODEL_ID = "gpt-4.1-mini"
    
    prompt = "The best programming language for beginners is"
    
    print(f"\nPrompt: {prompt}")
    print("-" * 65)
    
    print("\nNote: Some API providers do not support top_k directly.")
    print("We will demonstrate the concept and compare with Top P.\n")
    
    # --- CONCEPTUAL COMPARISON ---
    print("=" * 65)
    print("TOP K vs TOP P COMPARISON")
    print("=" * 65)
    print("\nImagine the token probabilities are:")
    print("  Python:     35%")
    print("  JavaScript: 25%")
    print("  Scratch:    15%")
    print("  Java:       10%")
    print("  C++:         8%")
    print("  Ruby:        4%")
    print("  Go:          3%")
    print("-" * 65)
    
    # --- TOP K BEHAVIOR ---
    print("\n[TOP K = 3] Hard cutoff at 3 tokens")
    print("  Included: Python (35%), JavaScript (25%), Scratch (15%)")
    print("  EXCLUDED: Java, C++, Ruby, Go (even if reasonable choices)")
    print("  Problem: Ignores probability - just counts tokens")
    
    # --- TOP P BEHAVIOR ---
    print("\n[TOP P = 0.75] Cumulative probability cutoff")
    print("  Included: Python (35%) + JavaScript (25%) + Scratch (15%) = 75%")
    print("  EXCLUDED: Everything else")
    print("  Benefit: Probability-aware cutoff")
    
    # --- PRACTICAL DEMONSTRATION ---
    print("\n" + "-" * 65)
    print("PRACTICAL DEMONSTRATION")
    print("-" * 65)
    
    # Using Top P to simulate narrow token selection
    print("\nNarrow Top P (simulating Top K effect):")
    
    # Set a narrow top_p value (e.g., 0.3)
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=0.3,
        max_tokens=30
    )
    print(f"  Top P=0.3: {response.choices[0].message.content}")
    
    # Set a wide top_p value (e.g., 0.95)
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=0.95,
        max_tokens=30
    )
    print(f"  Top P=0.95: {response.choices[0].message.content}")
    
    # --- KEY INSIGHT ---
    print("\n" + "=" * 65)
    print("KEY INSIGHT:")
    print("-" * 65)
    print("Top K: 'Consider exactly K tokens, regardless of probability'")
    print("Top P: 'Consider tokens until cumulative probability reaches P'")
    print("")
    print("Why Top P is preferred:")
    print("  - More natural: adapts to probability distribution")
    print("  - Top K might include very unlikely tokens if in top K")
    print("  - Top K might exclude reasonable tokens if just outside K")
    print("=" * 65)
    
    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task3_complete.txt", "w") as f:
        f.write("TOP_K_EXPLORATION_COMPLETE")
    
    print("\nTask 3 Complete!")
    
    # Launch visualizer and prompt user
    print("\n" + "=" * 65)
    print("VISUALIZER: LLM Tuning Studio")
    print("=" * 65)
    launch_visualizer()
    print("\nTo compare Top K vs Top P visually:")
    print("  1. In the Gradio UI (already open from Task 1)")
    print("  2. Go to 'Token Visualization' tab")
    print("  3. Adjust Top P and Top K sliders to see the difference!")
    print("=" * 65)

if __name__ == "__main__":
    main()

