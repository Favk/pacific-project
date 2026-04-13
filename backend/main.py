from fastapi import FastAPI
from pydantic import BaseModel
from documents import documents
from search import search_documents
from permissions import filter_by_permission
import time

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    query: str
    role: str

@app.get("/")
def home():
    return {"message": "Pacific Search Assistant is running"}

@app.post("/ask")
def ask(req: Request):
    start = time.time()

    results = search_documents(req.query, documents)
    allowed = filter_by_permission(req.role, results)

    ttft = round((time.time() - start) * 1000, 2)

    if not allowed:
    # simple retry strategy
        shorter_query = " ".join(req.query.split()[:1])
        results = search_documents(shorter_query, documents)
        allowed = filter_by_permission(req.role, results)

    if not allowed:
        answer = "No relevant documents found for your role."
    else:
        top_docs = allowed[:2]
        combined = " ".join([doc["content"] for doc in top_docs])
        answer = f"Based on your access level, here’s what I found: {combined}"

    return {
        "answer": answer,
        "documents": allowed,
        "ttft_ms": ttft
    }