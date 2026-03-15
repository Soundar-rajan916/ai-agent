import os
from langchain_groq import ChatGroq

# get key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)

def agent(message: str) -> str:
    response = llm.invoke(message)
    return response.content