import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from anthropic import Anthropic

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Store conversations per user
user_conversations = {}

# Initialize Anthropic client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

client = Anthropic(api_key=api_key)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command - initialize conversation"""
    user_id = update.effective_user.id
    user_conversations[user_id] = []

    await update.message.reply_text(
        "👋 Welcome to Claude Code!\n\n"
        "I'm an AI assistant powered by Claude. Send me any message and I'll respond!\n\n"
        "Commands:\n"
        "/clear - Clear conversation history\n"
        "/help - Show this message"
    )
    logger.info(f"User {user_id} started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = (
        "📚 Claude Code Bot Help\n\n"
        "Just send me any message and I'll respond using Claude AI.\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/clear - Clear your conversation history\n"
        "/help - Show this help message\n\n"
        "I can help with:\n"
        "• General questions\n"
        "• Code explanations\n"
        "• Writing assistance\n"
        "• Problem solving\n"
        "• And much more!"
    )
    await update.message.reply_text(help_text)


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear conversation history"""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    await update.message.reply_text("✅ Conversation history cleared!")
    logger.info(f"User {user_id} cleared conversation")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    user_id = update.effective_user.id
    user_message = update.message.text

    # Initialize conversation if needed
    if user_id not in user_conversations:
        user_conversations[user_id] = []

    # Show typing indicator
    await update.message.chat.send_action("typing")

    try:
        # Add user message to history
        user_conversations[user_id].append({
            "role": "user",
            "content": user_message
        })

        # Get response from Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=user_conversations[user_id],
        )

        # Extract response text
        assistant_message = response.content[0].text

        # Add to conversation history
        user_conversations[user_id].append({
            "role": "assistant",
            "content": assistant_message
        })

        # Keep only last 20 messages to save memory
        if len(user_conversations[user_id]) > 20:
            user_conversations[user_id] = user_conversations[user_id][-20:]

        # Send response (split if too long)
        if len(assistant_message) > 4096:
            # Telegram has a 4096 character limit
            parts = [assistant_message[i:i+4096] for i in range(0, len(assistant_message), 4096)]
            for part in parts:
                await update.message.reply_text(part)
        else:
            await update.message.reply_text(assistant_message)

        logger.info(f"User {user_id} sent: {user_message[:50]}...")

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        await update.message.reply_text(error_msg)
        logger.error(f"Error processing message for user {user_id}: {str(e)}")


def main():
    """Start the bot"""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

    # Create the Application
    application = Application.builder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    logger.info("Starting Telegram bot...")
    application.run_polling()


if __name__ == "__main__":
    main()
