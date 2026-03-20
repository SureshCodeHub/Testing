from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rag():
    response = client.get("/ask?query=What is RAG?")
    assert response.status_code == 200
    assert "answer" in response.json()