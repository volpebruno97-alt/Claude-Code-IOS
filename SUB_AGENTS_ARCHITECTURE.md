# Personal AI Data Centre - Sub-Agent System Architecture

**System Overview:** Multi-agent system running on Raspberry Pi 5 with Claude as the orchestrator  
**Total Agents:** 9 specialized agents  
**Communication:** N8N workflows + Claude SDK  
**Status:** Ready to implement  

---

## 📋 Complete Agent Registry

### **TIER 1: CORE AGENTS** (Essential)

#### **1️⃣ AGENT-TELEGRAM-GATEWAY**
**Purpose:** User interface & message router  
**Responsibilities:**
- Receive Telegram messages
- Parse user intent
- Route to relevant agents
- Format & send responses back

**Inputs:**
```json
{
  "user_id": "123456789",
  "message": "Analyze my portfolio",
  "chat_id": "987654321"
}
```

**Outputs:**
```json
{
  "response": "Analysis...",
  "status": "success",
  "agents_used": ["AGENT-PORTFOLIO-MANAGER", "AGENT-MARKET-DATA"]
}
```

**Dependencies:**
- Telegram Bot Token
- Main Orchestrator Agent

**Error Handling:**
- Connection failures → Retry 3x
- Invalid messages → Send help text
- Agent timeout → Return error response

---

#### **2️⃣ AGENT-MAIN-ORCHESTRATOR**
**Purpose:** Request routing & agent coordination  
**Responsibilities:**
- Analyze user requests
- Determine required agents
- Coordinate multi-agent workflows
- Synthesize responses

**Inputs:**
```json
{
  "user_request": "Buy 10 TSLA and analyze my portfolio",
  "user_context": {"account_id": "123", "balance": "5000"}
}
```

**Outputs:**
```json
{
  "action_plan": [
    {"agent": "AGENT-TRADING212", "action": "place_trade"},
    {"agent": "AGENT-PORTFOLIO-MANAGER", "action": "analyze"}
  ],
  "final_response": "Trade executed..."
}
```

**Uses Claude Agent SDK:** YES

---

### **TIER 2: TRADING AGENTS**

#### **3️⃣ AGENT-TRADING212**
**Purpose:** Brokerage operations  
**Responsibilities:**
- Execute trades (buy/sell)
- Manage orders
- Get account balance
- View holdings
- Transaction history

**Inputs:**
```json
{
  "action": "place_trade",
  "symbol": "TSLA",
  "quantity": 10,
  "order_type": "market"
}
```

**Outputs:**
```json
{
  "order_id": "ORD123456",
  "status": "executed",
  "price": 245.50,
  "total": 2455.00
}
```

**API Endpoints:**
- Trading212 REST API
- Authentication: API Key in headers

**Error Handling:**
- Insufficient funds → Return balance
- Invalid symbol → Suggest alternatives
- API error → Fallback to cache

---

#### **4️⃣ AGENT-TECHNICAL-ANALYSIS**
**Purpose:** Technical indicators & predictions  
**Responsibilities:**
- Calculate RSI, EMA, MACD
- Identify patterns
- Generate signals
- Price predictions
- Backtesting

**Inputs:**
```json
{
  "symbol": "AAPL",
  "period": "100",
  "indicators": ["RSI", "EMA", "MACD"]
}
```

**Outputs:**
```json
{
  "symbol": "AAPL",
  "price": 185.50,
  "rsi": 72,
  "signal": "SELL",
  "prediction": "185.00",
  "confidence": 0.78
}
```

**Uses Python Libraries:**
- pandas_ta
- numpy
- scipy

---

#### **5️⃣ AGENT-MARKET-DATA**
**Purpose:** Real-time & historical market data  
**Responsibilities:**
- Fetch price data
- Get market news
- Sector performance
- Economic indicators
- Dividend data

**Inputs:**
```json
{
  "symbol": "MSFT",
  "data_type": "price_history",
  "period": "1y"
}
```

**Outputs:**
```json
{
  "symbol": "MSFT",
  "current_price": 380.50,
  "52w_high": 420.75,
  "52w_low": 220.50,
  "news": [{"title": "...", "date": "2026-04-06"}]
}
```

**Data Sources:**
- Alpha Vantage API
- Polygon.io
- Finnhub
- Yahoo Finance

---

#### **6️⃣ AGENT-PORTFOLIO-MANAGER**
**Purpose:** Portfolio analysis & optimization  
**Responsibilities:**
- View holdings
- Performance tracking
- Risk assessment
- Allocation analysis
- Rebalancing suggestions

**Inputs:**
```json
{
  "action": "analyze",
  "account_id": "123"
}
```

**Outputs:**
```json
{
  "total_value": 50000,
  "cash": 5000,
  "holdings": [
    {"symbol": "AAPL", "quantity": 10, "value": 18550}
  ],
  "allocation": {"stocks": 0.9, "cash": 0.1},
  "risk_score": 7.5
}
```

---

### **TIER 3: DATA & MANAGEMENT AGENTS**

#### **7️⃣ AGENT-FILE-MANAGER**
**Purpose:** Document & file operations  
**Responsibilities:**
- Organize documents
- Search files
- Generate reports
- Export data
- Backup management

**Inputs:**
```json
{
  "action": "search",
  "query": "trading reports",
  "type": "pdf"
}
```

**Outputs:**
```json
{
  "files": [
    {"name": "report_2026_01.pdf", "size": "2.5MB", "date": "2026-01-15"}
  ],
  "count": 5
}
```

**Storage:**
- 2TB SSD on Raspberry Pi
- PostgreSQL metadata

---

#### **8️⃣ AGENT-FINANCE-TRACKER**
**Purpose:** Personal finance management  
**Responsibilities:**
- Budget tracking
- Expense logging
- Income tracking
- Financial goals
- Tax calculations

**Inputs:**
```json
{
  "action": "log_expense",
  "amount": 150,
  "category": "food",
  "date": "2026-04-06"
}
```

**Outputs:**
```json
{
  "expense_id": "EXP123",
  "status": "logged",
  "monthly_total": 3500,
  "budget_remaining": 1500
}
```

---

#### **9️⃣ AGENT-RESEARCH**
**Purpose:** Company & market research  
**Responsibilities:**
- Company fundamentals
- Sector analysis
- Industry news
- Competitive analysis
- Report generation

**Inputs:**
```json
{
  "symbol": "TSLA",
  "research_type": "fundamentals"
}
```

**Outputs:**
```json
{
  "company": "Tesla",
  "pe_ratio": 45.5,
  "earnings_growth": 0.15,
  "analysis": "Growth stock with moderate valuation..."
}
```

---

## 🔗 Agent Communication Map

```
User Message (Telegram)
        ↓
AGENT-TELEGRAM-GATEWAY
        ↓
AGENT-MAIN-ORCHESTRATOR (Claude decides)
        ↓
Route to relevant agents:
├─ AGENT-TRADING212
├─ AGENT-TECHNICAL-ANALYSIS
├─ AGENT-MARKET-DATA
├─ AGENT-PORTFOLIO-MANAGER
├─ AGENT-FILE-MANAGER
├─ AGENT-FINANCE-TRACKER
└─ AGENT-RESEARCH
        ↓
Collect results
        ↓
AGENT-MAIN-ORCHESTRATOR (Synthesize)
        ↓
AGENT-TELEGRAM-GATEWAY
        ↓
Send to User
```

---

## 📁 File Structure

```
Raspberry Pi Data Centre
│
├── agents/
│   ├── agent-telegram-gateway.json
│   ├── agent-main-orchestrator.json
│   ├── agent-trading212.json
│   ├── agent-technical-analysis.json
│   ├── agent-market-data.json
│   ├── agent-portfolio-manager.json
│   ├── agent-file-manager.json
│   ├── agent-finance-tracker.json
│   └── agent-research.json
│
├── config/
│   ├── agents-config.yaml
│   ├── .env.agents
│   └── agent-dependencies.json
│
└── data/
    ├── conversation-logs/
    ├── technical-analysis/
    └── portfolio-data/
```

---

## 🔐 Environment Variables Required

### **Global (.env.agents)**
```
ANTHROPIC_API_KEY=sk-ant-...
TELEGRAM_BOT_TOKEN=8673730056:AAGbysiHPkBCE6mEi1C5HP8i7kVjWcwXwZo
DATABASE_URL=postgresql://user:pass@localhost:5432/ai_assistant

# Trading
TRADING212_API_KEY=your_api_key
TRADING212_ACCOUNT_ID=your_account_id

# Market Data
ALPHA_VANTAGE_KEY=your_key
POLYGON_API_KEY=your_key
FINNHUB_API_KEY=your_key

# Database
DB_HOST=localhost
DB_USER=datacentre
DB_PASSWORD=your_password
DB_NAME=ai_assistant

# Storage
STORAGE_PATH=/mnt/data
BACKUP_PATH=/mnt/data/backups
```

---

## 🚀 Implementation Order

### Phase 1: Foundation (Week 1)
1. ✅ AGENT-TELEGRAM-GATEWAY (user interface)
2. ✅ AGENT-MAIN-ORCHESTRATOR (routing)
3. ✅ Agent communication protocol

### Phase 2: Trading (Week 2)
4. ✅ AGENT-TRADING212
5. ✅ AGENT-PORTFOLIO-MANAGER
6. ✅ AGENT-MARKET-DATA

### Phase 3: Analysis (Week 3)
7. ✅ AGENT-TECHNICAL-ANALYSIS
8. ✅ AGENT-RESEARCH

### Phase 4: Management (Week 4)
9. ✅ AGENT-FILE-MANAGER
10. ✅ AGENT-FINANCE-TRACKER

### Phase 5: Integration (Week 5)
11. ✅ Full system testing
12. ✅ Deployment to Raspberry Pi

---

## 📊 Agent Dependencies

```
AGENT-MAIN-ORCHESTRATOR
├── Claude SDK
├── Message Router
└── Response Synthesizer

AGENT-TELEGRAM-GATEWAY
├── Telegram Bot API
└── AGENT-MAIN-ORCHESTRATOR

AGENT-TRADING212
├── Trading212 API
├── PostgreSQL (order logging)
└── AGENT-PORTFOLIO-MANAGER (for context)

AGENT-TECHNICAL-ANALYSIS
├── pandas_ta (calculations)
├── Historical price data
└── AGENT-MARKET-DATA

AGENT-MARKET-DATA
├── Multiple API sources
└── Cache system (Redis optional)

AGENT-PORTFOLIO-MANAGER
├── AGENT-TRADING212 (holdings)
├── AGENT-MARKET-DATA (prices)
└── PostgreSQL (history)

AGENT-FILE-MANAGER
├── 2TB SSD storage
└── PostgreSQL metadata

AGENT-FINANCE-TRACKER
└── PostgreSQL (transactions)

AGENT-RESEARCH
└── Multiple data sources
```

---

## 💬 Example Workflow

### User Request:
```
"I want to buy 5 Tesla shares if the technical analysis 
looks good and then show me my portfolio"
```

### Orchestrator Actions:
```
1. Parse intent:
   - Trading action needed
   - Technical analysis needed
   - Portfolio view needed

2. Activate agents:
   a) AGENT-MARKET-DATA
      └─ Get TSLA price history
   
   b) AGENT-TECHNICAL-ANALYSIS
      └─ Calculate RSI, EMA, MACD
      └─ Generate signal
   
   c) If signal = BUY:
      └─ AGENT-TRADING212
         └─ Place order for 5 shares
   
   d) AGENT-PORTFOLIO-MANAGER
      └─ Analyze new portfolio

3. Synthesize response:
   "Based on technical analysis (RSI=68, EMA bullish),
    I bought 5 TSLA @ $245.50.
    
    Your new portfolio:
    - Total value: $52,277.50
    - Allocation: 92% stocks, 8% cash
    - Risk score: 7.8/10"
```

---

## ✅ Next Steps

1. Create n8n workflow JSON for each agent
2. Set up environment variables
3. Configure agent communication
4. Deploy to Raspberry Pi
5. Test each agent independently
6. Test multi-agent workflows
7. Monitor & optimize

---

**This is a production-grade, scalable architecture!** 🚀

