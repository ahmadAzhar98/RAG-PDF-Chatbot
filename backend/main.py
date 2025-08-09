from pdf_highlighter import highlight_chunks_in_pdf
import tempfile
import os
from rag.rag_engine import answer_question
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from rapidfuzz import fuzz

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    pdf_path: str
    highlight: bool = False
    highlighted_pdf_path: Optional[str] = None 



# def find_best_context_for_highlighting(question, contexts):
#     best_context = contexts[0]  # fallback
#     best_score = 0
    
#     for context in contexts:
#         # Score based on how well context matches the question
#         score = fuzz.partial_ratio(question.lower(), context.lower())
#         if score > best_score:
#             best_score = score
#             best_context = context
    
#     return best_context



@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = answer_question(request.question, request.pdf_path)
    # best_context = find_best_context_for_highlighting(request.question, result["contexts"])    

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
