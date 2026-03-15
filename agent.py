import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

# ChatGroq automatically picks up GROQ_API_KEY from .env
llm = ChatGroq(model="llama-3.1-8b-instant")

def agent(message: str) -> str:
    """
    Invokes the LLM with the message.
    """
    response = llm.invoke(message)
    return response.content

