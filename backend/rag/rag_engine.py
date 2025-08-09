# backend/rag/rag_engine.py

from typing import Dict
from langchain_core.vectorstores import InMemoryVectorStore
from .embedder import get_embedder
from .loader import load_and_split_pdf
from .prompt import get_prompt
from .llm_wrapper import get_llm
import os

from dotenv import load_dotenv
load_dotenv() 

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Keep global components to avoid re-instantiating unnecessarily
embedder = get_embedder()
llm = get_llm()
prompt = get_prompt()

# Cache so the PDF is not processed repeatedly
_vector_store_cache = {}

def answer_question(question: str, pdf_path: str, k: int = 3) -> Dict:
    global _vector_store_cache

    # Load and index the PDF if not cached
    if pdf_path not in _vector_store_cache:
        splits = load_and_split_pdf(pdf_path)
        vector_store = InMemoryVectorStore(embedder)
        vector_store.add_documents(splits)
        _vector_store_cache[pdf_path] = (vector_store, splits)
    else:
        vector_store, splits = _vector_store_cache[pdf_path]

    # Retrieve top-k documents
    docs = vector_store.similarity_search(question, k=k)
    context_text = "\n\n".join(doc.page_content for doc in docs)

    # Ask LLM
    messages = prompt.format_messages(question=question, context=context_text)
    response = llm.invoke(messages)

    return {
        "answer": response.content.strip(),
        "contexts": [doc.page_content for doc in docs],
        "matching_chunks": [doc.metadata.get("page", None) for doc in docs],
        "documents": docs
    }
