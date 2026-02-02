import os
import secrets
import string
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv
from rag_pipeline import retrieve_relevant_context, retrieve_relevant_context_mistral
from instruct_model import query_llama_cloud_stream, query_codestral, query_ft_mistral
from sql_related import save_to_database, update_feedback
from load_course_specific import load_course_config
import asyncio
import json

# Load environment variables
load_dotenv(override=True)

# Initialize FastAPI app
app = FastAPI(title="Chat Bot API")

# Add CORS middleware
# In production, you should restrict allow_origins to specific domains
# Set ALLOWED_ORIGINS environment variable (comma-separated) to restrict access
# Example: ALLOWED_ORIGINS=https://arete.cbs.dk,https://www.arete.cbs.dk
allowed_origins_env = os.getenv("ALLOWED_ORIGINS")
if allowed_origins_env and allowed_origins_env != "*":
    allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
else:
    allowed_origins = ["*"]  # Allow all origins (less secure, but works for network access)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://lt5s2924rgrqevma.eu-west-1.aws.endpoints.huggingface.cloud/v1",
    api_key=os.getenv("HF_TOKEN")
)

# Store conversation history per session and course
# Format: {(session_id, course): [messages]}
conversation_history = {}

# Cache for course-specific configurations
# Format: {course: (system_prompt, vectorstore)}
course_config_cache = {}


# Pydantic models for request/response
class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None
    course: Optional[str] = "ml"  # Default to "ml" for backward compatibility

class FeedbackUpdate(BaseModel):
    record_id: int
    feedback: str  # "Chosen" or "Rejected"


@app.post("/chat/stream")
async def chat_stream_endpoint(chat_message: ChatMessage):
    """
    Streaming chat endpoint that processes user messages and streams AI responses.
    """
    async def generate():
        try:
            # Normalize course name
            course = chat_message.course.lower() if chat_message.course else "ml"
            if course not in ["ml", "sc", "iot"]:
                raise ValueError(f"Invalid course: {course}. Must be 'ml', 'sc', or 'iot'")
            
            # Load course-specific configuration (with caching)
            if course not in course_config_cache:
                system_prompt, vectorstore = load_course_config(course)
                course_config_cache[course] = (system_prompt, vectorstore)
            else:
                system_prompt, vectorstore = course_config_cache[course]
            
            # Use provided session_id or generate a new one
            if chat_message.session_id:
                current_session_id = chat_message.session_id
            else:
                # Generate a unique 16-character alphanumeric session ID
                current_session_id = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
            
            # Send session_id as first message
            yield f"data: {json.dumps({'type': 'session_id', 'session_id': current_session_id})}\n\n"
            
            # Create a unique key for this session and course combination
            session_key = (current_session_id, course)
            
            # Initialize conversation history for this session and course if not exists
            if session_key not in conversation_history:
                conversation_history[session_key] = [
                    {"role": "system", "content": system_prompt}
                ]
            
            # Retrieve relevant context using RAG (use mistral function for IoT, regular for others)
            if course == "iot":
                rag_user_prompt = retrieve_relevant_context_mistral(vectorstore, chat_message.message)
            else:
                rag_user_prompt = retrieve_relevant_context(vectorstore, chat_message.message)
            
            # Add user message to conversation history
            conversation_history[session_key].append(
                {"role": "user", "content": rag_user_prompt}
            )
            
            # Stream the LLM response (use codestral for IoT, llama for others)
            full_response = ""
            if course == "iot":
                async for chunk in query_codestral(
                    messages=conversation_history[session_key]
                ):
                    full_response += chunk
                    # Flush each chunk immediately - ensure UTF-8 encoding
                    yield f"data: {json.dumps({'type': 'chunk', 'content': chunk}, ensure_ascii=False)}\n\n"
            else:
                # async for chunk in query_llama_cloud_stream(
                #     client, 
                #     messages=conversation_history[session_key]
                # ):
                #     full_response += chunk
                #     # Flush each chunk immediately
                #     yield f"data: {json.dumps({'type': 'chunk', 'content': chunk})}\n\n"
                
                # Optional: Use query_ft_mistral instead of query_llama_cloud_stream
                async for chunk in query_ft_mistral(
                    messages=conversation_history[session_key]
                ):
                    full_response += chunk
                    # Flush each chunk immediately - ensure UTF-8 encoding
                    yield f"data: {json.dumps({'type': 'chunk', 'content': chunk}, ensure_ascii=False)}\n\n"
            
            # Add assistant response to conversation history
            conversation_history[session_key].append(
                {"role": "assistant", "content": full_response}
            )
            
            # Convert course to uppercase for database (ML, SC, or IOT)
            course_db = course.upper()
            
            # Save to database and get record_id
            record_id = await save_to_database(current_session_id, rag_user_prompt, full_response, course=course_db)
            
            # Send completion signal with record_id
            yield f"data: {json.dumps({'type': 'done', 'record_id': record_id})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"
    
    return StreamingResponse(
        generate(), 
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable nginx buffering if present
        }
    )


@app.post("/chat/feedback")
async def update_chat_feedback(feedback_update: FeedbackUpdate):
    """
    Update feedback for a chat message.
    """
    try:
        success = await update_feedback(feedback_update.record_id, feedback_update.feedback)
        if success:
            return {"status": "success", "message": "Feedback updated successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to update feedback")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

