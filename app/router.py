from fastapi import APIRouter
from app.rag_pipeline import query_financegpt

router = APIRouter()

@router.post("/ask")
async def ask_financegpt(payload: dict):
    question = payload.get("question", "")
    if not question:
        return {"error": "Question is required"}
    response = query_financegpt(question)
    return response
