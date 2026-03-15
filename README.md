# Groq-Powered Telegram Bot (Luffy AI)

A Telegram bot built with **FastAPI** and **LangChain** that uses **Groq** to respond dynamically to user messages—**speaking just like Luffy from One Piece!**

## 🚀 Features
- **FastAPI Backend**: Handles Telegram Webhook updates.
- **LangChain Integration**: Uses `create_agent` with a system prompt setting the AI persona to Luffy.
- **Improved Error Handling**: Catches execution errors and relays them back to chat cleanly.

---

## 🛠️ Setup & Installation

### 1. Create and Activate a Virtual Environment
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Environment variables **must be set in your system environment** before running because `load_dotenv()` has been removed from application code.

On Windows (PowerShell):
```powershell
$env:TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
$env:GROQ_API_KEY="your_groq_api_key_here"
```

On Linux/macOS:
```bash
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
export GROQ_API_KEY="your_groq_api_key_here"
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
- `main.py`: FastAPI server receiving Webhook responses and executing the agent call inside `try-except`.
- `agent.py`: Langchain agent configured to talk like Luffy on Groq inference.
