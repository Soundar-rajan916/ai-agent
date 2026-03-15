import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request
import requests
from agent import agent
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

app = FastAPI()


def ai_agent(message):
    return agent(message)

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]

    response = ai_agent(text)
    print(data)
    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={"chat_id": chat_id, "text": response}
    )

    return {"status": "ok"}