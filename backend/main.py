from pdf_highlighter import highlight_chunks_in_pdf
import tempfile
import os
from rag.rag_engine import answer_question
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from rapidfuzz import fuzz
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str
    pdf_path: str
    highlight: bool = False
    highlighted_pdf_path: Optional[str] = None 

@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = answer_question(request.question, request.pdf_path)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        highlighted_path = tmp.name
    
    success = highlight_chunks_in_pdf(
        documents=result["documents"],
        output_path=highlighted_path
    )
    if success:
        result["highlighted_pdf"] = highlighted_path
    else:
        result["highlighted_pdf"] = None
    
    return result
