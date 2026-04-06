# N8N Telegram Bot Workflow Documentation

**Purpose:** Replace the Python Telegram bot with a visual n8n workflow that runs on Raspberry Pi 5  
**Status:** Ready to implement when hardware arrives  
**Platform:** n8n (open-source workflow automation)  

---

## 📊 Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    N8N TELEGRAM BOT WORKFLOW                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  START: Telegram Trigger Node                        │   │
│  │  (Listen for incoming messages)                      │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                            │
│                 ▼                                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  STEP 1: Switch Node                                │   │
│  │  (Route based on command or message type)           │   │
│  │  - /start → Initialize                             │   │
│  │  - /help → Send help text                          │   │
│  │  - /clear → Clear history                          │   │
│  │  - Regular text → Process with Claude              │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                            │
│  ┌──────────────┴───────────────────────────────────────┐   │
│  │                                                      │   │
│  ▼                                                      ▼   │
│  ┌─────────────────┐                  ┌───────────────────┐│
│  │ COMMAND Handler │                  │ MESSAGE Handler   ││
│  │ (send help/info)│                  │ (call Claude)     ││
│  └────────┬────────┘                  └─────────┬─────────┘│
│           │                                      │          │
│           │                    ┌─────────────────┘          │
│           │                    │                            │
│           │                    ▼                            │
│           │         ┌──────────────────────────────┐        │
│           │         │  STEP 2: HTTP Request        │        │
│           │         │  (Call Claude API)           │        │
│           │         │                              │        │
│           │         │  URL: api.anthropic.com      │        │
│           │         │  Method: POST                │        │
│           │         │  Headers: API Key            │        │
│           │         │  Body: Message + History     │        │
│           │         └──────────┬───────────────────┘        │
│           │                    │                            │
│           │                    ▼                            │
│           │         ┌──────────────────────────────┐        │
│           │         │  STEP 3: Parse Response      │        │
│           │         │  (Extract Claude's answer)   │        │
│           │         └──────────┬───────────────────┘        │
│           │                    │                            │
│           │                    ▼                            │
│           │         ┌──────────────────────────────┐        │
│           │         │  STEP 4: Telegram Send       │        │
│           │         │  (Send message back)         │        │
│           │         └──────────┬───────────────────┘        │
│           │                    │                            │
│           └────────────┬───────┘                            │
│                        │                                    │
│                        ▼                                    │
│           ┌──────────────────────────────┐                 │
│           │  STEP 5: Database Logger     │                 │
│           │  (Log to PostgreSQL)         │                 │
│           │  - User ID                   │                 │
│           │  - Message                   │                 │
│           │  - Response                  │                 │
│           │  - Timestamp                 │                 │
│           └──────────────┬───────────────┘                 │
│                          │                                 │
│                          ▼                                 │
│           ┌──────────────────────────────┐                 │
│           │  END: Success                │                 │
│           │  (Workflow complete)         │                 │
│           └──────────────────────────────┘                 │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Detailed Node Configuration

### NODE 1: Telegram Trigger

**Type:** Trigger → Telegram  
**Purpose:** Listen for incoming Telegram messages

**Configuration:**
```
Trigger: New message
Chat Type: Private
Include Attachments: No
Message Type: Text, Command
```

**Output:**
```json
{
  "user_id": "123456789",
  "chat_id": "123456789",
  "message_id": "999",
  "text": "Hello Claude",
  "first_name": "John",
  "username": "john_doe",
  "date": "2026-04-06T10:30:00Z"
}
```

---

### NODE 2: Switch Node

**Type:** Flow → Switch  
**Purpose:** Route based on message type (command vs regular message)

**Configuration:**
```
Switch on: {{ $json.text }}

Conditions:
1. If text starts with "/start"  → Route to "Start Handler"
2. If text starts with "/help"   → Route to "Help Handler"
3. If text starts with "/clear"  → Route to "Clear Handler"
4. Default (Regular message)     → Route to "Claude Handler"
```

---

### NODE 3A: Command Handlers (Start/Help/Clear)

**Type:** HTTP Request  
**Purpose:** Send static responses for commands

**For /start:**
```
Method: POST
URL: {{ $env.TELEGRAM_BOT_API }}
Headers: {
  "Content-Type": "application/json"
}
Body: {
  "chat_id": {{ $json.chat_id }},
  "text": "👋 Welcome to Claude Code!\n\nI'm an AI assistant powered by Claude. Send me any message and I'll respond!\n\nCommands:\n/clear - Clear conversation history\n/help - Show this message"
}
```

---

### NODE 3B: Claude Handler

**Type:** HTTP Request  
**Purpose:** Call Claude API with user message

**Configuration:**
```
Method: POST
URL: https://api.anthropic.com/v1/messages
Headers: {
  "Content-Type": "application/json",
  "x-api-key": "{{ $env.ANTHROPIC_API_KEY }}"
}

Body:
{
  "model": "claude-opus-4-1",
  "max_tokens": 2048,
  "messages": [
    {
      "role": "user",
      "content": "{{ $json.text }}"
    }
  ]
}
```

**Response Mapping:**
```
Extract: .content[0].text
Store as: claude_response
```

---

### NODE 4: Response Parser

**Type:** Code → JavaScript  
**Purpose:** Format Claude's response for Telegram

**Code:**
```javascript
// Extract the response text
const response = $json.claude_response;

// Handle long responses (Telegram limit: 4096 chars)
if (response.length > 4096) {
  const messages = [];
  for (let i = 0; i < response.length; i += 4096) {
    messages.push(response.substring(i, i + 4096));
  }
  return { messages: messages };
} else {
  return { messages: [response] };
}
```

---

### NODE 5: Telegram Send Response

**Type:** HTTP Request  
**Purpose:** Send Claude's response back to Telegram

**Configuration:**
```
Method: POST
URL: {{ $env.TELEGRAM_BOT_API }}
Headers: {
  "Content-Type": "application/json"
}

For each message in messages array:
{
  "chat_id": {{ $json.chat_id }},
  "text": "{{ $json.message }}",
  "parse_mode": "HTML"
}
```

---

### NODE 6: Database Logger

**Type:** PostgreSQL  
**Purpose:** Store conversation history

**Configuration:**
```
Host: localhost
Port: 5432
Database: ai_assistant
User: datacentre
Password: [from .env]

Query:
INSERT INTO conversations 
(user_id, user_message, claude_response, created_at)
VALUES 
({{ $json.user_id }}, 
 '{{ $json.text }}', 
 '{{ $json.claude_response }}', 
 NOW())
```

**Database Schema:**
```sql
CREATE TABLE conversations (
  id SERIAL PRIMARY KEY,
  user_id BIGINT,
  user_message TEXT,
  claude_response TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE users (
  user_id BIGINT PRIMARY KEY,
  username VARCHAR(255),
  first_seen TIMESTAMP DEFAULT NOW(),
  message_count INT DEFAULT 0
);
```

---

### NODE 7: Error Handler

**Type:** Flow → Error Workflow  
**Purpose:** Handle and log errors

**Configuration:**
```
On Error:
1. Send error message to user: "❌ Error: Please try again"
2. Log error to database
3. Notify admin (optional)

Error Message Template:
❌ Something went wrong: {{ error.message }}
Please try again later.
```

---

## 🔐 Environment Variables (.env)

```
ANTHROPIC_API_KEY=sk-ant-api03-pid4-...
TELEGRAM_BOT_TOKEN=8673730056:AAGbysiHPkBCE6mEi1C5HP8i7kVjWcwXwZo
TELEGRAM_BOT_API=https://api.telegram.org/bot{{ $env.TELEGRAM_BOT_TOKEN }}/sendMessage
DATABASE_URL=postgresql://datacentre:password@localhost:5432/ai_assistant
```

---

## 📈 Advanced Features (Optional)

### Feature 1: Conversation Context
Store and retrieve conversation history for multi-turn conversations:
```
Before calling Claude:
- Fetch last 5 messages from database
- Include in Claude API request
- Maintain context across sessions
```

### Feature 2: Rate Limiting
Prevent spam and API abuse:
```
Per user: Max 10 messages per minute
Per IP: Max 50 messages per minute
Add check: IF message_count > limit THEN deny
```

### Feature 3: User Management
Track user engagement:
```
Node: Track user activity
- Increment message_count on new message
- Update last_seen timestamp
- Track unique users
```

### Feature 4: Admin Commands
Add privileged commands:
```
/stats - Show bot statistics
/users - Show active users
/clear-all - Clear all conversations
```

---

## 🚀 Deployment on Raspberry Pi

### Installation Steps:
```bash
# 1. SSH into Raspberry Pi
ssh pi@raspberry-pi-ip

# 2. Install n8n
npm install -g n8n

# 3. Start n8n
n8n start

# 4. Access at: http://raspberry-pi-ip:5678
```

### Run n8n as Service:
```bash
# Create systemd service
sudo nano /etc/systemd/system/n8n.service

[Unit]
Description=n8n Workflow Automation
After=network.target

[Service]
Type=simple
User=pi
ExecStart=/usr/local/bin/n8n start
Restart=always

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable n8n
sudo systemctl start n8n
```

---

## 📊 Workflow Benefits vs Python Bot

| Feature | Python Bot | N8N Workflow |
|---------|-----------|--------------|
| Visual Interface | ❌ Code only | ✅ Drag & drop |
| Error Handling | Manual | ✅ Built-in |
| Logging | Manual | ✅ Built-in |
| Monitoring | Terminal | ✅ Dashboard |
| Easy Changes | Code edit needed | ✅ Visual edit |
| Performance | Fast | ✅ Fast |
| Learning Curve | Steep | ✅ Gentle |
| Database Integration | Manual | ✅ Native nodes |

---

## 🔄 Migration Path

### Current (Now):
```
Windows Laptop
└── Python Telegram Bot (manual run)
```

### When Hardware Arrives:
```
Raspberry Pi 5 (Always On)
├── n8n Service (Auto-start)
│   └── Telegram Bot Workflow
├── PostgreSQL Database
└── 2TB SSD Storage
```

### Full Integration:
```
Raspberry Pi 5
├── n8n Workflows
│   ├── Telegram Bot
│   ├── Email Notifications
│   ├── Data Backup
│   └── Analytics
├── Web Dashboard (React)
├── API Server (FastAPI)
└── PostgreSQL Database
```

---

## 📝 Notes

- **All nodes are visual** - No coding required
- **Fully configurable** - Change behavior without redeploying
- **Production-ready** - Handles errors gracefully
- **Scalable** - Can add more workflows easily
- **Monitored** - Built-in execution history & logs
- **24/7 ready** - Runs on Raspberry Pi automatically

---

## ✅ Advantages of N8N Workflow

1. **Visual Development** - See entire workflow at a glance
2. **No Server Restarts** - Edit workflows while running
3. **Built-in Database** - Native PostgreSQL integration
4. **Error Handling** - Automatic retry & fallback logic
5. **Monitoring Dashboard** - See all executions & logs
6. **Easy Debugging** - Test individual nodes
7. **Extensible** - Add more nodes/workflows later
8. **Cost** - Free & open-source

---

**Ready to implement on Raspberry Pi 5 when hardware arrives!** 🚀
