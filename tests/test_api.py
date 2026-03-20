from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rag():
    # ✅ Mock the LLM call
    with patch("app.main.generate_answer") as mock:
        mock.return_value = "RAG means Retrieval Augmented Generation"

        response = client.get("/ask?query=What is RAG?")
        
        assert response.status_code == 200
        assert "answer" in response.json()