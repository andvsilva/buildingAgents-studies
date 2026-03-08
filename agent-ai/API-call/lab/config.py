import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return key