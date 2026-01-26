from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"

client = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"  # required but ignored by Ollama
)

response = client.responses.create(
    model="llama3.2:1b",
    input="Explain to me, Physics state-of-the-art"
)

print(response.output_text)
