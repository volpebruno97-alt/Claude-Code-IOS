# Development Guide

## Quick Start

### Backend

1. Set up Python environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

4. Run the server:
   ```bash
   python main.py
   ```

   The server will start at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### iOS App

#### Option 1: Using Swift Package Manager (CLI)

1. Create an Xcode project from the source files:
   ```bash
   cd ios
   ```

2. Open Xcode and create a new iOS App project:
   - File → New → Project
   - Select "App" template
   - Product Name: "ClaudeCodeIOS"
   - Team: Your team
   - Organization: Your org
   - Bundle Identifier: com.yourname.claudecodeiOS
   - Interface: SwiftUI
   - Language: Swift

3. Copy the Swift files from `ClaudeCodeIOS/` to your new project

4. Update the API URL in `ChatViewModel.swift` if needed:
   ```swift
   @Published var apiBaseURL: String = "http://localhost:8000"
   ```

5. Build and run (⌘B then ⌘R)

#### Option 2: Creating Project Programmatically

We provide sample code files. You can:
1. Create a new iOS project in Xcode
2. Copy `App.swift`, `ContentView.swift`, and `ChatViewModel.swift` to your project
3. Replace the default `ContentView` implementation

## API Testing

### Using curl

```bash
# Start a new conversation
curl -X POST http://localhost:8000/new-conversation

# Send a message
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "your-conversation-id",
    "message": "Hello, Claude!"
  }'
```

### Using the built-in API docs

Visit `http://localhost:8000/docs` to use the interactive API documentation.

## Debugging

### Backend
- Enable debug mode by setting `DEBUG=true` in `.env`
- Check logs in the terminal where you ran `python main.py`
- Use FastAPI's Swagger UI for API testing

### iOS
- Use Xcode's debug console (⌘Y)
- Set breakpoints in the code and inspect variables
- Monitor network traffic in Xcode's Network Link Conditioner

## File Structure

```
ios/ClaudeCodeIOS/
├── App.swift              # App entry point (@main)
├── ContentView.swift      # Main chat UI
├── ChatViewModel.swift    # ViewModel for chat logic
└── Preview Content/       # Preview assets (if needed)
```

## Common Issues

### "Cannot connect to backend"
- Ensure backend is running: `python main.py`
- Check that `apiBaseURL` in `ChatViewModel.swift` matches your backend URL
- For iOS simulator on Mac: use `http://localhost:8000`
- For physical device: use your Mac's IP address (e.g., `http://192.168.1.100:8000`)

### "ANTHROPIC_API_KEY not set"
- Make sure you've created a `.env` file in the `backend/` directory
- Add your Anthropic API key: `ANTHROPIC_API_KEY=sk-...`
- Restart the backend server after updating `.env`

### "CORS error"
- Update `CORS_ORIGINS` in `.env` to include your frontend URL
- Default: `http://localhost:8000,http://localhost:3000`

## Testing

### Manual Testing
1. Start backend: `python main.py`
2. Run iOS app in simulator
3. Send test messages and verify responses

### API Testing with SwiftUI Previews
Edit `ContentView.swift` to add custom preview data for testing UI without making API calls.

## Next Development Steps

- [ ] Add persistent conversation storage
- [ ] Implement code syntax highlighting in iOS
- [ ] Add support for file uploads
- [ ] Create user authentication system
- [ ] Add conversation history view
- [ ] Implement markdown rendering for API responses
- [ ] Add dark mode support
- [ ] Create settings page for API URL configuration
