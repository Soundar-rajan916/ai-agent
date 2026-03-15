import os
from fastapi import FastAPI, Request
import requests
from agent import agent

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

app = FastAPI()


@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    print("UPDATE:", data)

    message = data.get("message")

    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if not text:
        return {"ok": True}

    try:
        response = agent(text)
    except Exception as e:
        response = f"Error: {str(e)}"

    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": response
        }
    )

    return {"ok": True}