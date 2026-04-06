# 🔧 Configuration Templates

Configuration files and templates for setting up your system.

---

## 📁 Files in This Folder

### `.env.example`
**Environment variables template**

Copy to `.env` and fill in your values:

```bash
cp .env.example .env
```

Then edit `.env` with your actual API keys and credentials.

**Never commit `.env` to git!** It contains sensitive data.

---

### `database-schema.sql`
**PostgreSQL database schema**

Creates all necessary tables for logging and data storage:

```bash
psql -U datacentre -d ai_assistant < database-schema.sql
```

Creates tables:
- `telegram_messages` - Chat history
- `trading_logs` - Trading transactions
- `technical_analysis` - Analysis results
- `news_alerts` - Breaking news alerts
- `orchestrator_logs` - Workflow routing logs
- `system_logs` - All activity

---

## 🚀 Quick Setup

### Step 1: Copy Environment Template

```bash
cp .env.example .env
```

### Step 2: Edit Your API Keys

```bash
nano .env
```

Add:
- Anthropic API key
- Telegram bot token
- Trading212 API key
- Alpha Vantage API key
- Finnhub API key
- Polygon.io API key (optional)
- Database credentials

### Step 3: Create Database

```bash
psql -U postgres
CREATE DATABASE ai_assistant;
\c ai_assistant
\q
```

### Step 4: Load Schema

```bash
psql -U datacentre -d ai_assistant < database-schema.sql
```

### Step 5: Verify

```bash
psql -U datacentre -d ai_assistant -c "\dt"
```

Should show 6 tables.

---

## 📝 Environment Variables Guide

### Required Variables

```bash
# Anthropic (Claude AI)
ANTHROPIC_API_KEY=sk-ant-abc123...
  - Get from: https://console.anthropic.com
  - Format: starts with "sk-ant-"

# Telegram (Bot messaging)
TELEGRAM_BOT_TOKEN=123456789:ABCDEF_ghijklmnop...
  - Get from: @BotFather on Telegram
  - Format: "number:string"

TELEGRAM_USER_ID=987654321
  - Get by: Send message to bot, call getUpdates API
  - Format: Just numbers
```

### API Keys (For Features)

```bash
# Trading212 (Stock trading)
TRADING212_API_KEY=your_key_here
  - Get from: https://trading212.com API settings
  
# Alpha Vantage (Stock prices)
ALPHA_VANTAGE_KEY=demo
  - Get from: https://alphavantage.co/api-key
  - Free tier: 5 requests/min

# Finnhub (Market news)
FINNHUB_API_KEY=your_key_here
  - Get from: https://finnhub.io
  - Free tier: 60 requests/min

# Polygon.io (Real-time news) - Optional
POLYGON_API_KEY=your_key_here
  - Get from: https://polygon.io
  - 7-day free trial
```

### Database Variables

```bash
DB_HOST=localhost
  - Where PostgreSQL is running

DB_PORT=5432
  - Default PostgreSQL port

DB_NAME=ai_assistant
  - Database name to create

DB_USER=datacentre
  - Database user to create

DB_PASSWORD=your_secure_password
  - Strong password recommended
```

### Optional Variables

```bash
# Auto-trading (Be careful!)
AUTO_TRADE_ENABLED=false
  - Set to "true" only if fully configured

AUTO_TRADE_QUANTITY=1
  - Shares to buy per auto-trade

AUTO_TRADE_MAX_DAILY=5
  - Maximum trades per day (safety limit)

# N8N Settings
N8N_PORT=5678
  - Port for N8N dashboard

NODE_ENV=production
  - Set to "production" for Raspberry Pi
```

---

## 🔐 Security Best Practices

### Protect Your `.env` File

```bash
# Make it readable only by you
chmod 600 .env

# Don't commit to git
echo ".env" >> .gitignore

# Don't share or send anywhere
```

### API Key Rotation

Periodically rotate your API keys:

1. Generate new key in provider's dashboard
2. Update `.env` file
3. Restart N8N: `n8n stop && n8n`
4. Delete old key from provider

### Strong Database Password

Requirements:
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, symbols
- Not a dictionary word
- Not related to username

Example: `P@ssw0rd_AI_2024!`

---

## 📊 Database Schema Details

### Tables Included

#### `telegram_messages`
Stores all Telegram conversations:
```sql
- id (Primary key)
- user_id (Telegram user ID)
- username (Display name)
- message (User's message)
- response (Bot's response)
- created_at (Timestamp)
```

#### `trading_logs`
Tracks all trades:
```sql
- id
- user_id
- action (BUY/SELL)
- symbol (Stock ticker)
- quantity (Shares)
- price (Execution price)
- status (success/failed)
- created_at
```

#### `technical_analysis`
Stores analysis results:
```sql
- id
- symbol
- rsi (RSI indicator)
- ema20 (20-day EMA)
- ema50 (50-day EMA)
- macd (MACD value)
- prediction (AI analysis)
- confidence (Score 0-100)
- created_at
```

#### `news_alerts`
Logs breaking news:
```sql
- id
- ticker
- title
- impact (BULLISH/BEARISH)
- recommendation
- risk_level
- in_portfolio (Boolean)
- analysis (Claude's analysis)
- auto_traded (If trade executed)
- created_at
```

#### `orchestrator_logs`
Tracks workflow routing:
```sql
- id
- user_id
- intent (What user wanted)
- agents_used (Which agents ran)
- created_at
```

#### `system_logs`
General activity log:
```sql
- id
- user_id
- intent
- response
- created_at
```

---

## 🔍 Useful Queries

### Check Recent Messages

```sql
SELECT username, message, response, created_at 
FROM telegram_messages 
ORDER BY created_at DESC 
LIMIT 10;
```

### View Trading Activity

```sql
SELECT symbol, action, quantity, price, status, created_at 
FROM trading_logs 
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;
```

### Analyze News Impact

```sql
SELECT ticker, impact, COUNT(*) as count
FROM news_alerts
WHERE created_at > NOW() - INTERVAL '1 day'
GROUP BY ticker, impact
ORDER BY count DESC;
```

### Check System Health

```sql
SELECT 
  (SELECT COUNT(*) FROM telegram_messages) as total_messages,
  (SELECT COUNT(*) FROM trading_logs) as total_trades,
  (SELECT COUNT(*) FROM news_alerts) as total_alerts,
  NOW() as checked_at;
```

---

## 🚨 Backup Your Database

### Daily Backup

```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U datacentre ai_assistant > backup_$DATE.sql
echo "Backup created: backup_$DATE.sql"
```

### Restore from Backup

```bash
psql -U datacentre ai_assistant < backup_20240406_120000.sql
```

### Automate Backups

```bash
# Add to crontab
crontab -e

# Add line:
0 2 * * * /home/pi/backup.sh
```

---

## 📈 Performance Tuning

### Increase PostgreSQL Performance

Edit `/etc/postgresql/15/main/postgresql.conf`:

```ini
# For Raspberry Pi
shared_buffers = 256MB
effective_cache_size = 512MB
work_mem = 32MB
maintenance_work_mem = 64MB
```

Restart: `sudo systemctl restart postgresql`

### Clean Old Logs

Keep database lean by archiving old data:

```sql
-- Delete logs older than 90 days
DELETE FROM telegram_messages 
WHERE created_at < NOW() - INTERVAL '90 days';

-- Archive to CSV first if needed
COPY telegram_messages TO '/tmp/archive.csv' 
WHERE created_at < NOW() - INTERVAL '90 days';
```

---

## ❌ Common Configuration Mistakes

### ❌ API Key Has Spaces
```
ANTHROPIC_API_KEY=sk-ant- abc123   ← Wrong (spaces)
ANTHROPIC_API_KEY=sk-ant-abc123    ← Correct
```

### ❌ Wrong Variable Name
```
TELEGRAM_TOKEN=...              ← Wrong (should be TELEGRAM_BOT_TOKEN)
TELEGRAM_BOT_TOKEN=...          ← Correct
```

### ❌ Database Password Unset
```
DB_PASSWORD=                    ← Wrong (empty)
DB_PASSWORD=secure_password_123 ← Correct
```

### ❌ Port Already in Use
```
# Check what's using port 5678
lsof -i :5678

# Kill and free the port
kill -9 <PID>
```

---

## ✅ Verification Checklist

After setup:

```
Environment (.env):
[ ] ANTHROPIC_API_KEY is set
[ ] TELEGRAM_BOT_TOKEN is set
[ ] TELEGRAM_USER_ID is set
[ ] All API keys are added
[ ] DB credentials are correct

Database:
[ ] PostgreSQL is running
[ ] ai_assistant database exists
[ ] All 6 tables created
[ ] Can connect with credentials

N8N:
[ ] N8N is running
[ ] Can access http://localhost:5678
[ ] Workflows imported
[ ] Environment variables visible
```

---

## 🆘 Need Help?

### Check Logs

```bash
# N8N logs
tail -f ~/.n8n/logs.log

# PostgreSQL logs
sudo tail -f /var/log/postgresql/postgresql.log

# System logs
journalctl -u n8n -f
```

### Test Connection

```bash
# Test database
psql -U datacentre -d ai_assistant -c "SELECT NOW();"

# Test API key
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/models
```

---

## 📚 Additional Resources

- **PostgreSQL Docs:** https://www.postgresql.org/docs
- **N8N Configuration:** https://docs.n8n.io/hosting/environment-variables
- **Security Best Practices:** https://cheatsheetseries.owasp.org

---

**Setup complete? You're ready to use your AI assistant!** 🎉
