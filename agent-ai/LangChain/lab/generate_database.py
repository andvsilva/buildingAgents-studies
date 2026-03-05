import os
import argparse
from datetime import datetime
import ollama
import random
from datetime import datetime, timezone

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_prompt_files(folder_path: str):
    """
    Loads all .txt files from a folder.
    Returns a list of (filename, content).
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Prompt folder not found: {folder_path}")

    prompt_files = []

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            full_path = os.path.join(folder_path, file)
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                prompt_files.append((file, content))

    if not prompt_files:
        raise ValueError("No .txt prompt files found in folder.")

    return prompt_files


def generate_document(prompt: str, temperature: float = 0.9):
    """
    Calls LLaMA model via Ollama.
    """

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {"role": "system", "content": prompt},
        ],
        options={
            "temperature": temperature,
        }
    )

    return response["message"]["content"]


def generate_documents_from_folder(prompt_folder: str, quantity_per_prompt: int):
    """
    Generates documents for each prompt file in folder.
    """

    prompts = load_prompt_files(prompt_folder)

    jurisdictions = [
        "United States",
        "European Union",
        "United Kingdom",
        "Singapore",
        "Brazil",
        "Canada",
        "Australia"
    ]

    encryption_standards = [
        "AES-256",
        "RSA-2048",
        "TLS 1.3",
        "AES-128 with HSM",
        "PKI-based End-to-End Encryption"
    ]

    monitoring_models = [
        "Rule-Based Monitoring",
        "Machine Learning Behavioral Monitoring",
        "Hybrid Risk Scoring",
        "Real-Time Transaction Surveillance",
        "AI Anomaly Detection"
    ]

    for prompt_name, base_prompt in prompts:

        print(f"\nUsing prompt template: {prompt_name}")

        for i in range(quantity_per_prompt):

            print(f"  Generating document {i+1}/{quantity_per_prompt}")

            variation_block = f"""

Additional parameters:
- Jurisdiction: {random.choice(jurisdictions)}
- Encryption Standard: {random.choice(encryption_standards)}
- Monitoring Model: {random.choice(monitoring_models)}
- Ensure organization name is unique.
- Ensure structure is formal and realistic.
- Avoid repeating wording from previous outputs.
"""

            full_prompt = base_prompt + "\n" + variation_block

            content = generate_document(full_prompt)

            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

            clean_prompt_name = prompt_name.replace(".txt", "")
            filename = f"{clean_prompt_name}_{i+1}_{timestamp}.txt"

            with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
                f.write(content)

            print("    Saved:", filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RAG Financial Compliance Dataset Generator")
    parser.add_argument(
        "--prompt_folder",
        type=str,
        required=True,
        help="Folder containing .txt prompt templates"
    )
    parser.add_argument(
        "--quantity",
        type=int,
        default=5,
        help="Documents per prompt file"
    )

    args = parser.parse_args()

    generate_documents_from_folder(args.prompt_folder, args.quantity)