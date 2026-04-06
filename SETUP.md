# Claude Code iOS - Setup Guide

This project contains both a Python FastAPI backend and a native iOS app for accessing Claude AI.

## Project Structure

```
.
├── backend/                 # Python FastAPI backend
│   ├── main.py             # Main FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
└── ios/                     # iOS application
    └── ClaudeCodeIOS/       # SwiftUI app source code
        ├── App.swift        # App entry point
        ├── ContentView.swift # Main chat UI
        └── ChatViewModel.swift # Chat logic and API calls
```

## Backend Setup

### Prerequisites
- Python 3.9+
- pip
- Anthropic API key

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

5. Run the server:
   ```bash
   python main.py
   ```

   The backend will be available at `http://localhost:8000`

## iOS Setup

### Prerequisites
- macOS with Xcode 15+
- An iOS device or simulator running iOS 14+

### Steps

1. Open Xcode and create a new project:
   - Product → New → Project
   - Choose "App" template
   - Set Product Name to "ClaudeCodeIOS"
   - Choose SwiftUI for interface and Swift for language

2. Copy the Swift files from `ios/ClaudeCodeIOS/` to your Xcode project

3. In the iOS app, configure the API base URL in `ChatViewModel.swift`:
   - For development: `http://localhost:8000`
   - For production: your actual backend URL

4. Build and run the app (⌘R in Xcode)

## API Endpoints

### Chat
- **POST** `/chat`
  - Request: `{ "conversation_id": "uuid", "message": "user message" }`
  - Response: `{ "conversation_id": "uuid", "response": "assistant response", "messages": [...] }`

### Code Execution
- **POST** `/execute-code`
  - Request: `{ "conversation_id": "uuid", "message": "code to execute" }`
  - Response: Same as chat

### New Conversation
- **POST** `/new-conversation`
  - Response: `{ "conversation_id": "uuid" }`

### Health Check
- **GET** `/health`
  - Response: `{ "status": "healthy" }`

## Development

### Backend Development
- FastAPI automatically reloads on file changes in development
- Access API docs at `http://localhost:8000/docs`

### iOS Development
- Use Xcode's preview to see changes in real-time
- Test on simulator or device

## Next Steps

- [ ] Add user authentication
- [ ] Implement code syntax highlighting on iOS
- [ ] Add message persistence/caching
- [ ] Support file uploads
- [ ] Add voice input/output
- [ ] Deploy backend to cloud service
- [ ] Implement actual code execution sandbox
