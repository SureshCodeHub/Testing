from app.embeddings import get_embedding
from app.vector_store import search_vector_db
from openai import OpenAI
import os


def generate_answer(query):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)
    query_embedding = get_embedding(query)

    docs = search_vector_db(query_embedding)

    context = "\n".join(docs)

    prompt = f"""
    Answer based on context:
    {context}

    Question: {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content