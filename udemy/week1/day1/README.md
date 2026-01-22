
---

# AI Website Content Analyzer (OpenAI)

This project demonstrates how to **scrape website content** and **analyze or summarize it using OpenAI models**.
It focuses on **prompt structure (system + user prompts)** and **modern OpenAI API usage**, without any domain-specific logic (e.g., finance).

---

## 📌 What This Project Does

1. Fetches and cleans text content from a website
2. Builds structured prompts (system + user)
3. Sends the content to an OpenAI model
4. Returns an AI-generated response (summary, analysis, or interpretation)

This project is designed as a **learning and experimentation lab** for:

* Prompt engineering
* Website content processing
* OpenAI API integration
* System vs user prompt behavior

---

## 🧱 Project Structure

```
.
├── scraper.py          # Website scraping utilities
├── main.ipynb / main.py # OpenAI interaction logic
├── .env                # API key (ignored by git)
├── README.md           # Documentation
```

---

## 🔐 Environment Setup

### 1️⃣ Install dependencies

```bash
pip install openai python-dotenv requests beautifulsoup4
```

Optional (for debugging):

```bash
pip install snoop icecream
```

---

### 2️⃣ Create a `.env` file

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx
```

> ⚠️ Keep your API key private. Do not commit `.env` to version control.

---

## 🌐 Website Scraping (`scraper.py`)

### Purpose

The scraper extracts **human-readable text** from a webpage so it can be safely and efficiently sent to an LLM.

---

### `fetch_website_contents(url)`

```python
def fetch_website_contents(url):
```

**What it does:**

* Fetches the webpage using `requests`
* Parses HTML with `BeautifulSoup`
* Extracts the page title
* Removes non-content elements:

  * `<script>`
  * `<style>`
  * `<img>`
  * `<input>`
* Returns clean text limited to **10,000 characters**

**Why limit content size?**

* Prevents excessive token usage
* Keeps prompts predictable and efficient

---

### `fetch_website_links(url)`

```python
def fetch_website_links(url):
```

**What it does:**

* Extracts all anchor (`<a>`) links from the page
* Filters out empty or invalid links

This function is intentionally simple and optimized for clarity rather than performance.

---

## 🤖 OpenAI Client Setup

```python
from openai import OpenAI
client = OpenAI()
```

The OpenAI client automatically reads the API key from the `.env` file.

---

## 🧠 Prompt Design

### System Prompt

```python
system_prompt = """
You are an AI assistant that analyzes website content
and provides clear, accurate, and concise responses.
"""
```

**Purpose:**

* Defines the assistant’s role
* Controls tone and behavior
* Applies consistently across all requests

The system prompt is **persistent and global**.

---

### User Prompt Prefix

```python
user_prompt_prefix = """
You are interacting with an AI assistant.
"""
```

This prompt introduces the task context and is combined with the scraped website content.

---

## 🧩 Message Construction

```python
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]
```

**Why this matters:**

* Matches OpenAI’s expected role-based structure
* Separates instructions from data
* Makes prompts reusable and easy to modify

---

## 📊 Website Analysis Function

### `summarize(url)`

```python
def summarize(url):
    website = fetch_website_contents(url)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages_for(website)
    )

    return response.output_text
```

**Execution flow:**

1. Scrape website content
2. Build system + user prompts
3. Send prompts to OpenAI using the **Responses API**
4. Return the model’s output as plain text

---

## 🚨 Important API Note

This project uses the **modern OpenAI Responses API**:

```python
client.responses.create(...)
```

### ❌ Deprecated (do not use)

```python
client.chat.completions.create(...)
```

The `chat.completions` API has been replaced and will cause errors in new SDK versions.

---

## 🧪 Example Usage

```python
text = summarize(
    "https://andrevsilva.com/freedomsblog/articles/aboutblog.html"
)
print(text)
```

This returns an AI-generated summary or analysis of the website’s content.

---

## 🛠 Debugging Utilities (Optional)

* **`snoop`** – traces function execution line by line
* **`icecream (ic)`** – prints variables in a readable format

Example:

```python
from icecream import ic
ic(text)
```

These tools are useful for learning and debugging but are not required.

---

## 🚀 Possible Extensions

* Add domain-specific system prompts (finance, legal, marketing, etc.)
* Output structured JSON instead of plain text
* Chunk large websites automatically
* Cache website content to avoid repeated scraping
* Build a CLI or web interface

---

## ✅ Summary

This project is a **general-purpose AI website content analyzer** that demonstrates:

* Web scraping
* Prompt engineering
* Modern OpenAI API usage
* Clean and extensible Python design

It is intentionally **generic**, making it easy to adapt to any domain by changing only the system prompt.

--- 🚀
