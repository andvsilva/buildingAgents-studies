## Types of prompts

"""
You may know this already - but if not, you will get very familiar with it!
Models like GPT have been trained to receive instructions in a particular way.

They expect to receive:

**A system prompt** that tells them what task they are performing and what tone they should use
**A user prompt** -- the conversation starter that they should reply to

"""

# imports
import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import display, Markdown
from openai import OpenAI
import snoop
from icecream import ic

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

"""
To give you a preview -- calling OpenAI with these messages is this easy. 
Any problems, head over to the Troubleshooting notebook.
Define our system prompt - you can experiment with this later, changing 
the last sentence to 'Respond in markdown in Spanish."
And now: call the OpenAI API. You will get very familiar with this!
See how this function creates exactly the format above
"""

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

@snoop
def summarize(url):
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

# A function to display this nicely in the output, using markdown

@snoop
def display_summary(url):
    summary = summarize(url)
    # display(Markdown(summary)) # Work only on the jupyter notebook.
    ic(summary)

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

# Define our user prompt

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

# Messages
# The API from OpenAI expects to receive messages in a particular structure.
# Many of the other APIs share this structure:

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]

response = client.chat.completions.create(model="gpt-4.1-nano", messages=messages)
response.choices[0].message.content

# See how this function creates exactly the format above

summarize("https://andrevsilva.com")

display_summary("https://andrevsilva.com")

