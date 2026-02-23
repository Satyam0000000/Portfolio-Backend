import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


HF_API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")


TOGETHER_API_URL = "https://api.together.xyz/inference"
TOGETHER_API_TOKEN = os.getenv("TOGETHER_API_TOKEN", "")


def get_ai_response(
    user_message: str,
    resume_context: str,
    conversation_history: Optional[list] = None
) -> str:
    """
    Get AI response using Hugging Face Router Inference API
    
    Args:
        user_message: User's question/message
        resume_context: Resume data formatted as context
        conversation_history: Previous messages for context
    
    Returns:
        AI generated response
    """
    
    
    system_prompt = f"""
You are Satyam Goswami’s personal AI assistant.

Identity:
- Name: Satyam Goswami
- Role: AI-focused Full Stack Developer, Ex-AI/ML Research Intern at IIT Ropar
- Education: B.Tech, NIT Jalandhar (2023–2027)

Rules you MUST follow:
- Always answer in first person (“I built…”, “I worked…”).
- Be confident, specific, and resume-grounded.
- NEVER reply with generic phrases like “Feel free to ask” or “That’s an interesting question”.
- If the user greets (hi/hello/hloo), respond with a strong self-introduction using my background.
- If unsure, ask a clarifying question instead of giving a vague response.

RESUME CONTEXT:
{resume_context}

Preferred closing style:
- Invite the user to explore projects, internships, or contact details naturally (not pushy).
"""

    
    if user_message.lower().strip() in ["hi", "hello", "hloo", "hey", "hola"]:
        return (
            "Hi! I’m Satyam Goswami, a full-stack developer and Ex-AI/ML research intern at IIT Ropar, "
            "currently pursuing my B.Tech at NIT Jalandhar. I’ve built production-grade platforms like "
            "Tarang and worked on AI-based UAV intrusion detection systems. "
            "What would you like to know — projects, internships, or technical skills?"
        )

   
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
    
   
    return _get_fallback_response(user_message, resume_context)


def _get_huggingface_response(
    user_message: str,
    system_prompt: str,
    conversation_history: Optional[list] = None
) -> str:
    """Get response from Hugging Face Router Inference API"""
    
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
            "temperature": 0.4,
            "top_p": 0.95,
        }
    }
    
    response = requests.post(HF_API_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    
    result = response.json()
    
    
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
        "temperature": 0.4,
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
    
    
    if any(word in message_lower for word in ["skill", "technology", "tech", "know"]):
        return "I have expertise in React, Node.js, MongoDB, Python, and modern web development. I'm also experienced in cybersecurity and machine learning. Ask me about any specific technology!"
    
    if any(word in message_lower for word in ["experience", "work", "job", "company"]):
        return "I've worked as a Full Stack Developer at Snack Delivery, as a Cybersecurity Research Intern at IIT Ropar, and as a Freelance Developer for Tarang. I'm currently working on a Skill-Based Dating App. Would you like details about any of these?"
    
    if any(word in message_lower for word in ["project", "build", "create", "portfolio"]):
        return "My main projects include Tarang (event management platform) and Snack Delivery (food ordering platform). Both showcase my full-stack development skills. Which one interests you?"
    
    if any(word in message_lower for word in ["contact", "email", "reach", "connect"]):
        return "You can contact me at satyamgoswami2705@gmail.com. I'm always open to discussing interesting projects and opportunities!"
    
    if any(word in message_lower for word in ["hi", "hello", "hey", "greetings"]):
        return (
            "Hi! I’m Satyam Goswami, a full-stack developer at NIT Jalandhar and former AI/ML research intern at IIT Ropar. "
            "I work on AI-driven security systems, full-stack web platforms, and real-world products like Tarang. "
            "What would you like to explore?"
        )
    
    return (
        "I can help you with my projects (Tarang, Snack Delivery), my AI research at IIT Ropar, "
        "or my technical skills in React, Node.js, ML, and cybersecurity. "
        "Could you tell me what you’d like to focus on?"
    )
