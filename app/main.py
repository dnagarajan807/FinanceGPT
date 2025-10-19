from fastapi import FastAPI
from app.router import router

app = FastAPI(
    title="FinanceGPT",
    description="Ask financial questions over enterprise data using GenAI (RAG).",
    version="1.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "FinanceGPT API is running. Use /api/ask endpoint to query financial data."}
