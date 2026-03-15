# Groq-Powered Telegram Bot

A Telegram bot built with **FastAPI** and **LangChain** that uses **Groq** (Llama model) to respond dynamically to user messages.

## 🚀 Features
- **FastAPI Backend**: Handles Telegram Webhook updates.
- **LangChain + Groq Integration**: Forwards chat text to Groq AI inference.
- **Robust Message Handling**: Safely parses text and reports errors back to chat.

---

## 🛠️ Setup & Installation

### 1. Create a Virtual Environment
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
GROQ_API_KEY="your_groq_api_key_here"
```

---

## 🏃 Running the Application

Start the FastAPI server:
```powershell
uvicorn main:app --reload
```

> [!IMPORTANT]
> To receive messages, you must set up your **Telegram Webhook** to point to your running server (use tools like `ngrok` for exposing localhost to HTTPS).
> 
> ```url
> https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook?url=<YOUR_PUBLIC_URL>/webhook
> ```

---

## 📂 Project Structure
- `main.py`: The entrypoint containing the FastAPI application and the `/webhook` endpoint.
- `agent.py`: Handles initializing `ChatGroq` and invoking the model for responses.
- `.env`: Holds secure API secrets.
