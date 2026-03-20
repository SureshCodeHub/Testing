from fastapi import FastAPI
from app.rag_pipeline import generate_answer

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    answer = generate_answer(query)
    return {"answer": answer}

@app.get("/health")
def health():
    return {"status": "ok"} 