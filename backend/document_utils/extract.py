from langchain_core.documents import Document
from langchain_core.runnables import chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage
from vector_utils.vectoriser import Vectoriser
from db.vector_store import clarityVectorStore
from typing import List, Dict

"""
documents = [
    Document(
        page_content="A quick brown fox",
        metadata={"source": "sample_doc"},
    ),
    Document(
        page_content="Jumps over the lazy dog",
        metadata={"source": "sample doc"},
    ),
]
"""

class ResourcePipeline:
    def __init__(self, in_path: str = "./resources/"):
        self.in_path = in_path
        self.all_splits: List[Document] = []
        
    def extract_and_chunk_from_pdf(self, chunk_size: int = 1000, overlap: int = 200) -> List[Document]:
        loader = PyPDFLoader(self.in_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=overlap, add_start_index=True
        )

        self.all_splits = text_splitter.split_documents(docs)
        return self
    
    def add_embeddings_to_vector_store(self, resource_id: str) -> None:
        vectoriser = Vectoriser()
        vector_store = clarityVectorStore()
        points: List[Dict] = []

        for idx, doc in enumerate(self.all_splits):
            try:
                vector = vectoriser.embed(doc.page_content)
                points.append({
                    "id": f"{resource_id}_{idx}",
                    "vector": vector,
                    "payload": {
                        "resource_id": resource_id,
                        "chunk_index": idx,
                        "text": doc.page_content
                    }
                })
                print(f"Document id {resource_id}_{idx} added.")
            except Exception as e:
                print(f"Error while embedding id {idx}: {e}")
                continue
        
        vector_store.q_client.upsert(
            collection_name=vector_store.collection_name,
            points=points
        )

        print(f"Inserted {len(points)} chunks into collection")
        return None
    
    @tool("retreive context", description="Retreives embeddings from the vector store")
    def retreive_context(self, query: str, runtime: ToolRuntime) -> List[Document]:
        """
        Tool for retreiving the context
        """
        pass

    @tool
    def get_last_user_message(runtime: ToolRuntime) -> str:
        """
        Get the last message from the user.
        """
        messages = runtime.state["messages"]
        for message in reversed(messages):
            if isinstance(message, HumanMessage):
                return message.content
        
        return "No user message found"

    
    @chain
    def retreive_embeddings(self, query: str) -> List[Document]:
        return 
