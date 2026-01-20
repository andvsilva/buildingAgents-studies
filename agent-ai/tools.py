from langchain_core.tools import tool

@tool
def search_tool(query: str) -> str:
    """Search information (mock)."""
    return f"Search result for: {query}"

@tool
def wiki_tool(topic: str) -> str:
    """Wikipedia lookup (mock)."""
    return f"Wikipedia summary for: {topic}"

@tool
def save_tool(text: str) -> str:
    """Save text somewhere (mock)."""
    return f"Saved: {text}"
