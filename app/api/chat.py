from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import asyncio

from app.utils.llm import get_ai_response
from app.utils.resume_data import get_resume_context

router = APIRouter(prefix="/api", tags=["chat"])


class ChatMessage(BaseModel):
    """Schema for chat messages"""
    message: str
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Schema for chat responses"""
    response: str
    conversation_id: str
    status: str = "success"


class ConversationStore:
    """Simple in-memory conversation storage"""
    def __init__(self):
        self.conversations = {}
    
    def add_message(self, conversation_id: str, role: str, content: str):
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        self.conversations[conversation_id].append({
            "role": role,
            "content": content
        })
    
    def get_history(self, conversation_id: str):
        return self.conversations.get(conversation_id, [])



conversation_store = ConversationStore()


@router.post("/chat", response_model=ChatResponse)
async def chat(chat_input: ChatMessage) -> ChatResponse:
    """
    Chat endpoint that processes user messages and returns AI responses
    
    Args:
        chat_input: ChatMessage with user message
    
    Returns:
        ChatResponse with AI response
    
    Raises:
        HTTPException: If message is empty or processing fails
    """
    
    
    if not chat_input.message or not chat_input.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    user_message = chat_input.message.strip()
    
  
    conversation_id = chat_input.conversation_id or "default"
    
    try:
       
        resume_context = get_resume_context()
        
        
        conversation_history = conversation_store.get_history(conversation_id)
        
      
        try:
            ai_response = await asyncio.wait_for(
                asyncio.to_thread(
                    get_ai_response,
                    user_message,
                    resume_context,
                    conversation_history
                ),
                timeout=30.0
            )
        except asyncio.TimeoutError:
            raise HTTPException(
                status_code=504,
                detail="AI service took too long to respond. Please try again."
            )
        
        
        conversation_store.add_message(conversation_id, "user", user_message)
        conversation_store.add_message(conversation_id, "assistant", ai_response)
        
        return ChatResponse(
            response=ai_response,
            conversation_id=conversation_id,
            status="success"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing message: {str(e)}"
        )


@router.get("/chat/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Chat API is running"
    }
