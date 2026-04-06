# N8N Multi-Agent System - Visual Layout Guide

**Complete visual guide for organizing your agents in n8n dashboard**

---

## 🏗️ Overall System Architecture in N8N

```
┌─────────────────────────────────────────────────────────────────┐
│                    N8N DASHBOARD (Main View)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WORKFLOWS TAB (9 separate workflows listed)                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ ✓ AGENT-TELEGRAM-GATEWAY        [Active] [Edit] [Run]    │  │
│  │ ✓ AGENT-MAIN-ORCHESTRATOR       [Active] [Edit] [Run]    │  │
│  │ ✓ AGENT-TRADING212              [Active] [Edit] [Run]    │  │
│  │ ✓ AGENT-TECHNICAL-ANALYSIS      [Active] [Edit] [Run]    │  │
│  │ ✓ AGENT-MARKET-DATA             [Active] [Edit] [Run]    │  │
│  │ ✓ AGENT-PORTFOLIO-MANAGER       [Active] [Edit] [Run]    │  │
│  │ ○ AGENT-FILE-MANAGER            [Inactive]              │  │
│  │ ○ AGENT-FINANCE-TRACKER         [Inactive]              │  │
│  │ ○ AGENT-RESEARCH                [Inactive]              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  TAGS: [Core] [Trading] [Market] [Management] [Analysis]        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Agent Communication Layout

### **Communication Pattern**

```
TELEGRAM USER
    │
    ▼
┌──────────────────────────┐
│ AGENT-TELEGRAM-GATEWAY   │ (Node Layout: Vertical)
│                          │
│ [Telegram Trigger]       │ (Y: 300)
│         ↓                │
│ [Parse Message]          │ (Y: 450)
│         ↓                │
│ [Send to Orchestrator]   │ (Y: 600) ──HTTP──→
│         ↓                │
│ [Send Response]          │ (Y: 750) ←──HTTP──
│         ↓                │
│ [Log to Database]        │ (Y: 900)
└──────────────────────────┘
    │
    ▼ (Webhook POST)
┌──────────────────────────────┐
│ AGENT-MAIN-ORCHESTRATOR      │ (Node Layout: Vertical Flow)
│                              │
│ [Webhook Trigger]            │ (Y: 300)
│         ↓                     │
│ [Analyze Intent]             │ (Y: 450)
│         ↓                     │
│ [Route to Agents]            │ (Y: 600) ──HTTP→
│    ├──→ Agent 1              │
│    ├──→ Agent 2              │
│    └──→ Agent 3              │
│         ↓                     │
│ [Synthesize Response]        │ (Y: 750)
│         ↓                     │
│ [Send to Telegram]           │ (Y: 900)
│         ↓                     │
│ [Log Orchestration]          │ (Y: 1050)
└──────────────────────────────┘
```

---

## 📐 Individual Agent Node Layout

### **Layout Pattern for Each Agent**

```
HORIZONTAL FLOW (Left to Right)

┌─────────────────────────────────────────────────────────────┐
│ AGENT WORKFLOW                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  X: 250      X: 450      X: 650      X: 850      X: 1050  │
│  ┌────┐      ┌────┐      ┌────┐      ┌────┐      ┌────┐   │
│  │    │  →   │    │  →   │    │  →   │    │  →   │    │   │
│  │ 1  │      │ 2  │      │ 3  │      │ 4  │      │ 5  │   │
│  │    │      │    │      │    │      │    │      │    │   │
│  └────┘      └────┘      └────┘      └────┘      └────┘   │
│   Trigger    Process    API Call    Transform    Output    │
│                                        │                    │
│                                        ▼                    │
│                                      ┌────┐                │
│                                      │ 6  │ (Side)         │
│                                      │DB  │                │
│                                      └────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 AGENT-TELEGRAM-GATEWAY Layout (Detailed)

### **Node Positions & Flow**

```
Y-AXIS (Top to Bottom):

Y: 200  ┌─────────────────────────────────────┐
        │  Telegram Trigger                   │
        │  (Node ID: telegram-trigger-01)     │
        │  X: 250, Y: 300                     │
        │  Purpose: Listen for messages       │
        └────────────────┬────────────────────┘
                         │ (Connection)
                         ▼
Y: 350  ┌─────────────────────────────────────┐
        │  Parse Message                      │
        │  (Node ID: parse-message-02)        │
        │  X: 450, Y: 300                     │
        │  Purpose: Extract user info         │
        └────────────────┬────────────────────┘
                         │
                         ▼
Y: 500  ┌─────────────────────────────────────┐
        │  Send to Orchestrator               │
        │  (Node ID: send-to-orchestrator-03) │
        │  X: 650, Y: 300                     │
        │  Purpose: HTTP POST to orchestrator │
        └────────────────┬────────────────────┘
                         │
                         ▼
Y: 650  ┌─────────────────────────────────────┐
        │  Send Response                      │
        │  (Node ID: send-response-04)        │
        │  X: 850, Y: 300                     │
        │  Purpose: Reply via Telegram API    │
        └────────────────┬────────────────────┘
                         │
                         ▼
Y: 800  ┌─────────────────────────────────────┐
        │  Log Message (Database)             │
        │  (Node ID: log-message-05)          │
        │  X: 850, Y: 450                     │
        │  Purpose: Store in PostgreSQL       │
        └─────────────────────────────────────┘
```

### **In N8N Editor (What You'll See)**

```
Screen Layout:
┌────────────────────────────────────────────────────────┐
│ AGENT-TELEGRAM-GATEWAY                      [Activate]│
├────────────────────────────────────────────────────────┤
│                                                        │
│   [Telegram Trigger]                                  │
│          ↓ (Blue line)                                │
│   [Parse Message]                                     │
│          ↓                                            │
│   [Send to Orchestrator] ──(Red)──→ [API]            │
│          ↓                                            │
│   [Send Response]                                     │
│          ↓                                            │
│   [Log Message to DB]                                │
│                                                        │
│   Zoom: 100%  Grid: On   Pan: [+] [-]                │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 🎯 AGENT-MAIN-ORCHESTRATOR Layout (Complex)

### **Node Positions with Multiple Routes**

```
                           ┌─────────────────────┐
                           │ Webhook Trigger     │
                           │ (X: 250, Y: 300)    │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Analyze Intent      │
                           │ (X: 450, Y: 300)    │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Route to Agents     │
                           │ (X: 650, Y: 300)    │
                           └──────────┬──────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
            ┌────────────┐   ┌────────────┐   ┌────────────┐
            │ Agent 1    │   │ Agent 2    │   │ Agent 3    │
            │ (Trading)  │   │ (Analysis) │   │ (Market)   │
            └──────┬─────┘   └──────┬─────┘   └──────┬─────┘
                   │                │                │
                   └────────────────┼────────────────┘
                                    ▼
                           ┌─────────────────────┐
                           │ Synthesize Response │
                           │ (X: 850, Y: 300)    │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Send to Telegram    │
                           │ (X: 1050, Y: 300)   │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │ Log Orchestration   │
                           │ (X: 1050, Y: 450)   │
                           └─────────────────────┘
```

---

## 🔄 Sub-Agent Layout Pattern (AGENT-TRADING212)

### **Switch Node with Multiple Branches**

```
                        ┌──────────────────┐
                        │ Webhook Trigger  │
                        │ (X: 250, Y: 300) │
                        └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │ Switch Action    │
                        │ (X: 450, Y: 300) │
                        └────────┬─────────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                   /buy\        /sell\       /balance\
                   │            │            │
                   ▼            ▼            ▼
           ┌──────────┐  ┌──────────┐  ┌─────────────┐
           │ Get      │  │ Place    │  │ Get Balance │
           │ Balance  │  │ Trade    │  │ (X: 650,Y:450)
           │(X:650,   │  │(X:650,   │  └──────┬──────┘
           │Y:150)    │  │Y:300)    │         │
           └────┬─────┘  └────┬─────┘  ┌──────┴──────┐
                │              │       │             │
                └──────────────┼───────┘             │
                               │                     │
                               ▼                     │
                      ┌──────────────────┐           │
                      │ Format Response  │◄──────────┘
                      │ (X: 850, Y: 300) │
                      └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │ Log Trade (DB)   │
                      │ (X: 850, Y: 450) │
                      └──────────────────┘
```

---

## 📊 Dashboard Organization Tips

### **1. Use Folders/Groups**

```
N8N Sidebar:
┌─ Workflows
│  ├─ 📁 TIER 1 - CORE
│  │  ├─ AGENT-TELEGRAM-GATEWAY
│  │  └─ AGENT-MAIN-ORCHESTRATOR
│  │
│  ├─ 📁 TIER 2 - TRADING
│  │  ├─ AGENT-TRADING212
│  │  ├─ AGENT-TECHNICAL-ANALYSIS
│  │  ├─ AGENT-MARKET-DATA
│  │  └─ AGENT-PORTFOLIO-MANAGER
│  │
│  └─ 📁 TIER 3 - MANAGEMENT
│     ├─ AGENT-FILE-MANAGER
│     ├─ AGENT-FINANCE-TRACKER
│     └─ AGENT-RESEARCH
│
├─ Credentials
├─ Variables
└─ Executions
```

### **2. Color-Code by Tier**

```
Node Colors (Recommendation):
- TIER 1 (Core):     Blue nodes
- TIER 2 (Trading):  Green nodes
- TIER 3 (Manage):   Purple nodes
- API Calls:         Red nodes
- Database:          Orange nodes
```

### **3. Naming Convention**

```
Node Names:
[AGENT]-[STEP NUMBER]-[ACTION]

Examples:
- telegram-trigger-01
- parse-message-02
- send-to-orchestrator-03
- get-balance-02
- format-response-05
- log-message-05
```

---

## 🖥️ Full Dashboard Layout Example

```
┌────────────────────────────────────────────────────────────────┐
│ N8N Editor - AGENT-MAIN-ORCHESTRATOR                      ▢ ▢ ✕│
├────────────────────────────────────────────────────────────────┤
│ File  Edit  View  Insert  Tools  Help                    [?]    │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [+]  [Save]  [Activate]  [Execute]  [Clear]                   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │                                                          │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Webhook In  │                               │   │
│  │          └──────┬───────┘                               │   │
│  │                 │                                        │   │
│  │                 ▼                                        │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Analyze     │                               │   │
│  │          │  Intent      │                               │   │
│  │          └──────┬───────┘                               │   │
│  │                 │                                        │   │
│  │                 ▼                                        │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Route to    │                               │   │
│  │          │  Agents      │                               │   │
│  │          └──────┬───────┘                               │   │
│  │                 │                                        │   │
│  │                 ▼                                        │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Synthesize  │                               │   │
│  │          │  Response    │                               │   │
│  │          └──────┬───────┘                               │   │
│  │                 │                                        │   │
│  │                 ▼                                        │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Send to TG  │                               │   │
│  │          └──────┬───────┘                               │   │
│  │                 │                                        │   │
│  │                 ▼                                        │   │
│  │          ┌──────────────┐                               │   │
│  │          │  Log Result  │                               │   │
│  │          └──────────────┘                               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Zoom: 100%  Pan Mode  [Node Props] [Executions] [Monitor]     │
└────────────────────────────────────────────────────────────────┘
```

---

## 🔌 Node Types Used in Each Agent

### **Common Node Types**

```
AGENT-TELEGRAM-GATEWAY:
├─ Telegram Trigger (Trigger node)
├─ Code (JavaScript - Parse)
├─ HTTP Request (POST to orchestrator)
├─ Telegram Send Message (HTTP Request)
└─ PostgreSQL (Insert logs)

AGENT-MAIN-ORCHESTRATOR:
├─ Webhook (Trigger node)
├─ Code (JavaScript - Intent analysis)
├─ HTTP Request (Route to agents)
├─ Code (JavaScript - Synthesize)
├─ HTTP Request (Response to Telegram)
└─ PostgreSQL (Log orchestration)

AGENT-TRADING212:
├─ Webhook (Trigger node)
├─ Switch (Route by action)
├─ HTTP Request (Get balance)
├─ HTTP Request (Get holdings)
├─ HTTP Request (Place trade)
├─ Code (JavaScript - Format)
└─ PostgreSQL (Log trades)

AGENT-TECHNICAL-ANALYSIS:
├─ Webhook (Trigger node)
├─ HTTP Request (Fetch price data)
├─ HTTP Request (Calculate indicators)
├─ HTTP Request (Claude API)
├─ Code (JavaScript - Format)
└─ PostgreSQL (Save analysis)

AGENT-MARKET-DATA:
├─ Webhook (Trigger node)
├─ HTTP Request (Get price - Alpha Vantage)
├─ HTTP Request (Get market data - Finnhub)
├─ HTTP Request (Get news - Finnhub)
├─ Code (JavaScript - Combine)
└─ PostgreSQL (Cache data)

AGENT-PORTFOLIO-MANAGER:
├─ Webhook (Trigger node)
├─ HTTP Request (Get holdings)
├─ HTTP Request (Get account info)
├─ Code (JavaScript - Analyze)
├─ HTTP Request (Claude analysis)
└─ PostgreSQL (Save snapshot)
```

---

## 🎨 Visual Spacing Guide

### **Recommended Node Spacing**

```
X-Axis (Horizontal spacing):
200px apart for each node in sequence

Y-Axis (Vertical spacing):
150px apart for vertical flow
300px apart for parallel branches

Example Grid:
X: 250, 450, 650, 850, 1050 (200px intervals)
Y: 300, 450, 600, 750, 900 (150px intervals)
```

---

## 📱 Monitor/Dashboard View

### **Once All Agents Running**

```
N8N Dashboard > Executions:

┌─────────────────────────────────────────────┐
│ Workflow Executions                         │
├──────────────┬──────────┬────────────────────┤
│ Workflow     │ Status   │ Time               │
├──────────────┼──────────┼────────────────────┤
│ AGENT-TELE.. │ ✓ Active │ Last: 2 min ago    │
│ AGENT-MAIN.. │ ✓ Active │ Last: 1 min ago    │
│ AGENT-TRAD.. │ ✓ Active │ Last: 3 min ago    │
│ AGENT-TECH.. │ ✓ Active │ Last: 5 min ago    │
│ AGENT-MARK.. │ ✓ Active │ Last: 1 min ago    │
│ AGENT-PORT.. │ ✓ Active │ Last: 2 min ago    │
│ AGENT-FILE.. │ ○ Idle   │ Last: 1 hour ago   │
│ AGENT-FINA.. │ ○ Idle   │ Last: Never        │
│ AGENT-RESE.. │ ○ Idle   │ Last: Never        │
└──────────────┴──────────┴────────────────────┘
```

---

## ✅ Best Practices for Layout

1. **Use Consistent Spacing**
   - Keep nodes evenly spaced
   - Use grid alignment

2. **Color Code by Function**
   - Triggers: Blue
   - Logic: Green
   - API: Red
   - Database: Orange
   - Code: Purple

3. **Label Nodes Clearly**
   - Use descriptive names
   - Include step numbers
   - Keep names short but clear

4. **Organize Connections**
   - Avoid crossing lines when possible
   - Use webhooks for agent-to-agent communication
   - Keep main flow horizontal (left to right)

5. **Group Related Nodes**
   - Keep API calls together
   - Group database operations
   - Keep parsing logic near triggers

6. **Document with Comments**
   - Add description to each node
   - Explain API endpoints
   - Note database operations

---

## 🚀 Setup Order on N8N

```
1. Create AGENT-TELEGRAM-GATEWAY first
   └─ Test with Telegram

2. Create AGENT-MAIN-ORCHESTRATOR
   └─ Connect to Telegram Gateway

3. Create trading agents
   ├─ AGENT-TRADING212
   ├─ AGENT-TECHNICAL-ANALYSIS
   ├─ AGENT-MARKET-DATA
   └─ AGENT-PORTFOLIO-MANAGER

4. Test each agent independently

5. Create management agents
   ├─ AGENT-FILE-MANAGER
   ├─ AGENT-FINANCE-TRACKER
   └─ AGENT-RESEARCH

6. Full system testing
```

---

**Your agents are now ready to be beautifully organized in n8n!** 🎨

