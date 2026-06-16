import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/arxiv_sample.csv")

print("Loading embedding model...")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Creating embeddings...")

# Convert abstracts into embeddings
embeddings = model.encode(
    df['abstract'].tolist(),
    show_progress_bar=True
)

print("Creating FAISS index...")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("Saving FAISS index...")

# Save FAISS index
faiss.write_index(index, "models/arxiv_index.faiss")

print("Saving paper data...")

# Save dataframe
with open("models/papers.pkl", "wb") as f:
    pickle.dump(df, f)

print("Embeddings created successfully!")