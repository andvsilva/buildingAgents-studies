# Illusion of memory 
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


# instance to calling the GPT LLM
openai = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm andrevsilva!"}
    ]

response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
text = response.choices[0].message.content
print(text)

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What's my name?"}
    ]

response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
text = response.choices[0].message.content
print(text)

"""
Here's the thing: every call to an LLM is completely STATELESS. 
It's a totally new call, every single time. As AI engineers, 
it's OUR JOB to devise techniques to give the impression that 
the LLM has a "memory".
"""

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed! How can I assist you today?"},
    {"role": "user", "content": "What's my name?"}
    ]

response = openai.chat.completions.create(model="gpt-4.1-mini", messages=messages)
text = response.choices[0].message.content
print(text)
