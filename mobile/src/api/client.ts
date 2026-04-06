import axios, { AxiosInstance } from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_BASE_URL = 'http://localhost:8000';
const CONVERSATION_ID_KEY = 'conversation_id';

export interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export interface ChatRequest {
  conversation_id: string;
  message: string;
}

export interface ChatResponse {
  conversation_id: string;
  response: string;
  messages: Message[];
}

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  async initializeConversation(): Promise<string> {
    const existing = await AsyncStorage.getItem(CONVERSATION_ID_KEY);
    if (existing) {
      return existing;
    }

    const response = await this.client.post<{ conversation_id: string }>(
      '/new-conversation'
    );
    const conversationId = response.data.conversation_id;
    await AsyncStorage.setItem(CONVERSATION_ID_KEY, conversationId);
    return conversationId;
  }

  async getConversationId(): Promise<string> {
    const stored = await AsyncStorage.getItem(CONVERSATION_ID_KEY);
    if (!stored) {
      return this.initializeConversation();
    }
    return stored;
  }

  async sendMessage(message: string): Promise<ChatResponse> {
    const conversationId = await this.getConversationId();
    const response = await this.client.post<ChatResponse>('/chat', {
      conversation_id: conversationId,
      message,
    });
    return response.data;
  }

  async executeCode(code: string): Promise<ChatResponse> {
    const conversationId = await this.getConversationId();
    const response = await this.client.post<ChatResponse>('/execute-code', {
      conversation_id: conversationId,
      message: code,
    });
    return response.data;
  }

  setBaseURL(url: string) {
    this.client.defaults.baseURL = url;
  }
}

export const apiClient = new ApiClient();

export const initializeConversation = () => apiClient.initializeConversation();
export const sendMessage = (message: string) => apiClient.sendMessage(message);
export const executeCode = (code: string) => apiClient.executeCode(code);
