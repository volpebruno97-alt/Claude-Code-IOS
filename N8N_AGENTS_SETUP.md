# N8N Sub-Agents Setup Guide

**All n8n workflow JSON files ready to import into your Raspberry Pi 5 data centre!**

---

## 📋 Agent Registry & Files

### **TIER 1: CORE AGENTS** (Import First)

#### **1. AGENT-TELEGRAM-GATEWAY**
**File:** `agent-telegram-gateway.json`  
**Purpose:** User interface & message router  
**What it does:**
- Receives Telegram messages from users
- Parses incoming requests
- Routes to Main Orchestrator
- Sends responses back to Telegram
- Logs all messages to database

**Import Order:** #1 (First)

**Environment Variables Needed:**
```
TELEGRAM_BOT_TOKEN
DATABASE_URL
```

---

#### **2. AGENT-MAIN-ORCHESTRATOR**
**File:** `agent-main-orchestrator.json`  
**Purpose:** Request routing & agent coordination  
**What it does:**
- Analyzes user intent from messages
- Determines which sub-agents are needed
- Routes requests to relevant agents
- Synthesizes responses from multiple agents
- Logs orchestration decisions

**Import Order:** #2 (Second)

**Environment Variables Needed:**
```
ANTHROPIC_API_KEY
DATABASE_URL
```

**Depends On:**
- AGENT-TELEGRAM-GATEWAY

---

### **TIER 2: TRADING AGENTS** (Import Second)

#### **3. AGENT-TRADING212**
**File:** `agent-trading212.json`  
**Purpose:** Brokerage operations  
**What it does:**
- Get account balance
- View current holdings
- Place buy/sell orders
- Get transaction history
- Execute trades

**Import Order:** #3

**Environment Variables Needed:**
```
TRADING212_API_KEY
TRADING212_ACCOUNT_ID
DATABASE_URL
```

**Depends On:**
- AGENT-MAIN-ORCHESTRATOR

**Features:**
- ✅ Buy orders
- ✅ Sell orders
- ✅ Balance checks
- ✅ Holdings view
- ✅ Trade logging

---

#### **4. AGENT-TECHNICAL-ANALYSIS**
**File:** `agent-technical-analysis.json`  
**Purpose:** Technical indicators & predictions  
**What it does:**
- Fetch historical price data
- Calculate RSI, EMA, MACD, Bollinger Bands
- Identify technical patterns
- Generate buy/sell signals
- Predict future prices using Claude AI

**Import Order:** #4

**Environment Variables Needed:**
```
ALPHA_VANTAGE_KEY
ANTHROPIC_API_KEY
DATABASE_URL
```

**Depends On:**
- Python technical analysis service (localhost:5680)

**Features:**
- ✅ RSI calculations
- ✅ EMA calculations
- ✅ MACD analysis
- ✅ Bollinger Bands
- ✅ AI price predictions
- ✅ Signal generation

---

#### **5. AGENT-MARKET-DATA**
**File:** `agent-market-data.json`  
**Purpose:** Real-time & historical market data  
**What it does:**
- Fetch current stock prices
- Get 52-week highs/lows
- Retrieve market news
- Get volume & market cap data
- Cache data in database

**Import Order:** #5

**Environment Variables Needed:**
```
ALPHA_VANTAGE_KEY
FINNHUB_API_KEY
DATABASE_URL
```

**Features:**
- ✅ Real-time quotes
- ✅ Historical data
- ✅ News aggregation
- ✅ Market statistics
- ✅ Caching layer

---

#### **6. AGENT-PORTFOLIO-MANAGER**
**File:** `agent-portfolio-manager.json`  
**Purpose:** Portfolio analysis & optimization  
**What it does:**
- View all holdings
- Calculate portfolio allocation
- Assess portfolio risk
- Provide rebalancing suggestions
- Track performance

**Import Order:** #6

**Environment Variables Needed:**
```
TRADING212_API_KEY
ANTHROPIC_API_KEY
DATABASE_URL
```

**Depends On:**
- AGENT-TRADING212
- AGENT-MARKET-DATA

**Features:**
- ✅ Allocation analysis
- ✅ Risk scoring
- ✅ Performance tracking
- ✅ AI recommendations
- ✅ Snapshot saving

---

### **TIER 3: DATA & MANAGEMENT AGENTS** (Import Last)

#### **7. AGENT-FILE-MANAGER**
**File:** `Not yet created` (Template ready)  
**Purpose:** Document & file operations

#### **8. AGENT-FINANCE-TRACKER**
**File:** `Not yet created` (Template ready)  
**Purpose:** Budget & expense tracking

#### **9. AGENT-RESEARCH**
**File:** `Not yet created` (Template ready)  
**Purpose:** Company & market research

---

## 🚀 How to Import Agents into N8N

### Step 1: Access N8N Dashboard
```bash
# On your Raspberry Pi
n8n start

# Then open browser
http://raspberry-pi-ip:5678
```

### Step 2: Import Each Agent

**For each agent:**
1. Click **"+"** or **"New Workflow"**
2. Click **three dots menu** (top right)
3. Select **"Import from file"**
4. Choose the JSON file
5. Click **"Import"**
6. Click **"Activate"** to enable

### Step 3: Import Order

**MUST import in this exact order:**

```
1. agent-telegram-gateway.json
2. agent-main-orchestrator.json
3. agent-trading212.json
4. agent-technical-analysis.json
5. agent-market-data.json
6. agent-portfolio-manager.json
```

---

## 🔐 Environment Variables Setup

### Create `.env.agents` on Raspberry Pi:

```bash
# Core
ANTHROPIC_API_KEY=sk-ant-api03-pid4-...
TELEGRAM_BOT_TOKEN=8673730056:AAGbysiHPkBCE6mEi1C5HP8i7kVjWcwXwZo

# Trading
TRADING212_API_KEY=your_trading212_key
TRADING212_ACCOUNT_ID=your_account_id

# Market Data
ALPHA_VANTAGE_KEY=your_alpha_vantage_key
FINNHUB_API_KEY=your_finnhub_key
POLYGON_API_KEY=your_polygon_key

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_assistant
DB_USER=datacentre
DB_PASSWORD=your_secure_password

# Storage
STORAGE_PATH=/mnt/data
BACKUP_PATH=/mnt/data/backups
```

### Load in N8N:
1. Go to N8N Settings
2. Click "Variables"
3. Add each variable
4. Save

---

## 📊 Workflow Communication

### Message Flow:
```
User → Telegram
    ↓
AGENT-TELEGRAM-GATEWAY
    ↓
AGENT-MAIN-ORCHESTRATOR
    ↓
Required Sub-Agents:
    ├─ AGENT-TRADING212
    ├─ AGENT-TECHNICAL-ANALYSIS
    ├─ AGENT-MARKET-DATA
    └─ AGENT-PORTFOLIO-MANAGER
    ↓
AGENT-MAIN-ORCHESTRATOR (Synthesize)
    ↓
AGENT-TELEGRAM-GATEWAY
    ↓
User ← Response
```

---

## ✅ Testing Checklist

### After Importing Each Agent:

- [ ] Agent imports without errors
- [ ] Environment variables are set
- [ ] Agent appears in dashboard
- [ ] "Activate" button is available
- [ ] Test webhook endpoint responds

### After Activating All Agents:

- [ ] Send `/start` to Telegram bot
- [ ] Test: "What's my balance?"
- [ ] Test: "Buy 5 TSLA"
- [ ] Test: "Analyze AAPL"
- [ ] Test: "Show my portfolio"
- [ ] Check database logs

---

## 🐛 Troubleshooting

### Agent Won't Activate
**Solution:** Check environment variables in N8N Settings

### Telegram Bot Not Responding
**Solution:** Verify TELEGRAM_BOT_TOKEN is correct in variables

### Trading212 API Errors
**Solution:** Verify API key has correct permissions

### Database Connection Failed
**Solution:** Ensure PostgreSQL is running on Raspberry Pi

### Webhook Errors
**Solution:** Check that agent URLs are correct (use localhost for internal communication)

---

## 📈 Next Steps

1. **Import & Test Core Agents** (This Week)
   - AGENT-TELEGRAM-GATEWAY
   - AGENT-MAIN-ORCHESTRATOR

2. **Add Trading Agents** (Week 2)
   - AGENT-TRADING212
   - AGENT-TECHNICAL-ANALYSIS
   - AGENT-MARKET-DATA
   - AGENT-PORTFOLIO-MANAGER

3. **Add Management Agents** (Week 3)
   - AGENT-FILE-MANAGER
   - AGENT-FINANCE-TRACKER
   - AGENT-RESEARCH

4. **Full System Testing** (Week 4)
   - Multi-agent workflows
   - Error handling
   - Performance optimization

---

## 💾 All Files Location

```
/home/user/Claude-Code-IOS/n8n-workflows/
├── agent-telegram-gateway.json
├── agent-main-orchestrator.json
├── agent-trading212.json
├── agent-technical-analysis.json
├── agent-market-data.json
├── agent-portfolio-manager.json
└── [More agents coming...]
```

---

## 🎯 Agent System Benefits

✅ **Modular** - Each agent is independent  
✅ **Scalable** - Add new agents easily  
✅ **Reliable** - One failure doesn't crash all  
✅ **Maintainable** - Easy to update/fix  
✅ **Parallel** - Agents run concurrently  
✅ **Monitored** - Each agent has logging  

---

**Ready to set up your multi-agent system!** 🚀

