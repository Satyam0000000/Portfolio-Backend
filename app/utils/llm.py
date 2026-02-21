"""
LLM integration using Hugging Face Inference API (Free)
Supports multiple free models without requiring API keys for inference
"""

import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# Using Hugging Face Inference API - Free tier available
# Models available: mistral-7b, zephyr-7b, neural-chat-7b, etc.
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")

# Alternative: Using Together.ai (also free with generous limits)
TOGETHER_API_URL = "https://api.together.xyz/inference"
TOGETHER_API_TOKEN = os.getenv("TOGETHER_API_TOKEN", "")


async def get_ai_response(
    user_message: str,
    resume_context: str,
    conversation_history: Optional[list] = None
) -> str:
    """
    Get AI response using Hugging Face Inference API (Free)
    
    Args:
        user_message: User's question/message
        resume_context: Resume data formatted as context
        conversation_history: Previous messages for context
    
    Returns:
        AI generated response
    """
    
    # Build the system prompt with resume context
    system_prompt = f"""You are an intelligent AI assistant representing Satyam Goswami, a Full Stack Developer and Cybersecurity Enthusiast. 
You have access to Satyam's resume and project information. Answer questions about his skills, experience, and projects based on the context provided.
Be professional, concise, and helpful. If you don't have information, say so honestly.

RESUME CONTEXT:
{resume_context}

Remember to be friendly and encourage people to visit the portfolio or contact directly for more detailed discussions."""

    # Try Hugging Face API first
    if HF_API_TOKEN:
        try:
            response = _get_huggingface_response(
                user_message, 
                system_prompt, 
                conversation_history
            )
            return response
        except Exception as e:
            print(f"HF API error: {e}")
    
    # Fallback to Together.ai
    if TOGETHER_API_TOKEN:
        try:
            response = _get_together_response(
                user_message, 
                system_prompt, 
                conversation_history
            )
            return response
        except Exception as e:
            print(f"Together API error: {e}")
    
    # Fallback: Rule-based response
    return _get_fallback_response(user_message, resume_context)


def _get_huggingface_response(
    user_message: str,
    system_prompt: str,
    conversation_history: Optional[list] = None
) -> str:
    """Get response from Hugging Face Inference API"""
    
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    if conversation_history:
        messages.extend(conversation_history)
    
    messages.append({"role": "user", "content": user_message})
    
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": [{"role": msg["role"], "content": msg["content"]} for msg in messages],
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.7,
            "top_p": 0.95,
        }
    }
    
    response = requests.post(HF_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    
    # Parse response based on API return format
    if isinstance(result, list) and len(result) > 0:
        return result[0].get("generated_text", "I couldn't generate a response.")
    
    return "I couldn't generate a response."


def _get_together_response(
    user_message: str,
    system_prompt: str,
    conversation_history: Optional[list] = None
) -> str:
    """Get response from Together.ai API (Free alternative)"""
    
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    if conversation_history:
        messages.extend(conversation_history)
    
    messages.append({"role": "user", "content": user_message})
    
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": messages,
        "max_tokens": 500,
        "temperature": 0.7,
    }
    
    response = requests.post(TOGETHER_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    return result.get("output", {}).get("choices", [{}])[0].get("text", "I couldn't generate a response.")


def _get_fallback_response(user_message: str, resume_context: str) -> str:
    """
    Fallback rule-based response when APIs are unavailable
    Searches resume context for keywords in the question
    """
    message_lower = user_message.lower()
    
    # Simple keyword-based responses
    if any(word in message_lower for word in ["skill", "technology", "tech", "know"]):
        return "I have expertise in React, Node.js, MongoDB, Python, and modern web development. I'm also experienced in cybersecurity and machine learning. Ask me about any specific technology!"
    
    if any(word in message_lower for word in ["experience", "work", "job", "company"]):
        return "I've worked as a Full Stack Developer at Snack Delivery, as a Cybersecurity Research Intern at IIT Ropar, and as a Freelance Developer for Tarang. I'm currently working on a Skill-Based Dating App. Would you like details about any of these?"
    
    if any(word in message_lower for word in ["project", "build", "create", "portfolio"]):
        return "My main projects include Tarang (event management platform) and Snack Delivery (food ordering platform). Both showcase my full-stack development skills. Which one interests you?"
    
    if any(word in message_lower for word in ["contact", "email", "reach", "connect"]):
        return "You can contact me at satyamgoswami2705@gmail.com. I'm always open to discussing interesting projects and opportunities!"
    
    if any(word in message_lower for word in ["hi", "hello", "hey", "greetings"]):
        return "Hello! I'm Satyam, a Full Stack Developer and Cybersecurity Enthusiast. Feel free to ask me anything about my skills, experience, or projects!"
    
    return "That's an interesting question! Feel free to ask me about my skills, experience, projects, or how to contact me. I'm here to help!"
