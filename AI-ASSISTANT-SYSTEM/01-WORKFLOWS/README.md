# 🔄 N8N Workflows

All workflow JSON files ready to import into N8N.

---

## 📁 What's Here

### Consolidated Workflows (Recommended)

**`agent-complete-system.json`** (45 KB)
- ✅ All 6 agents in ONE file
- ✅ Single import, ready to use
- ✅ Best for getting started
- 📖 Guide: `../02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md`

**`agent-realtime-news.json`** (25 KB)
- ✅ Real-time breaking news alerts
- ✅ Portfolio-aware notifications
- ✅ Claude AI sentiment analysis
- 📖 Guide: `../02-SETUP-GUIDES/02-REALTIME-NEWS.md`

---

### Individual Agent Workflows (Modular)

Located in `individual-agents/` folder:

| File | Purpose | Nodes |
|------|---------|-------|
| `agent-telegram-gateway.json` | Message parsing & routing | 5 |
| `agent-main-orchestrator.json` | Intent analysis & agent routing | 6 |
| `agent-trading212.json` | Buy/sell orders, balance, holdings | 7 |
| `agent-technical-analysis.json` | RSI, EMA, MACD, Claude predictions | 6 |
| `agent-market-data.json` | Prices, news, market stats | 6 |
| `agent-portfolio-manager.json` | Portfolio analysis & recommendations | 7 |

**Total:** 37 nodes, 40+ connections

📖 Guide: `../02-SETUP-GUIDES/03-INDIVIDUAL-AGENTS.md`

---

## ⚡ Quick Import

### Option 1: Single File (Easiest)

```
1. Open N8N: http://localhost:5678
2. Click "+"
3. Select "Import from file"
4. Choose: agent-complete-system.json
5. Click "Activate"
6. Done! ✅
```

### Option 2: Individual Agents (Full Control)

```
1. Open N8N: http://localhost:5678
2. For each file in individual-agents/:
   a. Click "+"
   b. Select "Import from file"
   c. Choose the JSON file
   d. Click "Activate"
3. All agents now running! ✅
```

### Option 3: Real-Time News Only

```
1. Open N8N: http://localhost:5678
2. Click "+"
3. Select "Import from file"
4. Choose: agent-realtime-news.json
5. Configure with your news API key
6. Click "Activate"
```

---

## 🔧 Configuration Required

After importing, add these environment variables:

```bash
# Required for all workflows
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=123456:ABC...
TELEGRAM_USER_ID=987654321

# For trading features
TRADING212_API_KEY=your_key

# For technical analysis
ALPHA_VANTAGE_KEY=your_key

# For market data
FINNHUB_API_KEY=your_key

# For real-time news
POLYGON_API_KEY=your_key

# For database logging
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_assistant
DB_USER=datacentre
DB_PASSWORD=your_password
```

See: `../04-TEMPLATES/.env.example`

---

## 📊 Workflow Architecture

```
COMPLETE SYSTEM (agent-complete-system.json):

Telegram Input
     ↓
Parse Message
     ↓
Analyze Intent
     ↓
Route by Intent (Switch Node)
     ↙  ↓  ↙  ↓
  TRADING ANALYSIS MARKET PORTFOLIO
     ↓
Synthesize Response
     ↓
Send Telegram Alert
     ↓
Log to Database
```

```
REALTIME NEWS (agent-realtime-news.json):

Breaking News (Webhook)
     ↓
Parse News Article
     ↓
Get Your Portfolio
     ↓
Check if Relevant
     ↓
Claude AI Analysis
     ↓
Format Alert
     ↓
🚨 Send Telegram
     ↓
[Optional] Auto-Trade
     ↓
Log to Database
```

---

## ✅ Testing Your Import

### Test 1: Manual Trigger (No API needed)

```bash
curl -X POST http://localhost:5678/hook/realtime-news-webhook \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "AAPL",
    "title": "Test News",
    "summary": "This is a test",
    "source": "Test",
    "sentiment": "positive"
  }'
```

Expected: Telegram alert received

### Test 2: Telegram Message

1. Find your bot on Telegram
2. Send: "Hi"
3. Expect: Response from bot

### Test 3: Trading Query

1. Send: "What is my balance?"
2. Expect: Account balance information

### Test 4: Analysis Query

1. Send: "Analyze AAPL"
2. Expect: Technical analysis with indicators

---

## 🎯 Recommended Setup Path

### For Beginners:
1. Start with `agent-complete-system.json`
2. Test with Telegram
3. Add one API key at a time
4. Expand from there

### For Advanced Users:
1. Import individual agents
2. Customize each agent
3. Add webhooks for external triggers
4. Create additional sub-agents

### For Pro Traders:
1. Use `agent-realtime-news.json` for breaking news
2. Combine with technical analysis
3. Enable auto-trading
4. Monitor via dashboard

---

## 📈 Node Count Summary

| Workflow | Nodes | Connections | Triggers |
|----------|-------|-------------|----------|
| Complete System | 25 | 35+ | 1 (Telegram) |
| Real-Time News | 12 | 20+ | 1 (Webhook) |
| Telegram Gateway | 5 | 4 | 1 |
| Orchestrator | 6 | 5 | 1 |
| Trading | 7 | 6 | 1 |
| Analysis | 6 | 5 | 1 |
| Market Data | 6 | 5 | 1 |
| Portfolio | 7 | 6 | 1 |

---

## 🔗 Integration Points

### Incoming Data
- ✅ Telegram messages (user input)
- ✅ Webhook from Polygon.io (breaking news)
- ✅ Internal webhooks (agent-to-agent)

### Outgoing Data
- ✅ Telegram API (send alerts)
- ✅ Trading212 API (execute trades)
- ✅ Anthropic API (Claude AI)
- ✅ Alpha Vantage API (price data)
- ✅ Finnhub API (market news)
- ✅ PostgreSQL (database)

---

## 🚨 Common Issues

### "Module not found" error?
→ Check all API keys in environment variables

### "No response from bot"?
→ Verify TELEGRAM_BOT_TOKEN and TELEGRAM_USER_ID

### "Trading API error"?
→ Check TRADING212_API_KEY is valid

### "Database connection failed"?
→ Verify PostgreSQL is running and credentials are correct

See detailed troubleshooting: `../02-SETUP-GUIDES/README.md`

---

## 📚 Learn More

- **Full Architecture:** `../03-DOCUMENTATION/01-ARCHITECTURE.md`
- **Visual Layout:** `../03-DOCUMENTATION/02-VISUAL-LAYOUT.md`
- **Setup Guides:** `../02-SETUP-GUIDES/`
- **N8N Docs:** https://docs.n8n.io

---

## 🎓 Next Steps

1. **Choose your import option** (Single file recommended)
2. **Read the setup guide** for your choice
3. **Get your API keys** (see ../04-TEMPLATES/.env.example)
4. **Import the workflow**
5. **Configure environment variables**
6. **Test with Telegram**
7. **Enable additional features**

---

**Ready to import? Start here:** `../02-SETUP-GUIDES/01-CONSOLIDATED-IMPORT.md` 🚀
