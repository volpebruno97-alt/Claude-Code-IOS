import React, { createContext, useContext, useState, useCallback } from 'react';
import { Message } from '../api/client';
import { sendMessage as apiSendMessage } from '../api/client';

interface ChatContextType {
  messages: Message[];
  isLoading: boolean;
  sendMessage: (message: string) => Promise<void>;
  clearMessages: () => void;
}

const ChatContext = createContext<ChatContextType | undefined>(undefined);

export function ChatProvider({ children }: { children: React.ReactNode }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = useCallback(async (message: string) => {
    setIsLoading(true);
    try {
      setMessages(prev => [...prev, { role: 'user', content: message }]);
      const response = await apiSendMessage(message);
      setMessages(response.messages);
    } catch (error) {
      const errorMessage =
        error instanceof Error ? error.message : 'An error occurred';
      setMessages(prev => [
        ...prev,
        { role: 'assistant', content: `Error: ${errorMessage}` },
      ]);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const clearMessages = useCallback(() => {
    setMessages([]);
  }, []);

  return (
    <ChatContext.Provider value={{ messages, isLoading, sendMessage, clearMessages }}>
      {children}
    </ChatContext.Provider>
  );
}

export function useChat() {
  const context = useContext(ChatContext);
  if (!context) {
    throw new Error('useChat must be used within ChatProvider');
  }
  return context;
}
