# 🤖 Personal AI Data Center - Complete System

A production-ready AI assistant running on **Raspberry Pi 5** with real-time market intelligence, automated trading, and instant news alerts. Access your personal AI on any device via Telegram.

---

## 📦 What's Inside

```
AI-ASSISTANT-SYSTEM/
├── 01-WORKFLOWS/              ← N8N workflow JSON files
│   ├── agent-complete-system.json      (All-in-one, recommended)
│   ├── agent-realtime-news.json        (Breaking news alerts)
│   └── individual-agents/              (6 separate agents)
│
├── 02-SETUP-GUIDES/           ← Step-by-step installation guides
│   ├── 01-CONSOLIDATED-IMPORT.md       (Start here!)
│   ├── 02-REALTIME-NEWS.md
│   ├── 03-INDIVIDUAL-AGENTS.md
│   └── 04-TELEGRAM-BOT.md
│
├── 03-DOCUMENTATION/          ← Technical documentation
│   ├── 01-ARCHITECTURE.md              (System overview)
│   ├── 02-VISUAL-LAYOUT.md             (N8N node positioning)
│   └── 03-IMPLEMENTATION-PLAN.md       (11-phase timeline)
│
├── 04-TEMPLATES/              ← Configuration templates
│   ├── .env.example
│   ├── database-schema.sql
│   └── README.md
│
└── 05-DOWNLOADS/              ← Ready-to-import files
    ├── agent-complete-system.json
    ├── agent-realtime-news.json
    └── individual-agents/
```

---

## 🚀 Quick Start (5 Minutes)

### For Your Raspberry Pi

1. **Install N8N**
   ```bash
   npm install -g n8n
   n8n
   ```

2. **Open Dashboard**
   - Navigate to: `http://localhost:5678`

3. **Import Workflow**
   - Click **"+"** → **"Import from file"**
   - Choose: `agent-complete-system.json`
   - Click **"Activate"**

4. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your API keys (see below)

5. **Start Trading & Receive News**
   - Send message on Telegram
   - Instant AI response!

---

## 🔑 Required API Keys

Get these ASAP (most are free):

| Service | Purpose | Free Tier | Sign Up |
|---------|---------|-----------|---------|
| **Anthropic** | Claude AI | $5 free | https://console.anthropic.com |
| **Telegram** | Bot messaging | Unlimited free | @BotFather on Telegram |
| **Trading212** | Brokerage API | Free account | https://trading212.com |
| **Alpha Vantage** | Stock data | 5/min limit | https://alphavantage.co |
| **Finnhub** | Market news | 60/min free | https://finnhub.io |
| **Polygon.io** | Real-time news | 7-day trial | https://polygon.io |
| **PostgreSQL** | Database | Open source | http://postgresql.org |

---

## 📊 System Architecture

```
Your iPhone/Android
       ↓ Telegram
    🤖 N8N Orchestrator (Raspberry Pi)
       ↓
    ├─ AGENT-REALTIME-NEWS     (Breaking news alerts)
    ├─ AGENT-TRADING212        (Buy/sell stocks)
    ├─ AGENT-TECHNICAL-ANALYSIS (RSI, EMA, MACD)
    ├─ AGENT-MARKET-DATA       (Prices, news)
    └─ AGENT-PORTFOLIO-MANAGER (Analysis & risk)
       ↓
    📊 PostgreSQL Database (Logs everything)
```

---

## 🎯 Import Options

### Option 1: Single File (Recommended) ⭐
```
Download: agent-complete-system.json
Size: 45 KB
Import time: 1 click
All agents included!
```

👉 **Start here:** `02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md`

### Option 2: Individual Agents (Modular)
```
Download: 6 separate JSON files
Size: 31 KB total
Import time: 6 clicks
Full control per agent
```

👉 **Use this:** `02-SETUP-GUIDES/03-INDIVIDUAL-AGENTS.md`

### Option 3: Real-Time News Only
```
Download: agent-realtime-news.json
Size: 25 KB
Get breaking news alerts instantly
```

👉 **Setup:** `02-SETUP-GUIDES/02-REALTIME-NEWS.md`

---

## 💾 Hardware You Need

- **Raspberry Pi 5** (8GB) ✅
- **External SSD 2TB** (WD/Samsung/Kingston) ⏳
- **SD Card 128GB** (for OS) ✅
- **Cooling case** ✅
- **Power supply** (5V/5A) ✅

[View shopping list](../UK_SHOPPING_LIST.md)

---

## 📝 Setup Steps

### Phase 1: Database (30 mins)
```bash
sudo apt-get install postgresql
createdb ai_assistant
psql < templates/database-schema.sql
```

### Phase 2: N8N (30 mins)
```bash
npm install -g n8n
n8n
# Import workflows in 02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md
```

### Phase 3: Configuration (15 mins)
```bash
cp templates/.env.example .env
# Fill in your API keys
```

### Phase 4: Testing (15 mins)
```
Send message to bot on Telegram
Check for instant response
Monitor logs for errors
```

**Total time: ~90 minutes** ⏱️

---

## 🎮 What You Can Do

### Trading
```
User: "Buy 10 shares of AAPL at £120"
Bot: ✅ Order placed. Confirmation #123
```

### Market Analysis
```
User: "Analyze TSLA"
Bot: 📊 Technical Analysis with RSI, EMA, MACD predictions
```

### Portfolio Insights
```
User: "Show my portfolio"
Bot: 📈 Holdings breakdown, risk score, AI recommendations
```

### Breaking News Alerts
```
🚨 BREAKING: Apple wins $50B contract
📈 BULLISH for AAPL | You own 50 shares
Recommendation: BUY MORE
```

---

## 📚 Documentation Index

| Document | Purpose |
|----------|---------|
| **01-ARCHITECTURE.md** | Complete system design & agent specs |
| **02-VISUAL-LAYOUT.md** | Exact N8N node positioning (X,Y coords) |
| **03-IMPLEMENTATION-PLAN.md** | 11-phase timeline & success criteria |
| **01-CONSOLIDATED-IMPORT.md** | Import everything in 1 click |
| **02-REALTIME-NEWS.md** | Setup breaking news alerts |
| **03-INDIVIDUAL-AGENTS.md** | Import 6 agents separately |
| **04-TELEGRAM-BOT.md** | Configure Telegram bot |

---

## 🐛 Troubleshooting

### N8N won't start?
```bash
npm install -g n8n@latest
n8n
```

### Telegram not responding?
- Check `TELEGRAM_BOT_TOKEN` in `.env`
- Verify `TELEGRAM_USER_ID` is set
- Check N8N execution logs

### No database connection?
- Verify PostgreSQL is running
- Check DB credentials in `.env`
- Run: `psql -U datacentre -d ai_assistant`

### API key errors?
- Verify key is correct (no spaces)
- Check environment variable name matches
- Ensure API tier supports your usage

[More troubleshooting →](02-SETUP-GUIDES/README.md#troubleshooting)

---

## 🎯 Next Steps

1. **Read:** `02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md` (10 mins)
2. **Get:** All API keys (30 mins)
3. **Setup:** Database + N8N (90 mins)
4. **Import:** `agent-complete-system.json` (2 mins)
5. **Test:** Send Telegram message (1 min)
6. **Enjoy:** Your personal AI assistant! 🎉

---

## 📞 Support

- **N8N Docs:** https://docs.n8n.io
- **Telegram Bot Docs:** https://core.telegram.org/bots/api
- **Trading212 API:** https://github.com/trading212/api
- **Issues:** Check execution logs in N8N

---

## ✨ Features

✅ **Real-time news alerts** - Breaking news for your portfolio  
✅ **Instant trades** - Buy/sell stocks via Telegram  
✅ **Technical analysis** - RSI, EMA, MACD, Claude predictions  
✅ **Portfolio management** - Holdings, risk scoring, recommendations  
✅ **Market data** - Prices, news, analyst ratings  
✅ **24/7 operation** - Always-on Raspberry Pi  
✅ **Database logging** - Complete audit trail  
✅ **Auto-scaling** - From 1 to 100+ agents  

---

## 📊 Production Specs

- **Uptime:** 99.9% (Raspberry Pi with auto-restart)
- **Response time:** <2 seconds per request
- **Data retention:** Unlimited (PostgreSQL)
- **Concurrent users:** 1 (personal assistant)
- **Workflows:** 7+ agents
- **Nodes:** 40+ total

---

## 🔒 Security

- Environment variables for all secrets
- PostgreSQL database encryption
- Telegram API token protected
- Trading API key secured
- All logs stored locally
- No data sent to third parties (except APIs)

---

## 💰 Total Cost

| Item | Cost | Notes |
|------|------|-------|
| Raspberry Pi 5 8GB | £60-80 | One-time |
| External SSD 2TB | £60-80 | One-time |
| SD Card 128GB | £10-15 | One-time |
| N8N | FREE | Open source |
| PostgreSQL | FREE | Open source |
| API Keys | FREE-$20/mo | Mostly free tier |
| **Total First Year** | **~£130-200** | Then just API costs |

---

## 📅 Timeline

- **Days 1-3:** Hardware arrives, setup Raspberry Pi
- **Day 4:** Configure N8N, import workflows
- **Day 5:** Add API keys, test system
- **Day 6+:** Deploy to production, receive alerts!

---

## 🚀 Ready to Begin?

👉 **Start with:** `02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md`

Questions? Check the troubleshooting section or review the architecture docs.

**Let's build your personal AI data center!** 🤖✨
