import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import ollama

print("Loading FAISS index...")

# Load FAISS index
index = faiss.read_index("models/arxiv_index.faiss")

print("Loading paper data...")

# Load saved papers
with open("models/papers.pkl", "rb") as f:
    df = pickle.load(f)

print("Loading embedding model...")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


# Function to search papers
def search_papers(query, top_k=3):

    # Convert query into embeddings
    query_embedding = model.encode([query])

    # Search FAISS index
    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    for idx in indices[0]:

        paper = df.iloc[idx]

        results.append({
            "title": paper['title'],
            "abstract": paper['abstract'],
            "category": paper['categories']
        })

    return results


# Function to generate explanation using Phi-3
def generate_explanation(query, papers):

    context = ""

    for paper in papers:

        context += f"""
Title: {paper['title']}

Abstract:
{paper['abstract']}

"""

    prompt = f"""
You are an expert AI research assistant.

Using the research papers below, answer the user's question clearly and simply.

User Question:
{query}

Research Papers:
{context}

Provide:
1. Simple explanation
2. Important concepts
3. Research insights
"""

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']


# Main chatbot loop
query = input("Ask a research question: ")

# Search relevant papers
papers = search_papers(query)

print("\nRelevant Research Papers:\n")

for i, paper in enumerate(papers, 1):

    print(f"{i}. {paper['title']}")
    print(f"Category: {paper['category']}")
    print("-" * 80)

print("\nGenerating AI explanation...\n")

# Generate AI explanation
answer = generate_explanation(query, papers)

print(answer)