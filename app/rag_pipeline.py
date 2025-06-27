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


