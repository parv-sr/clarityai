from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from typing import List
from exceptions import StoreAlreadyExists

class clarityVectorStore:
    def __init__(self, model: str = "sentence-transformers/all-MiniLM-L6-v2", name: str = "clarityai_vec_store"):
        self.model = model
        self.collection_name = name
        self.embeddings: List[float]
        self.q_client: QdrantClient = QdrantClient("localhost", port=6333)
        self.embeddings = HuggingFaceEmbeddings(model_name=model)

        if self.q_client.collection_exists(self.collection_name):
            self.vector_store: QdrantVectorStore = QdrantVectorStore(
                client=self.q_client, 
                collection_name=self.collection_name, 
                embedding=self.embeddings,
                )

    def create_collection(self) -> None:
        if not self.q_client.collection_exists(self.collection_name):
            try:
                self.q_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=768, distance=Distance.COSINE)
                )
                print(f"Vector store successfully created!")
            except Exception as e:
                print(f"Failed installation! Error: {e}")
        else:
            raise StoreAlreadyExists(self.q_client.collection_exists(self.collection_name))

        




        