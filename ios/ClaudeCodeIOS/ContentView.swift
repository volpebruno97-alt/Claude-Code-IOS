import SwiftUI

struct ContentView: View {
    @EnvironmentObject var viewModel: ChatViewModel
    @State private var messageInput: String = ""

    var body: some View {
        VStack {
            // Header
            VStack {
                Text("Claude Code")
                    .font(.title2)
                    .fontWeight(.bold)
                Text(viewModel.conversationId.prefix(8) + "...")
                    .font(.caption)
                    .foregroundColor(.gray)
            }
            .frame(maxWidth: .infinity)
            .padding()
            .background(Color(.systemGray6))

            // Message List
            ScrollViewReader { proxy in
                ScrollView {
                    VStack(alignment: .leading, spacing: 12) {
                        ForEach(viewModel.messages) { message in
                            MessageBubble(message: message)
                        }
                    }
                    .padding()
                    .onChange(of: viewModel.messages.count) { _ in
                        if let lastMessage = viewModel.messages.last {
                            proxy.scrollTo(lastMessage.id)
                        }
                    }
                }
            }

            // Input Area
            VStack(spacing: 0) {
                Divider()
                HStack {
                    TextField("Type a message...", text: $messageInput)
                        .textFieldStyle(.roundedBorder)
                        .disabled(viewModel.isLoading)

                    Button(action: sendMessage) {
                        if viewModel.isLoading {
                            ProgressView()
                                .scaleEffect(0.8)
                        } else {
                            Image(systemName: "paperplane.fill")
                        }
                    }
                    .disabled(messageInput.trimmingCharacters(in: .whitespaces).isEmpty || viewModel.isLoading)
                }
                .padding()
            }
            .background(Color(.systemBackground))
        }
    }

    private func sendMessage() {
        let trimmedMessage = messageInput.trimmingCharacters(in: .whitespaces)
        guard !trimmedMessage.isEmpty else { return }

        Task {
            await viewModel.sendMessage(trimmedMessage)
            messageInput = ""
        }
    }
}

struct MessageBubble: View {
    let message: ChatMessage

    var body: some View {
        HStack {
            if message.role == "user" {
                Spacer()
                VStack(alignment: .trailing, spacing: 4) {
                    Text(message.content)
                        .foregroundColor(.white)
                        .padding(12)
                        .background(Color.blue)
                        .cornerRadius(8)
                }
            } else {
                VStack(alignment: .leading, spacing: 4) {
                    Text(message.content)
                        .foregroundColor(.black)
                        .padding(12)
                        .background(Color(.systemGray5))
                        .cornerRadius(8)
                }
                Spacer()
            }
        }
        .id(message.id)
    }
}

#Preview {
    ContentView()
        .environmentObject(ChatViewModel())
}
