from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Claude Code iOS Backend", version="0.1.0")

# CORS configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:8000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Anthropic client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

client = Anthropic(api_key=api_key)

# In-memory conversation storage (for demo purposes)
conversations = {}


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    conversation_id: str
    message: str


class ChatResponse(BaseModel):
    conversation_id: str
    response: str
    messages: list[Message]


@app.get("/")
async def root():
    return {"message": "Claude Code iOS Backend", "version": "0.1.0"}


@app.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Send a message and get a response from Claude.
    """
    try:
        conversation_id = request.conversation_id
        user_message = request.message

        # Initialize or retrieve conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        # Add user message to history
        conversations[conversation_id].append({"role": "user", "content": user_message})

        # Get response from Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=conversations[conversation_id],
        )

        # Extract response text
        assistant_message = response.content[0].text

        # Add assistant response to history
        conversations[conversation_id].append(
            {"role": "assistant", "content": assistant_message}
        )

        # Prepare response
        return ChatResponse(
            conversation_id=conversation_id,
            response=assistant_message,
            messages=[
                Message(role=msg["role"], content=msg["content"])
                for msg in conversations[conversation_id]
            ],
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/execute-code")
async def execute_code(request: ChatRequest) -> ChatResponse:
    """
    Execute code through Claude and return the result.
    """
    try:
        conversation_id = request.conversation_id
        code_request = request.message

        # Initialize or retrieve conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        # Create a system message for code execution
        system_message = "You are a helpful assistant that executes code and returns results. When asked to execute code, provide the output."

        # Add user message
        conversations[conversation_id].append({"role": "user", "content": code_request})

        # Get response from Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            system=system_message,
            messages=conversations[conversation_id],
        )

        # Extract response text
        assistant_message = response.content[0].text

        # Add assistant response to history
        conversations[conversation_id].append(
            {"role": "assistant", "content": assistant_message}
        )

        return ChatResponse(
            conversation_id=conversation_id,
            response=assistant_message,
            messages=[
                Message(role=msg["role"], content=msg["content"])
                for msg in conversations[conversation_id]
            ],
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/new-conversation")
async def new_conversation() -> dict:
    """
    Create a new conversation.
    """
    import uuid

    conversation_id = str(uuid.uuid4())
    conversations[conversation_id] = []
    return {"conversation_id": conversation_id}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
