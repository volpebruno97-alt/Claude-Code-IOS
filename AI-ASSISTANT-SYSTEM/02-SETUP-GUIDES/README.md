# 📚 Setup Guides

Complete step-by-step installation guides for every part of the system.

---

## 🎯 Start Here

### Choose Your Path

**I want everything in one go** → `01-CONSOLIDATED-IMPORT.md`
- Single N8N workflow with all agents
- Perfect for first-time setup
- Get started in 15 minutes

**I want real-time breaking news alerts** → `02-REALTIME-NEWS.md`
- Instant Telegram alerts for relevant news
- Portfolio-aware notifications
- Auto-trading optional
- Takes 20 minutes to setup

**I want individual agents for modularity** → `03-INDIVIDUAL-AGENTS.md`
- 6 separate workflows
- Full control over each agent
- Import in specific order
- Takes 30 minutes total

**I want to setup the Telegram bot** → `04-TELEGRAM-BOT.md`
- Configure your bot with BotFather
- Test locally on your laptop
- Link to your N8N system
- Takes 10 minutes

---

## 📖 Guide Descriptions

### 01-CONSOLIDATED-IMPORT.md (⭐ START HERE)

**Best for:** Beginners, quick setup, all-in-one solution

**What you'll do:**
1. Download `agent-complete-system.json`
2. Open N8N dashboard
3. Import the single file
4. Add environment variables
5. Test via Telegram
6. Done in 15 minutes!

**Includes:**
- System overview diagram
- Exact step-by-step instructions
- Environment variables needed
- Testing checklist
- Troubleshooting guide

**Time:** 15 minutes

---

### 02-REALTIME-NEWS.md

**Best for:** Traders, early market advantage, news alerts

**What you'll do:**
1. Choose your news API (Polygon.io recommended)
2. Sign up for API key
3. Import `agent-realtime-news.json`
4. Configure webhook from news provider
5. Test with sample news
6. Enable auto-trading (optional)

**Includes:**
- API comparison (Polygon.io vs NewsAPI vs Finnhub)
- Real-time webhook setup
- Database schema for storing alerts
- Priority alert system
- Auto-trading safety limits

**Time:** 20 minutes

---

### 03-INDIVIDUAL-AGENTS.md

**Best for:** Advanced users, modularity, customization

**What you'll do:**
1. Import 6 workflows in order
2. Configure each agent individually
3. Test each one
4. Enable inter-agent communication
5. Monitor via N8N dashboard

**Includes:**
- Import order (important!)
- Per-agent environment variables
- Testing instructions for each agent
- Debugging tips
- Performance optimization

**Time:** 30 minutes

---

### 04-TELEGRAM-BOT.md

**Best for:** Testing locally, Telegram setup, bot configuration

**What you'll do:**
1. Create bot with BotFather
2. Get bot token
3. Configure in Python (optional)
4. Test on your phone
5. Link to N8N system

**Includes:**
- BotFather step-by-step
- Python bot code (for testing)
- Token configuration
- Local testing guide
- Linking to N8N workflows

**Time:** 10 minutes

---

## 🔄 Setup Order Recommendation

```
1. Get API Keys (start immediately)
   └─ Takes 30 mins, do while reading docs
   
2. Setup Raspberry Pi (if you have it)
   └─ Install N8N, PostgreSQL, Docker
   
3. Configure Database
   └─ Run SQL schema (5 mins)
   
4. Import Workflows (choose one path)
   ├─ Path A: Consolidated (15 mins) ⭐
   ├─ Path B: Individual Agents (30 mins)
   └─ Path C: Real-Time News (20 mins)
   
5. Configure Environment Variables
   └─ Add API keys to .env (10 mins)
   
6. Test System
   └─ Send Telegram message (1 min)
   
7. Deploy to Production
   └─ Keep N8N running 24/7 (5 mins)
```

**Total Time: ~90 minutes from scratch**

---

## 📋 Quick Reference

### Files You Need

```
N8N Workflow Files:
- agent-complete-system.json (Recommended)
- agent-realtime-news.json (Optional)
- individual-agents/*.json (If you want modularity)

Configuration:
- .env.example (copy to .env)
- database-schema.sql (run once)

Documentation:
- This file!
- Each guide has detailed steps
```

### Environment Variables Template

```bash
# Core
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=123456:ABC...
TELEGRAM_USER_ID=987654321

# APIs
TRADING212_API_KEY=...
ALPHA_VANTAGE_KEY=...
FINNHUB_API_KEY=...
POLYGON_API_KEY=...

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_assistant
DB_USER=datacentre
DB_PASSWORD=...

# Optional
AUTO_TRADE_ENABLED=false
AUTO_TRADE_QUANTITY=1
```

See: `../04-TEMPLATES/.env.example`

---

## ⚠️ Prerequisites

Before you start, make sure you have:

- ✅ **N8N installed** on your Raspberry Pi
  ```bash
  npm install -g n8n
  ```

- ✅ **PostgreSQL installed**
  ```bash
  sudo apt-get install postgresql
  ```

- ✅ **API keys** (or in progress of getting them)
  - Anthropic, Telegram, Trading212, Alpha Vantage, Finnhub, Polygon.io

- ✅ **Telegram bot created**
  - Talk to @BotFather on Telegram

- ✅ **Database created**
  ```bash
  createdb ai_assistant
  ```

---

## 🆘 Troubleshooting

### General Issues

**N8N won't start?**
```bash
npm install -g n8n@latest
n8n
```

**Port 5678 already in use?**
```bash
n8n -p 5679
```

**PostgreSQL not running?**
```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
```

---

### Workflow Import Issues

**"Cannot import" error?**
1. Check file format is valid JSON
2. Try re-downloading the file
3. Check file size (should be > 5KB)
4. Check N8N version is up to date

**"Node type not found" error?**
1. N8N version might be old
2. Update: `npm install -g n8n@latest`
3. Restart N8N

---

### API & Connection Issues

**"API key invalid" error?**
1. Check key is copied exactly (no spaces)
2. Check correct key for the API
3. Verify API key hasn't expired
4. Check environment variable name matches

**"Cannot connect to database" error?**
1. Check PostgreSQL is running
2. Verify credentials in .env
3. Test manually: `psql -U datacentre -d ai_assistant`
4. Check network connection

**"Telegram not responding"?**
1. Verify TELEGRAM_BOT_TOKEN is correct
2. Verify TELEGRAM_USER_ID is correct
3. Check bot privacy settings in Telegram
4. Restart N8N

---

### Performance Issues

**System is slow?**
1. Check CPU usage: `top`
2. Check disk space: `df -h`
3. Check N8N logs for errors
4. Consider upgrading SSD

**Workflows timing out?**
1. Check API rate limits
2. Increase timeout in node settings
3. Check network speed
4. Look for stuck executions

---

## 📞 Getting Help

### Check Logs

**N8N logs:**
- N8N UI → Executions → View details
- Command line: Watch terminal

**Database logs:**
```bash
psql ai_assistant
SELECT * FROM system_logs ORDER BY created_at DESC LIMIT 20;
```

**System logs:**
```bash
journalctl -u n8n -f
```

### Resources

- **N8N Docs:** https://docs.n8n.io
- **Telegram Bot API:** https://core.telegram.org/bots/api
- **PostgreSQL Docs:** https://www.postgresql.org/docs
- **Trading212 API:** https://github.com/trading212/api

---

## ✅ Success Checklist

After setup, verify:

- [ ] N8N running on http://localhost:5678
- [ ] PostgreSQL database created
- [ ] All API keys in .env file
- [ ] Workflow imported and activated
- [ ] Telegram bot created and token added
- [ ] Test message sent to bot
- [ ] Bot responds with AI message
- [ ] Database logging working
- [ ] No errors in N8N execution logs

If all checked, you're ready to use your AI assistant! 🎉

---

## 🚀 Next Steps After Setup

1. **Send your first message** to test
2. **Monitor logs** to ensure everything works
3. **Add more API integrations** as needed
4. **Enable auto-trading** if desired
5. **Create dashboard** for monitoring
6. **Set up alerts** for critical events
7. **Backup database** regularly

---

## 📈 Implementation Timeline

- **Day 1:** Get API keys, setup hardware
- **Day 2:** Install N8N, PostgreSQL
- **Day 3:** Import workflow, configure
- **Day 4:** Test all features
- **Day 5+:** Production deployment, monitoring

---

**Ready to begin? Choose a guide above and follow the steps!** 🚀

Most popular: `01-CONSOLIDATED-IMPORT.md` ⭐
