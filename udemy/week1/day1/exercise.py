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

system_prompt = """
You are an AI financial assistant for Digital Market Investiment, a business operating in the Financial sector.

Your role is to provide accurate, practical, and business-oriented financial guidance to support decision-making.

Analyze financial data, reports, and metrics (e.g., cash flow, profit & loss, balance sheets, budgets).

"""

# Define our user prompt

user_prompt_prefix = """
You are interacting with an AI financial assistant for a business environment.
"""

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def summarize(url):
    website = fetch_website_contents(url)
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

text = summarize("https://andrevsilva.com/freedomsblog/articles/aboutblog.html")
ic(text)