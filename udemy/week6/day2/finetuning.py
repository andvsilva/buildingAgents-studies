from litellm import completion
from dotenv import load_dotenv
import json
from pricer.batch import Batch
from pricer.items import Item

load_dotenv(override=True)

LITE_MODE = True

username = "andrevsilva"
dataset = f"{username}/items_raw_lite" if LITE_MODE else f"{username}/items_raw_full"

train, val, test = Item.from_hub(dataset)

items = train + val + test

print(f"Loaded {len(items):,} items")
print(items[0])

items[2].id

# Give every item an id

for index, item in enumerate(items):
    item.id = index



SYSTEM_PROMPT = """Create a concise description of a product. Respond only in this format. Do not include part numbers.
Title: Rewritten short precise title
Category: eg Electronics
Brand: Brand name
Description: 1 sentence description
Details: 1 sentence on features"""

print(items[0].full)

messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": items[0].full}]
response = completion(messages=messages, model="groq/openai/gpt-oss-20b", reasoning_effort="low")

print(response.choices[0].message.content)
print()
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Cost: {response._hidden_params['response_cost']*100:.3f} cents")


messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": items[0].full}]
response = completion(messages=messages, model="ollama/llama3.2", api_base="http://localhost:11434")
print(response.choices[0].message.content)
print()
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Cost: {response._hidden_params['response_cost']*100:.3f} cents")

MODEL = "openai/gpt-oss-20b"

def make_jsonl(item):
    body = {"model": MODEL, "messages": [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": item.full}], "reasoning_effort": "low"}
    line = {"custom_id": str(item.id), "method": "POST", "url": "/v1/chat/completions", "body": body}
    return json.dumps(line)

def make_file(start, end, filename):
    batch_file = filename
    with open(batch_file, "w") as f:
        for i in range(start, end):
            f.write(make_jsonl(items[i]))
            f.write("\n")

make_file(0, 1000, "jsonl/0_1000.jsonl")

import os
from groq import Groq

groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
with open("jsonl/0_1000.jsonl", "rb") as f:
    response = groq.files.create(file=f, purpose="batch")
response

file_id = response.id

response = groq.batches.create(completion_window="24h", endpoint="/v1/chat/completions", input_file_id=file_id)

result = groq.batches.retrieve(response.id)

response = groq.files.content(result.output_file_id)
response.write_to_file("jsonl/batch_results.jsonl")

with open("jsonl/batch_results.jsonl", "r") as f:
    for line in f:
        json_line = json.loads(line)
        id = int(json_line["custom_id"])
        summary = json_line["response"]["body"]["choices"][0]["message"]["content"]
        items[id].summary = summary


print(items[0].full)
print(items[1000].summary)


Batch.create(items, LITE_MODE)
Batch.run()
Batch.fetch()
for index, item in enumerate(items):
    if not item.summary:
        print(index)
print(items[10234].summary)
# Remove the fields that we don't need in the hub

for item in items:
    item.full = None
    item.id = None

username = "andrevsilva"
full = f"{username}/items_full"
lite = f"{username}/items_lite"

if LITE_MODE:
    train = items[:20_000]
    val = items[20_000:21_000]
    test = items[21_000:]
    Item.push_to_hub(lite, train, val, test)
else:
    train = items[:800_000]
    val = items[800_000:810_000]
    test = items[810_000:]
    Item.push_to_hub(full, train, val, test)

    train_lite = train[:20_000]
    val_lite = val[:1_000]
    test_lite = test[:1_000]
    Item.push_to_hub(lite, train_lite, val_lite, test_lite)

