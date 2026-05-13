from langchain_huggingface import HuggingFaceEndpointEmbeddings
from typing import List
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Vectoriser:
    def __init__(self, model: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = model
    
    def embed(self, text: str) -> List[float]:
        token = os.getenv("HF_ACCESS_TOKEN")
        if not token:
            raise ValueError("No HF API key found!")
        
        embeddings = HuggingFaceEndpointEmbeddings(
            huggingfacehub_api_token=token,
            model=self.model,
            task="feature-extraction"
        )

        query_result = embeddings.embed_query(text)
        return query_result
    