import os
import argparse
from datetime import datetime
import ollama

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_document(prompt: str, temperature: float = 0.7):
    """
    Calls LLaMA model via Ollama to generate a compliance document.
    """

    system_prompt = """
You are a financial compliance expert generating realistic regulatory policy documents.
Each document must:
- Be detailed
- Contain structured sections
- Include AML, KYC, encryption, retention, governance
- Be realistic and varied
- Avoid repeating exact wording from previous outputs
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        options={
            "temperature": temperature,
        }
    )

    return response["message"]["content"]


def generate_documents(base_prompt: str, quantity: int):
    """
    Generates multiple documents using LLaMA.
    """

    for i in range(quantity):
        print(f"Generating document {i+1}/{quantity}...")

        variation_prompt = f"""
{base_prompt}

Generate a unique and realistic financial compliance policy.
Vary:
- Organization name
- Jurisdiction
- Encryption standard
- Retention period
- Risk level classification
- Monitoring model
- Regulatory authority
"""

        content = generate_document(variation_prompt)

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"llama_compliance_{i+1}_{timestamp}.txt"

        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)

        print("Saved:", filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLaMA RAG Data Generator")
    parser.add_argument("--prompt", type=str, required=True, help="Base prompt to start generation")
    parser.add_argument("--quantity", type=int, default=10, help="Number of documents to generate")

    args = parser.parse_args()

    generate_documents(args.prompt, args.quantity)