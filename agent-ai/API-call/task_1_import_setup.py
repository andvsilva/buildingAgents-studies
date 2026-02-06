#!/usr/bin/env python3
"""
Task 1: Import Required Libraries
Learn what libraries we need for AI API calls.
"""

# Step 1: Import the OpenAI library
# This library helps us talk to AI models
import openai  # TODO: Import "openai"

# Step 2: Import os for environment variables
# This helps us access API keys safely
import os  # TODO: Import "os"

print("✅ Step 1 Complete: Libraries imported!")
print("- openai: For making API calls")
print("- os: For accessing environment variables")

# Create marker
import os
from pathlib import Path

def setup_directories():
    """
    Create required directories for the agent.
    Uses a user-writable location to avoid permission errors.
    """

    # Option 1: project-relative directory (recommended for repos)
    BASE_DIR = Path(__file__).resolve().parent
    markers_dir = BASE_DIR / "markers"

    # Option 2: home directory (uncomment if you prefer)
    # markers_dir = Path.home() / "markers"

    markers_dir.mkdir(parents=True, exist_ok=True)

    print(f"Markers directory ready at: {markers_dir}")


def main():
    setup_directories()
    print("Import and setup completed successfully.")


if __name__ == "__main__":
    main()
