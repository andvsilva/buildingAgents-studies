from fastapi import APIRouter, HTTPException
from app.models.schemas import AskRequest, AskResponse
from app.services.agent_service import ask_agent

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/ask", response_model=AskResponse)
async def ask_question(payload: AskRequest):
    """
    Main endpoint for AI Business Intelligence Assistant.
    """

    try:
        result = await ask_agent(
            question=payload.question,
            explain=payload.explain
        )

        return AskResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))