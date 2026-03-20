from transformers import pipeline
from langchain_community.llms import huggingface_pipeline

pipe = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_new_tokens=200
)

llm = huggingface_pipeline(pipeline=pipe)

response = llm.invoke("Explain LangGraph")
print(response)