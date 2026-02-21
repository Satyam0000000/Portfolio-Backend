# Portfolio AI Chat Agent Backend

A FastAPI-based backend service that powers an intelligent chat agent answering questions about Satyam Goswami's resume, experience, and projects.

## Features

- 🤖 **Free AI Integration**: Uses Hugging Face Inference API (free tier)
- 💬 **Conversation Management**: Maintains chat history for context-aware responses
- 📋 **Resume Knowledge Base**: Structured resume data for accurate information
- 🚀 **Fast & Scalable**: Built with FastAPI for high performance
- 🔄 **CORS Enabled**: Ready for frontend integration

## Free AI Services Used

### Primary: Hugging Face Inference API
- **Cost**: Free tier available with generous limits
- **Model**: Mistral-7B-Instruct (open-source)
- **Signup**: https://huggingface.co/

### Fallback: Together.ai
- **Cost**: Free tier available
- **Models**: Multiple open-source options
- **Signup**: https://www.together.ai/

### Fallback: Rule-based Response
- Keyword-based responses when APIs are unavailable
- Always has a fallback response

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone/Navigate to Backend Folder**
```bash
cd Backend
```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Get Free API Keys**

   **Option A: Hugging Face (Recommended)**
   - Go to https://huggingface.co/
   - Sign up for free account
   - Navigate to Settings → Access Tokens
   - Create a new token (can be read-only)
   - Copy your token

   **Option B: Together.ai**
   - Go to https://www.together.ai/
   - Sign up for free
   - Get your API key from dashboard

5. **Configure Environment**
```bash
cp .env.example .env
```

Edit `.env` and add your API token:
```
HF_API_TOKEN=hf_your_token_here
FRONTEND_URL=http://localhost:5173
```

### Running the Server

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### POST /api/chat
Chat with the AI agent

**Request:**
```json
{
  "message": "What are your skills?",
  "conversation_id": "user_123"
}
```

**Response:**
```json
{
  "response": "I have expertise in React, Node.js, MongoDB...",
  "conversation_id": "user_123",
  "status": "success"
}
```

### GET /health
Health check endpoint

### GET /api/chat/health
Chat service health check

## Resume Data Structure

The AI agent uses structured resume data from `app/utils/resume_data.py`:

```
- Personal Info (name, contact, bio)
- Skills (languages, frontend, backend, databases, tools)
- Experience (job titles, companies, dates, achievements)
- Projects (name, description, technologies, links)
- Education
- Interests
```

Easily update this file to reflect any changes in your resume.

## Development

### Project Structure
```
Backend/
├── app/
│   ├── api/
│   │   └── chat.py          # Chat endpoint
│   └── utils/
│       ├── llm.py           # LLM integration
│       └── resume_data.py   # Resume knowledge base
├── main.py                  # FastAPI app
├── requirements.txt         # Dependencies
├── .env.example             # Environment template
└── README.md               # This file
```

### Adding New Endpoints

Edit `app/api/chat.py` to add new endpoints to the router.

### Customizing Resume Data

Edit `app/utils/resume_data.py` to update:
- Skills
- Experience
- Projects
- Contact information

### Changing AI Model

In `app/utils/llm.py`, change the model URL:
```python
HF_API_URL = "https://api-inference.huggingface.co/models/MODEL_NAME"
```

Available free models:
- `mistralai/Mistral-7B-Instruct-v0.2`
- `mistralai/Mistral-7B-Instruct-v0.1`
- `HuggingFaceH4/zephyr-7b-beta`
- `meta-llama/Llama-2-7b-chat-hf` (requires acceptance)

## Deployment

### Free Hosting Options

1. **Render** (Recommended)
   - https://render.com/
   - Free tier available
   - Supports Python/FastAPI

2. **Railway**
   - https://railway.app/
   - Free credits for new users
   - Easy Python deployment

3. **PythonAnywhere**
   - https://www.pythonanywhere.com/
   - Free tier available
   - Python-specific

4. **Replit**
   - https://replit.com/
   - Free hosting with generous limits

### Deployment Steps

1. Push your Backend folder to GitHub
2. Connect repository to hosting platform
3. Set environment variables in platform dashboard
4. Deploy

## Troubleshooting

### "HF API error: Invalid token"
- Check your HF_API_TOKEN is correct
- Make sure token is in `.env` file
- Verify token hasn't expired

### "Connection timeout"
- Check internet connection
- Hugging Face service might be down
- Try fallback responses (no API needed)

### CORS Issues
- Update FRONTEND_URL in `.env`
- Ensure frontend makes requests to correct backend URL

### Slow Responses
- Hugging Face free tier might be slow
- Try Together.ai alternative
- Increase timeout in chat.py

## Free Resources

- **Hugging Face**: https://huggingface.co/
- **Together.ai**: https://www.together.ai/
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Python Requests**: https://requests.readthedocs.io/

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, contact: satyamgoswami2705@gmail.com
