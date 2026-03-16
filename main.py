import os
from fastapi import FastAPI, Request
import requests
from agent import agent

# Telegram configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

# Only allow one user
ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))

app = FastAPI()


# Health check route
@app.get("/")
def home():
    return {"status": "Arthur AI agent running"}


@app.post("/webhook")
async def telegram_webhook(req: Request):

    # Safe JSON parsing
    try:
        data = await req.json()
    except Exception:
        return {"ok": True}

    print("UPDATE:", data)

    message = data.get("message")

    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    text = message.get("text", "")

    # Block unauthorized users
    if user_id != ALLOWED_USER_ID:
        requests.post(
            f"{TELEGRAM_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "🚫 This is a private AI agent."
            }
        )
        return {"ok": True}

    # Show typing indicator
    requests.post(
        f"{TELEGRAM_URL}/sendChatAction",
        json={
            "chat_id": chat_id,
            "action": "typing"
        }
    )

    # Run AI agent
    try:
        response = str(agent(text))
        print("AGENT RESPONSE:", response)
    except Exception as e:
        response = f"⚠️ Agent error: {str(e)}"

    # Telegram message length safety
    response = response[:4000]

    # Send message
    r = requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": response
        }
    )

    print("TELEGRAM API RESPONSE:", r.text)

    return {"ok": True}