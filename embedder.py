import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os
'''
QUESTION: What is a FAISS index?

ANSWER: A FAISS index is a special data structure that stores embeddings of your documents and lets you search them quickly.
'''
# Load your text chunks
with open("app/data/finance_articles.json") as f:
    data = json.load(f)

#extracts raw text content from the JSON file
texts = [entry["content"] for entry in data]

# Load the sentence embedding model
# this creates a numerical vector that captures the meaning of each sentence
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, convert_to_numpy=True)

# Create the FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Make sure directory exists
os.makedirs("app/vector_store", exist_ok=True)

# Save index
faiss.write_index(index, "app/vector_store/faiss_index.bin")

print("\n FAISS index created and saved to 'faiss_index.bin'\n")