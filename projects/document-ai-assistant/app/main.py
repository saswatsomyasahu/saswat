import os
import shutil
import uuid
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.rag import chat_with_documents, ingest_pdf

load_dotenv()

app = FastAPI(
    title="Document AI Assistant",
    description="RAG demo: upload PDFs, ask questions — portfolio project for cloud/AI roles.",
    version="1.0.0",
)

UPLOAD_DIR = Path("./data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=2000)
    top_k: int = Field(4, ge=1, le=10)


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/health")
def health():
    has_key = bool(os.getenv("OPENAI_API_KEY"))
    return {
        "status": "ok",
        "openai_configured": has_key,
        "hint": None if has_key else "Set OPENAI_API_KEY in .env to enable chat",
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    doc_id = str(uuid.uuid4())
    dest = UPLOAD_DIR / f"{doc_id}.pdf"
    with dest.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        chunk_count = ingest_pdf(dest, doc_id)
    except Exception as exc:
        dest.unlink(missing_ok=True)
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return {"document_id": doc_id, "filename": file.filename, "chunks_indexed": chunk_count}


@app.post("/chat", response_model=ChatResponse)
def chat(body: ChatRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail="OPENAI_API_KEY not set. Copy .env.example to .env and add your key.",
        )
    try:
        answer, sources = chat_with_documents(body.question, top_k=body.top_k)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return ChatResponse(answer=answer, sources=sources)
