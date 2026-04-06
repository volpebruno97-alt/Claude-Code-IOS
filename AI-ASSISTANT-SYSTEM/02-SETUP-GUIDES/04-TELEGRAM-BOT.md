# Telegram Bot Setup Guide

Run Claude AI directly from Telegram on any device! 📱

## Step 1: Create a Telegram Bot

1. **Open Telegram** and search for `@BotFather`
2. **Start the chat** and send: `/start`
3. **Create a new bot** by sending: `/newbot`
4. **Follow the prompts:**
   - Bot name: `Claude Code` (or whatever you want)
   - Bot username: `your_username_bot` (must be unique, like `myname_claude_bot`)
5. **Copy your bot token** - it looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

## Step 2: Configure Your Backend

1. **Edit your `.env` file** in the `backend` folder:
   ```
   ANTHROPIC_API_KEY=sk-your-key
   TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   ```

2. **Update dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Step 3: Run the Bot

### Option A: Run Flask Backend + Telegram Bot Together

1. **Open a terminal** in the `backend` folder
2. **Activate the virtual environment:**
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Start the Telegram bot** (this will run indefinitely):
   ```bash
   python telegram_bot.py
   ```

   You should see:
   ```
   INFO:telegram.ext._application:Starting Telegram bot...
   ```

That's it! The bot is now running and listening for messages.

### Option B: Run Both HTTP API and Telegram Bot

If you want both the REST API (for mobile apps) and Telegram bot running:

1. **Start the Flask API** in one terminal:
   ```bash
   python main.py
   ```

2. **Start the Telegram bot** in another terminal:
   ```bash
   python telegram_bot.py
   ```

Both will run simultaneously!

## Step 4: Test Your Bot

1. **Search for your bot in Telegram:**
   - Find `@your_username_bot` in Telegram search
   - Click the result

2. **Send `/start`** to initialize

3. **Send a test message:**
   ```
   Hello Claude! What is 2+2?
   ```

4. **Watch Claude respond!** 🎉

## Available Commands

- `/start` - Initialize the bot
- `/help` - Show help message
- `/clear` - Clear conversation history

## Features

✅ **Works on iPhone, Android, Web, Desktop**
✅ **Persistent conversation history** (per user)
✅ **Automatic typing indicator**
✅ **Handles long responses** (auto-splits if > 4096 chars)
✅ **Multi-user support** (different conversations per user)
✅ **Memory efficient** (keeps only last 20 messages)

## Troubleshooting

### "TELEGRAM_BOT_TOKEN not set"
- Make sure you added it to your `.env` file
- Restart the bot after editing `.env`

### Bot doesn't respond
- Check that `python telegram_bot.py` is running
- Make sure your token is correct
- Verify internet connection

### "Connection refused"
- Make sure you're not blocking Telegram's servers
- Try restarting the bot

### Bot responds slowly
- Check your internet connection
- May be slow the first time (API initialization)
- Usually responds within 2-5 seconds

## Keep Bot Running (Optional)

To keep the bot running 24/7, you can:

### On Windows
Use a task scheduler or service like:
- [NSSM](https://nssm.cc/download) - Run Python as Windows Service
- Task Scheduler - Run on startup

### On Mac/Linux
Use systemd or create a launch script

### Cloud Solutions
Deploy to:
- [Heroku](https://www.heroku.com/) (free tier available)
- [Railway](https://railway.app/)
- [Replit](https://replit.com/)
- AWS, Google Cloud, Azure

## Next Steps

- Share your bot username with friends!
- They can find it and start chatting: `@your_username_bot`
- Each user has their own conversation history
- Customize responses in `telegram_bot.py`

## Need Help?

Check logs for errors:
```bash
python telegram_bot.py  # Logs will appear here
```

Common issues are usually:
1. Wrong token
2. Missing ANTHROPIC_API_KEY
3. Internet/firewall blocking Telegram
