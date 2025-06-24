from sentence_transformers import SentenceTransformer
# from transformers import pipeline #Hugging Face Transformers
import faiss #a vector similarity search library
import json
import numpy as np

import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


