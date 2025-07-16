from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal
from ai_agent import get_response_from_ai_agent

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[ChatMessage]
    allow_search: bool

ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    llm_id = request.model_name
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Convert messages to the format LangGraph expects
    formatted_messages = [
        {"role": msg.role, "content": msg.content} for msg in request.messages
    ]

    try:
        response = get_response_from_ai_agent(
            llm_id,
            formatted_messages,
            allow_search,
            system_prompt,
            provider
        )
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}