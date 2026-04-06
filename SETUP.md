# Claude Code Mobile - Setup Guide

This project contains both a Python FastAPI backend and a React Native mobile app for accessing Claude AI.
Develop on Windows and deploy to both iOS and Android!

## Project Structure

```
.
├── backend/                 # Python FastAPI backend
│   ├── main.py             # Main FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── .env.example         # Environment variables template
└── mobile/                  # React Native mobile app
    ├── src/
    │   ├── App.tsx         # App entry point
    │   ├── api/
    │   │   └── client.ts   # API communication
    │   ├── context/
    │   │   └── ChatContext.tsx # State management
    │   ├── screens/
    │   │   └── ChatScreen.tsx  # Chat UI
    │   └── components/
    │       ├── MessageBubble.tsx
    │       └── ChatHeader.tsx
    ├── package.json
    └── tsconfig.json
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

## Mobile App Setup (React Native)

### Prerequisites
- Node.js 16+ and npm/yarn
- React Native CLI: `npm install -g react-native-cli`
- Java Development Kit (JDK) 11+ for Android
- Android Studio and Android SDK for Android development
- Xcode 14+ and CocoaPods for iOS development (on Mac)

### Installation

1. Navigate to the mobile directory:
   ```bash
   cd mobile
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Install native dependencies:
   ```bash
   npm install -g react-native-cli
   ```

### Running the App

#### On Android (Windows/Mac/Linux)
```bash
cd mobile
npm run android
```

#### On iOS (Mac only)
```bash
cd mobile
# Install pod dependencies first
cd ios && pod install && cd ..
npm run ios
```

#### Start the dev server
```bash
npm start
```

### Configuration

Edit `src/api/client.ts` to change the backend URL:
```typescript
const API_BASE_URL = 'http://your-backend-url:8000';
```

For development on Windows, use your machine's IP address when testing on a physical device:
- Get your IP: `ipconfig` (Windows)
- Update in client.ts: `http://192.168.x.x:8000`

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
