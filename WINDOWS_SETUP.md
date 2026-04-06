# Windows Setup Guide

This guide helps you set up Claude Code Mobile development on Windows.

## Prerequisites Installation

### 1. Node.js and npm
1. Download from https://nodejs.org (LTS version)
2. Run the installer and follow the prompts
3. Verify installation:
   ```bash
   node --version
   npm --version
   ```

### 2. Java Development Kit (JDK)
1. Download JDK 11+ from https://www.oracle.com/java/technologies/downloads/
2. Run the installer
3. Set JAVA_HOME environment variable:
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Add new system variable:
     - Variable name: `JAVA_HOME`
     - Variable value: `C:\Program Files\Java\jdk-XX` (your JDK path)

### 3. Android Studio
1. Download from https://developer.android.com/studio
2. Run the installer
3. Complete the setup wizard and install Android SDK

### 4. Python (for backend)
1. Download from https://www.python.org
2. Run the installer
3. **Important**: Check "Add Python to PATH"
4. Verify:
   ```bash
   python --version
   ```

### 5. Git
1. Download from https://git-scm.com/download/win
2. Run the installer and follow prompts
3. Verify:
   ```bash
   git --version
   ```

## Environment Setup

### Create Environment Variables
1. Right-click "This PC" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Add/verify these variables:
   - `JAVA_HOME` = `C:\Program Files\Java\jdk-XX`
   - `ANDROID_HOME` = `C:\Users\YourUsername\AppData\Local\Android\Sdk`

### Create .env File
1. Navigate to the `backend` folder
2. Copy `.env.example` to `.env`
3. Add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-your-key-here
   ```

## Running the Project

### Terminal 1: Start the Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

The backend will run at `http://localhost:8000`

### Terminal 2: Start the Mobile App

#### For Android
```bash
cd mobile
npm install
npm run android
```

This will:
1. Start the Metro bundler
2. Build the Android app
3. Deploy it to an emulator or connected device

#### To run on a physical Android device:
1. Enable Developer Mode on your phone
2. Connect via USB
3. Verify connection: `adb devices`
4. Run: `npm run android`

### Terminal 3: React Native Dev Server (if needed)
```bash
cd mobile
npm start
```

## Troubleshooting

### "Command 'react-native' not found"
```bash
npm install -g react-native-cli
```

### "ANDROID_HOME not set"
Set the environment variable as described above, then restart your terminal.

### "Failed to connect to backend"
- Ensure backend is running on port 8000
- Use your Windows PC's IP address instead of localhost for physical devices:
  ```bash
  ipconfig
  ```
  Look for "IPv4 Address" and update `src/api/client.ts`

### Android Emulator won't start
1. Open Android Studio
2. Tools → Device Manager
3. Create a new virtual device
4. Click "Play" to launch

### Port 8000 already in use
```bash
# Find the process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID)
taskkill /PID <PID> /F
```

## Next Steps

1. Start the backend server
2. Run the mobile app on Android
3. Send messages to Claude from your phone!
4. Once stable, build APK for distribution or use Xcode on Mac for iOS

## Building for Production

### Android APK
```bash
cd mobile/android
./gradlew assembleRelease
```

APK will be at: `mobile/android/app/build/outputs/apk/release/app-release.apk`

### Deploying to App Stores
- [Google Play Store](https://developer.android.com/studio/publish)
- [Apple App Store](https://developer.apple.com/app-store/) (requires Mac)
