#!/usr/bin/env python3
"""
Task 1: Temperature Exploration
Learn how temperature affects LLM output randomness.
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
    
    # Launch in background
    subprocess.Popen(
        [sys.executable, app_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

def main():
    print("=" * 65)
    print("Task 1: Temperature - The Randomness Dial")
    print("=" * 65)
    
    # Initialize OpenAI client with environment variables
    client = OpenAI(
        api_key=get_api_key() ,
    )
    
    MODEL_ID = "gpt-4.1-mini"
    
    # The prompt we will use for all tests
    prompt = "Write a one-sentence product description for a coffee mug."
    
    print(f"\nPrompt: {prompt}")
    print("-" * 65)
    
    # --- EXPERIMENT 1: Low Temperature (Deterministic) ---
    print("\n[Temperature = 0] Deterministic Mode")
    print("Running 3 times with temperature=0...")
    
    for i in range(3):
        # Set temperature to 0 for deterministic output
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=50
        )
        print(f"  Run {i+1}: {response.choices[0].message.content}")
    
    print("\nObservation: With temperature=0, outputs should be identical.")
    
    # --- EXPERIMENT 2: High Temperature (Creative) ---
    print("\n" + "-" * 65)
    print("[Temperature = 1] Creative Mode")
    print("Running 3 times with temperature=1...")
    
    for i in range(3):
        # Set temperature to 1 for creative output
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=50
        )
        print(f"  Run {i+1}: {response.choices[0].message.content}")
    
    print("\nObservation: With temperature=1, outputs should vary each time.")
    
    # --- KEY INSIGHT ---
    print("\n" + "=" * 65)
    print("KEY INSIGHT:")
    print("- Temperature = 0: Always picks the highest probability token")
    print("- Temperature = 1: Samples according to actual probabilities")
    print("- For a drive-thru agent: Use low temperature (consistency)")
    print("- For creative writing: Use high temperature (variety)")
    print("=" * 65)
    
    # Create marker file
    os.makedirs("markers", exist_ok=True)
    with open("markers/task1_complete.txt", "w") as f:
        f.write("TEMPERATURE_EXPLORATION_COMPLETE")
    
    print("\nTask 1 Complete!")
    
    # Launch visualizer and prompt user
    print("\n" + "=" * 65)
    print("VISUALIZER: Launching LLM Tuning Studio...")
    print("=" * 65)
    launch_visualizer()
    print("\nThe visualizer is starting on port 7860.")
    print("To explore Temperature settings interactively:")
    print("  1. Click the 'Gradio UI' button (top-right of lab)")
    print("  2. Go to 'Temperature Comparison' tab")
    print("  3. Experiment with different temperature values!")
    print("=" * 65)

if __name__ == "__main__":
    main()

