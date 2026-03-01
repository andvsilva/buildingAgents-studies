from pydantic import BaseModel
from typing import List, Optional


class ToolExecution(BaseModel):
    tool_name: str
    input: str
    output: str


class AgentResult(BaseModel):
    answer: str
    tools_used: List[ToolExecution]
    generated_sql: Optional[str] = None