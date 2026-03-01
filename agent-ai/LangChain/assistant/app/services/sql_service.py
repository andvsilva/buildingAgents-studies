from langchain_community.utilities import SQLDatabase
from langchain.tools import tool
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:password@localhost:5432/company"
)

# Create DB connection
db = SQLDatabase.from_uri(DATABASE_URL)


@tool
def run_sql_query(query: str) -> str:
    """
    Use this tool to answer questions about structured sales data.
    The input must be a valid SQL query.
    """
    try:
        result = db.run(query)
        return str(result)
    except Exception as e:
        return f"SQL Error: {str(e)}"