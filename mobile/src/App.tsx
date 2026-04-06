import React, { useEffect, useState } from 'react';
import {
  StyleSheet,
  View,
  SafeAreaView,
  StatusBar,
  Alert,
} from 'react-native';
import ChatScreen from './screens/ChatScreen';
import { ChatProvider } from './context/ChatContext';
import { initializeConversation } from './api/client';

export default function App(): React.JSX.Element {
  const [isInitializing, setIsInitializing] = useState(true);

  useEffect(() => {
    const initialize = async () => {
      try {
        await initializeConversation();
        setIsInitializing(false);
      } catch (error) {
        Alert.alert('Error', 'Failed to initialize app. Check your backend connection.');
        setIsInitializing(false);
      }
    };

    initialize();
  }, []);

  return (
    <ChatProvider>
      <SafeAreaView style={styles.container}>
        <StatusBar barStyle="dark-content" backgroundColor="#f5f5f5" />
        <ChatScreen />
      </SafeAreaView>
    </ChatProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
