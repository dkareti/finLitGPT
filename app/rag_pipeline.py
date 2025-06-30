from sentence_transformers import SentenceTransformer
import faiss #a vector similarity search library
import json
import numpy as np

'''
Libraries needed to use open ai's API
'''
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("vector_store/faiss_index.bin")

with open('data/finance_articles.json') as f:
    docs = json.load(f)

def get_answer(query):
    #embedd query
    query_vec = model.encode([query])

    #search the faiss index
    #the lower the distance, the more similar the match, 
    #the distance is the euclidean distance between the query vector and the top 3 similar vectors
    distance, indices = index.search(np.array(query_vec), k=3)
    context = "\n\n".join([docs[i]['content'] for i in indices[0]])

    #send to llm
    prompt = f"Answer the question based on the context below. \n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']



