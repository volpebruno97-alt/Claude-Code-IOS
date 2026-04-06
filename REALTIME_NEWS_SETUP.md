# Real-Time News Agent Setup Guide

**Get breaking news alerts INSTANTLY. Analyze impact in seconds. Stay ahead of the market.** 📰⚡

---

## Overview

The **AGENT-REALTIME-NEWS** workflow:

1. **Receives** breaking news via webhook (real-time)
2. **Extracts** ticker, headline, sentiment
3. **Checks** if ticker is in your portfolio
4. **Analyzes** using Claude AI (impact assessment)
5. **Generates** priority alerts
6. **Sends** via Telegram immediately
7. **Optionally** executes trades automatically
8. **Logs** everything to database

```
Breaking News Published
     ↓
Polygon.io/NewsAPI Webhook Fired
     ↓
Extract Ticker & Sentiment
     ↓
Check Your Portfolio
     ↓
Claude AI: Impact Analysis
     ↓
Generate Alert Score
     ↓
🚨 Telegram Alert
     ↓
Optional: Auto-Trade
     ↓
Log to Database
```

---

## Step 1: Choose Your News Source API

### Option A: Polygon.io (RECOMMENDED) ⭐

**Why:** Ultra-fast real-time news, webhooks support, professional tier

**Setup:**
1. Sign up: https://polygon.io
2. Start free trial (7 days)
3. Get API key from dashboard
4. Enable "News" webhook in settings
5. Webhook URL: `http://your-n8n-ip:5678/hook/realtime-news-webhook`

**Pricing:**
- Free: Limited (~100 requests/day)
- **Starter: £15/month** - Recommended for you
- Professional: £99+/month

**Add to `.env`:**
```
POLYGON_API_KEY=your_key_here
POLYGON_WEBHOOK_SECRET=your_secret
NEWS_API_SOURCE=polygon
```

---

### Option B: NewsAPI.org

**Why:** Good coverage, affordable, easy to set up

**Setup:**
1. Sign up: https://newsapi.org
2. Get API key
3. Use N8N's polling instead of webhooks (every 1-5 minutes)

**Pricing:**
- Free: 100 requests/day
- Developer: £10/month (1000/day)
- Business: From £25/month

**Add to `.env`:**
```
NEWS_API_KEY=your_key_here
NEWS_API_SOURCE=newsapi
```

---

### Option C: Finnhub Premium (Upgrade)

**Why:** You already use Finnhub, easier integration

**Setup:**
1. Upgrade Finnhub account to Premium
2. Enable real-time news webhooks
3. Get API key (already have it)

**Pricing:** £10-200/month (depends on tier)

**Already in `.env`:**
```
FINNHUB_API_KEY=existing_key
```

---

## Step 2: Configure N8N Environment Variables

Add these to your N8N `.env` file:

```bash
# News API
NEWS_API_SOURCE=polygon  # or newsapi, finnhub
POLYGON_API_KEY=your_polygon_key
POLYGON_WEBHOOK_SECRET=your_secret
NEWS_API_KEY=your_newsapi_key

# Trading
TRADING212_API_KEY=existing_key

# AI Analysis
ANTHROPIC_API_KEY=existing_key

# Telegram
TELEGRAM_BOT_TOKEN=existing_token
TELEGRAM_USER_ID=your_user_id_here  # NEW: Your personal chat ID

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_assistant
DB_USER=datacentre
DB_PASSWORD=your_password

# Optional: Auto-Trading
AUTO_TRADE_ENABLED=false  # Set to true only if you want auto-trades
AUTO_TRADE_QUANTITY=1     # How many shares to auto-buy
AUTO_TRADE_MAX_DAILY=5    # Max trades per day (safety limit)
```

---

## Step 3: Get Your Telegram User ID

Send a message to your bot, then run:

```bash
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

Look for `"id": 123456789` in the response. Add to `.env`:

```
TELEGRAM_USER_ID=123456789
```

---

## Step 4: Import the Workflow

1. **Download:** `agent-realtime-news.json`
2. **Open N8N:** http://localhost:5678 (or your Raspberry Pi IP)
3. **Import:**
   - Click **"+"**
   - Click **three dots menu**
   - Select **"Import from file"**
   - Choose `agent-realtime-news.json`
4. **Configure:**
   - Check all webhook URLs are correct
   - Verify all environment variables are set
5. **Activate:** Click **"Activate"** button

---

## Step 5: Test the Workflow

### Manual Test (No API needed)

1. Get your webhook URL from N8N (should show in the trigger node)
2. Send test data via curl:

```bash
curl -X POST http://localhost:5678/hook/realtime-news-webhook \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "AAPL",
    "title": "Apple Secures $50B Government Contract",
    "summary": "Apple wins major defense contract",
    "source": "Reuters",
    "url": "https://example.com",
    "sentiment": "positive"
  }'
```

3. Check Telegram - you should receive an alert!

### Real API Test (With Polygon.io)

1. Wait for real breaking news
2. System receives webhook automatically
3. Get instant Telegram alert
4. Check database logs

---

## Step 6: Configure Auto-Trading (Optional)

⚠️ **Warning:** Only enable if you're confident in automated trading

```bash
# In .env
AUTO_TRADE_ENABLED=true
AUTO_TRADE_QUANTITY=1      # Buy 1 share on bullish news
AUTO_TRADE_MAX_DAILY=5     # Max 5 trades per day
AUTO_TRADE_MIN_CONFIDENCE=80  # Only if Claude is 80%+ confident
```

**Safety Features:**
- Maximum daily trade limit
- Only trades on HIGH confidence signals
- Still requires manual approval (set to false by default)
- Logs all auto-trades to database
- Telegram alerts BEFORE executing

---

## Node-by-Node Breakdown

| Node | Function | Critical |
|------|----------|----------|
| News Webhook Trigger | Receives real-time news | ✅ Yes |
| Parse News | Extracts ticker, headline, sentiment | ✅ Yes |
| Get Your Portfolio | Fetches your current holdings | ✅ Yes |
| Check Portfolio | Determines if news is relevant to YOU | ✅ Yes |
| Claude AI Analysis | Analyzes impact (BULLISH/BEARISH/HOLD) | ✅ Yes |
| Extract Analysis | Parses Claude's recommendation | ✅ Yes |
| Format Alert | Creates readable Telegram message | ⚠️ Important |
| Send Telegram Alert | **Your instant notification** | ✅ Yes |
| Auto-Trade Check | Decides if trade should execute | ⚠️ Optional |
| Execute Trade | Places order automatically | ⚠️ Optional |
| Log to Database | Records everything for history | ⚠️ Important |

---

## Database Schema

Create this table for logging:

```sql
CREATE TABLE news_alerts (
  id SERIAL PRIMARY KEY,
  ticker VARCHAR(10),
  title TEXT,
  impact VARCHAR(20),        -- BULLISH/BEARISH/NEUTRAL
  recommendation VARCHAR(20), -- BUY/SELL/HOLD/MONITOR
  risk_level VARCHAR(20),     -- LOW/MEDIUM/HIGH
  in_portfolio BOOLEAN,
  analysis TEXT,
  auto_traded BOOLEAN,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_ticker ON news_alerts(ticker);
CREATE INDEX idx_created_at ON news_alerts(created_at);
```

---

## Alert Priority System

### 🚨 CRITICAL (Portfolio + Bullish News)
- You own this stock
- News is BULLISH
- High confidence signal
- **Action:** Immediate attention, consider buying more

### ⚠️ HIGH (Breaking news, not in portfolio)
- You DON'T own this stock
- But it's a major market mover
- Could affect your other holdings
- **Action:** Monitor for opportunity

### ➡️ MEDIUM (Neutral news)
- Mixed signal
- Could go either way
- **Action:** Watch closely

---

## Example Alert

```
🚨 BREAKING NEWS ALERT

📈 BULLISH | BUY MORE

Ticker: AAPL
Title: Apple Secures $50B Government Contract

📊 Analysis:
This is BULLISH with 85% confidence. Government contracts 
provide stable revenue streams. Expected impact: +3-5% 
stock price movement over 30 days. Recommend buying more 
if price pulls back within next 2 hours.

Source: Reuters
🔗 Read: https://reuters.com/...

Risk Level: LOW
Portfolio Position: 50 shares (£7,500)
```

---

## Troubleshooting

### No alerts coming through?

1. **Check webhook URL** - Verify in N8N node settings
2. **Check API key** - Ensure POLYGON_API_KEY is set correctly
3. **Check Telegram** - Verify TELEGRAM_USER_ID is correct
4. **Check logs** - Look at N8N execution logs for errors
5. **Test manually** - Use curl command above to test

### Alerts coming too frequently?

1. Add debounce: Configure in "Parse News" node
2. Filter by relevance score: Only alert if score > 0.6
3. Filter by time: Skip alerts outside market hours

### Database not logging?

1. Check PostgreSQL connection string
2. Verify table exists (run SQL above)
3. Check logs for SQL errors
4. Verify DB_PASSWORD is correct

---

## Next Steps

1. **Choose your API** (Polygon.io recommended)
2. **Sign up for trial/account**
3. **Get API key**
4. **Add to `.env`**
5. **Import workflow**
6. **Test with curl**
7. **Activate**
8. **Monitor Telegram for alerts!**

---

## Monitoring Dashboard (Optional)

Query your news alerts:

```sql
-- Most bullish news today
SELECT ticker, COUNT(*) as count, 
       ROUND(AVG(CASE WHEN impact = 'BULLISH' THEN 1 ELSE 0 END)*100, 2) as bullish_pct
FROM news_alerts
WHERE created_at > NOW() - INTERVAL '1 day'
GROUP BY ticker
ORDER BY bullish_pct DESC;

-- Trading alerts vs portfolio holdings
SELECT ticker, in_portfolio, recommendation, COUNT(*) as count
FROM news_alerts
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY ticker, in_portfolio, recommendation;
```

---

**You're now set up for real-time market intelligence!** 🎯

Questions? Check your N8N logs or test with the curl command.
