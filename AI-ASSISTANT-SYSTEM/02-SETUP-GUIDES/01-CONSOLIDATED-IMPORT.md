# N8N Single-File Import Guide

**Import Everything in ONE JSON File!**

---

## 📥 Quick Download

**File:** `agent-complete-system.json`  
**Location:** `/n8n-workflows/agent-complete-system.json`  
**Size:** ~45 KB  
**Status:** ✅ Ready to import

This single file contains:
- ✅ Telegram Gateway (message parsing & routing)
- ✅ Intent Analyzer (determines what the user needs)
- ✅ Trading Agent (buy/sell orders, balance, holdings)
- ✅ Technical Analysis Agent (RSI, EMA, MACD, Claude predictions)
- ✅ Market Data Agent (prices, news, statistics)
- ✅ Portfolio Manager (analysis, risk scoring, AI recommendations)

---

## 🚀 How to Import (3 Steps)

### Step 1: Download
Copy the raw file from GitHub:
```
https://raw.githubusercontent.com/volpebruno97-alt/Claude-Code-IOS/claude/initial-setup-fQu8Y/n8n-workflows/agent-complete-system.json
```

Or navigate to `/n8n-workflows/` folder and download `agent-complete-system.json`

### Step 2: Open N8N
```
http://localhost:5678
or
http://raspberry-pi-ip:5678
```

### Step 3: Import
1. Click **"+"** or **"New Workflow"**
2. Click **three dots menu** (top right)
3. Select **"Import from file"**
4. Choose `agent-complete-system.json`
5. Click **"Import"**
6. Click **"Activate"**

---

## ⚙️ Required Configuration

Before activating, add these environment variables to N8N:

```
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=8673730056:AAGbysiHPkBCE6mEi1C5HP8i7kVjWcwXwZo
TRADING212_API_KEY=your_key
TRADING212_ACCOUNT_ID=your_account
ALPHA_VANTAGE_KEY=your_key
FINNHUB_API_KEY=your_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_assistant
DB_USER=datacentre
DB_PASSWORD=your_password
```

---

## 📊 Workflow Structure

```
User Message (Telegram)
         ↓
Parse Message
         ↓
Analyze Intent
         ↓
Route by Intent
    ↙  ↓  ↙  ↓  ↙
 TRADING ANALYSIS MARKET PORTFOLIO
         ↓
Synthesize Response
         ↓
Send Telegram Response
         ↓
Log All Activity
```

---

## ✅ Testing

After import and activation:

1. **Test Trading:**
   - Send: "What's my balance?"
   - Should return account info

2. **Test Analysis:**
   - Send: "Analyze AAPL"
   - Should return technical analysis with indicators

3. **Test Market:**
   - Send: "Show TSLA price"
   - Should return market data

4. **Test Portfolio:**
   - Send: "Show my portfolio"
   - Should return portfolio analysis

5. **Test Logs:**
   - Check PostgreSQL database
   - Table: `system_logs`

---

## 🎯 Key Advantages

✅ **Single Import** - One file instead of 6  
✅ **All Connected** - Agents already linked  
✅ **Production Ready** - No configuration needed in JSON  
✅ **Easy to Manage** - One workflow to monitor  
✅ **Scalable** - Can add more branches easily  

---

## 🔧 Nodes Included

| Node | Type | Purpose |
|------|------|---------|
| Telegram Trigger | Webhook | Receive messages |
| Parse Message | Code | Extract user info |
| Analyze Intent | Code | Determine intent |
| Route by Intent | Switch | Branch logic |
| Trading Nodes | HTTP | Trading212 API |
| Analysis Nodes | HTTP | Alpha Vantage + Claude |
| Market Nodes | HTTP | Finnhub + Alpha Vantage |
| Portfolio Nodes | HTTP | Trading212 API + Claude |
| Synthesize Response | Code | Format output |
| Send Response | HTTP | Telegram API |
| Log All Activity | PostgreSQL | Database storage |

**Total Nodes:** 25  
**Total Connections:** 35+

---

## 📋 Still Need Individual Files?

If you prefer to keep the individual workflow files for modularity:

- `agent-telegram-gateway.json` - Just the gateway
- `agent-main-orchestrator.json` - Just the orchestrator
- `agent-trading212.json` - Just trading
- `agent-technical-analysis.json` - Just analysis
- `agent-market-data.json` - Just market data
- `agent-portfolio-manager.json` - Just portfolio

All 6 files are still available in `/n8n-workflows/` folder.

---

**Everything is ready. Choose whichever format works best for you!** 🎉
