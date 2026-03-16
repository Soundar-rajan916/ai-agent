import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY
)
agents = create_agent(
    model=llm,
    tools=[],
    system_prompt="you are a personal assistantand you name is Arthur"
)

def agent(message: str) -> str:
    response = agents.invoke({"messages": [{"role": "user", "content": message}]})
    return response["messages"][-1].content
