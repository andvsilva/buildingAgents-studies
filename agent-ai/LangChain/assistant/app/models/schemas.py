from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        description="User question for the AI assistant"
    )
    explain: Optional[bool] = Field(
        default=False,
        description="If true, return tool usage and debugging information"
    )


class AskResponse(BaseModel):
    answer: str
    tools_used: Optional[List[str]] = None
    generated_sql: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None