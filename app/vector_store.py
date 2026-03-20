import faiss
import numpy as np

dimension = 1536
index = faiss.IndexFlatL2(dimension)

documents = [
    "RAG stands for Retrieval Augmented Generation",
    "CI/CD automates deployment",
    "Docker containers package applications"
]

# Preload embeddings (simplified)
vectors = np.random.rand(len(documents), dimension).astype('float32')
index.add(vectors)

def search_vector_db(query_embedding):
    query = np.array([query_embedding]).astype('float32')
    distances, indices = index.search(query, k=2)

    return [documents[i] for i in indices[0]]