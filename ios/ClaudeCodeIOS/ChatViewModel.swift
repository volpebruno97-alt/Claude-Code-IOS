import Foundation

struct ChatMessage: Identifiable {
    let id = UUID()
    let role: String
    let content: String
}

struct ChatRequest: Codable {
    let conversation_id: String
    let message: String
}

struct ChatResponse: Codable {
    let conversation_id: String
    let response: String
    let messages: [ChatMessage]
}

struct APIMessage: Codable {
    let role: String
    let content: String
}

struct APIChatResponse: Codable {
    let conversation_id: String
    let response: String
    let messages: [APIMessage]
}

class ChatViewModel: ObservableObject {
    @Published var messages: [ChatMessage] = []
    @Published var isLoading = false
    @Published var conversationId: String = ""
    @Published var apiBaseURL: String = "http://localhost:8000"

    init() {
        Task {
            await createNewConversation()
        }
    }

    func createNewConversation() async {
        do {
            guard let url = URL(string: "\(apiBaseURL)/new-conversation") else {
                throw URLError(.badURL)
            }

            var request = URLRequest(url: url)
            request.httpMethod = "POST"

            let (data, _) = try await URLSession.shared.data(for: request)
            let response = try JSONDecoder().decode([String: String].self, from: data)

            DispatchQueue.main.async {
                self.conversationId = response["conversation_id"] ?? ""
            }
        } catch {
            print("Error creating conversation: \(error)")
        }
    }

    func sendMessage(_ message: String) async {
        DispatchQueue.main.async {
            self.messages.append(ChatMessage(role: "user", content: message))
            self.isLoading = true
        }

        do {
            guard let url = URL(string: "\(apiBaseURL)/chat") else {
                throw URLError(.badURL)
            }

            let chatRequest = ChatRequest(
                conversation_id: conversationId,
                message: message
            )

            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            request.httpBody = try JSONEncoder().encode(chatRequest)

            let (data, _) = try await URLSession.shared.data(for: request)
            let response = try JSONDecoder().decode(APIChatResponse.self, from: data)

            DispatchQueue.main.async {
                self.messages = response.messages.map {
                    ChatMessage(role: $0.role, content: $0.content)
                }
                self.isLoading = false
            }
        } catch {
            DispatchQueue.main.async {
                self.messages.append(
                    ChatMessage(role: "assistant", content: "Error: \(error.localizedDescription)")
                )
                self.isLoading = false
            }
        }
    }
}
