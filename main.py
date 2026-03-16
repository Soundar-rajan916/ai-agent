import os
from fastapi import FastAPI, Request
import requests
from agent import agent

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

# only this user can access the bot
ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))

app = FastAPI()


@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    print("UPDATE:", data)

    message = data.get("message")

    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    text = message.get("text", "")

    # block other users
    if user_id != ALLOWED_USER_ID:
        requests.post(
            f"{TELEGRAM_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "🚫 This is a private AI agent."
            }
        )
        return {"ok": True}

    try:
        response = agent(text)
    except Exception as e:
        response = f"Error: {str(e)}"

    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": response,
            "parse_mode": "Markdown"
        }
    )

    return {"ok": True}