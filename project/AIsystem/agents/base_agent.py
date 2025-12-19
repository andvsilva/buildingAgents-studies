from llm_client import get_openai_client
from config import MODEL_NAME

class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.client = get_openai_client()

    def act(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.role},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()