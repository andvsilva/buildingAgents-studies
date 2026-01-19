from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from datetime import datetime


@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


@tool
def search_tool(query: str) -> str:
    """Search the web for information."""
    search = DuckDuckGoSearchRun()
    return search.run(query)


@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia for information."""
    api = WikipediaAPIWrapper(
        top_k_results=1,
        doc_content_chars_max=500,
    )
    return api.run(query)
