from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TELEGRAM_BOT_TOKEN")
gemini = os.getenv("GEMINI_API_KEY")

if token:
    print(f"✅ Telegram token found: {token[:10]}...")
else:
    print("❌ Telegram token NOT found. Check your .env file.")

if gemini:
    print(f"✅ Gemini key found: {gemini[:5]}...")
else:
    print("❌ Gemini key NOT found. Check your .env file.")