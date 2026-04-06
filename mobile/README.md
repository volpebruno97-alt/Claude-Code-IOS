# Claude Code Mobile - React Native

A cross-platform mobile app for accessing Claude AI, built with React Native and TypeScript.

## Features

- 💬 Real-time chat with Claude AI
- 📱 Works on iOS and Android
- 🎨 Clean, intuitive UI
- ⚡ Fast message streaming
- 💾 Persistent conversation history
- 🔌 Configurable backend API

## Quick Start

```bash
# Install dependencies
npm install

# Run on Android
npm run android

# Run on iOS (Mac only)
npm run ios

# Start dev server
npm start
```

## Architecture

### State Management
- React Context API for global state
- Hooks for component-level state

### API Communication
- Axios for HTTP requests
- AsyncStorage for local data persistence

### Components
- **ChatScreen**: Main chat interface
- **MessageBubble**: Individual message display
- **ChatHeader**: App header with info

## Configuration

Edit `src/api/client.ts` to configure:
- Backend API URL
- Request timeouts
- API endpoints

## Platform-Specific Setup

### Android
- Requires Android SDK 21+
- Android Studio recommended
- Connect device or start emulator
- Run: `npm run android`

### iOS
- Requires macOS and Xcode 14+
- Run: `npm run ios`
- Install pods if needed: `cd ios && pod install`

## API Endpoints

The app communicates with a Python FastAPI backend:

- `POST /new-conversation` - Start new chat
- `POST /chat` - Send message
- `POST /execute-code` - Execute code

See `../backend` for backend implementation.

## Development

```bash
# Start Metro bundler
npm start

# Run tests
npm test

# Lint code
npm run lint
```

## Building for Release

### Android
```bash
cd android && ./gradlew assembleRelease
```

### iOS
```bash
cd ios && xcodebuild -workspace ClaudeCodeIOS.xcworkspace -scheme ClaudeCodeIOS -configuration Release
```

## Troubleshooting

- **Backend connection fails**: Check API URL in `src/api/client.ts`
- **Android emulator won't start**: Use Android Studio's Device Manager
- **Pod install fails on iOS**: Run `cd ios && rm -rf Pods && pod install`

## License

MIT
