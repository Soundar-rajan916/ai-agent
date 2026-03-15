import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") 

from langchain.agents import create_agent
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")

agent = create_agent(llm)
def agent(message):
    response = agent.invoke({"input": message})
    return response
