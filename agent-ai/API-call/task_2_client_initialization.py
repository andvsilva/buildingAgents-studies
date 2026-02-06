#!/usr/bin/env python3
"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""

import openai
import os
from dotenv import load_dotenv

# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

# TODO: Initialize the OpenAI client
client = openai.OpenAI()

print("✅ Step 2 Complete: Connected to OpenAI!")
print(f"- API Key: {os.getenv('OPENAI_API_KEY')[:20]}...")
#print(f"- Base URL: {os.getenv('OPENAI_API_BASE')}")

# Create marker
os.makedirs("markers", exist_ok=True)
with open("markers/task2_client_complete.txt", "w") as f:
    f.write("SUCCESS")