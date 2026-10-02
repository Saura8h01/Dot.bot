import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from agent import process_message

# Load environment variables
load_dotenv()

# Setup logging so we can see errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 I'm your Dot. I'm always on.\n\n"
        "Commands:\n"
        "/status - check if I'm alive\n"
        "Or just send me a message to chat!"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Dot is online. Brain is working.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    # Show "typing..." in Telegram while the AI thinks
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    response = await process_message(user_text)
    await update.message.reply_text(response)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not set in .env file")
        return

    # Build the bot
    application = ApplicationBuilder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Dot is running! Open Telegram and send a message to your bot.")
    application.run_polling()

if __name__ == "__main__":
    main()