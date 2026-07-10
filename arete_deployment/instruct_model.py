from transformers import TextIteratorStreamer
from threading import Thread
import torch
import secrets
import string
import asyncio
import os
from dotenv import load_dotenv

# Generate a unique 16-character alphanumeric session ID
session_id = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

async def query_llama_cloud(client, stream, messages):
    """
    Query the LLM cloud API asynchronously.
    
    Args:
        client: OpenAI client instance
        stream (bool): Whether to stream the response
        messages: List of message dictionaries
    
    Returns:
        str: The full response from the LLM
    """
    # Run the synchronous API call in a thread pool to avoid blocking
    loop = asyncio.get_event_loop()
    
    if stream:
        # For streaming, we need to handle it differently
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="Koskath/arete-llama-3.2-3b_5", 
                messages=messages,
                temperature=0.3,
                max_tokens=500,
                stream=True,
            )
        )
        
        # Handle streaming response
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
        return full_response
    else:
        # Non-streaming response
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="Koskath/arete-llama-3.2-3b_5", 
                messages=messages,
                temperature=0.3,
                max_tokens=500,
                stream=False,
            )
        )
        return response.choices[0].message.content


async def query_llama_cloud_stream(client, messages):
    """
    Query the LLM cloud API asynchronously with streaming support.
    Yields chunks of the response as they arrive.
    
    Args:
        client: OpenAI client instance
        messages: List of message dictionaries
    
    Yields:
        str: Chunks of the response content
    """
    import queue as thread_queue
    import threading
    
    loop = asyncio.get_event_loop()
    chunk_queue = thread_queue.Queue()
    exception_holder = [None]
    
    def process_stream():
        """Process the synchronous stream and put chunks in the thread-safe queue"""
        try:
            stream = client.chat.completions.create(
                model="Koskath/arete-llama-3.2-3b_5", 
                messages=messages,
                temperature=0.3,
                max_tokens=500,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if delta and delta.content is not None:
                        chunk_queue.put(delta.content)
            # Signal completion
            chunk_queue.put(None)
        except Exception as e:
            import traceback
            print(f"Error in process_stream: {e}")
            print(traceback.format_exc())
            exception_holder[0] = e
            chunk_queue.put(None)
    
    # Start processing stream in executor
    loop.run_in_executor(None, process_stream)
    
    # Yield chunks from queue
    while True:
        # Use run_in_executor to wait for queue.get() which is blocking
        chunk = await loop.run_in_executor(None, chunk_queue.get)
        if chunk is None:
            if exception_holder[0]:
                raise exception_holder[0]
            break
        yield chunk


async def query_codestral(messages):
    """
    Query the Codestral LLM via Mistral API directly with streaming support.
    Yields chunks of the response as they arrive.
    
    Args:
        messages: List of message dictionaries
    
    Yields:
        str: Chunks of the response content
    """
    import queue as thread_queue
    import threading
    from mistralai import Mistral
    
    # Load environment variables
    load_dotenv(override=True)
    
    loop = asyncio.get_event_loop()
    chunk_queue = thread_queue.Queue()
    exception_holder = [None]
    
    def process_stream():
        """Process the synchronous stream and put chunks in the thread-safe queue"""
        try:
            # Initialize Mistral client with API key from environment
            mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
            
            # Call Mistral API with streaming
            stream = mistral_client.chat.stream(
                model="codestral-2405",
                messages=messages,
            )
            
            for chunk in stream:
                content = chunk.data.choices[0].delta.content
                if content:
                    # Ensure content is properly encoded as UTF-8 string
                    if isinstance(content, bytes):
                        content = content.decode('utf-8')
                    chunk_queue.put(str(content))
            # Signal completion
            chunk_queue.put(None)
        except Exception as e:
            import traceback
            print(f"Error in process_stream: {e}")
            print(traceback.format_exc())
            exception_holder[0] = e
            chunk_queue.put(None)
    
    # Start processing stream in executor
    loop.run_in_executor(None, process_stream)
    
    # Yield chunks from queue
    while True:
        # Use run_in_executor to wait for queue.get() which is blocking
        chunk = await loop.run_in_executor(None, chunk_queue.get)
        if chunk is None:
            if exception_holder[0]:
                raise exception_holder[0]
            break
        yield chunk


async def query_ft_mistral(messages):
    """
    Query the Ministral-3b-latest LLM via Mistral API directly with streaming support.
    Yields chunks of the response as they arrive.
    
    Args:
        messages: List of message dictionaries
    
    Yields:
        str: Chunks of the response content
    """
    import queue as thread_queue
    import threading
    from mistralai import Mistral
    
    # Load environment variables
    load_dotenv(override=True)
    
    loop = asyncio.get_event_loop()
    chunk_queue = thread_queue.Queue()
    exception_holder = [None]
    
    def process_stream():
        """Process the synchronous stream and put chunks in the thread-safe queue"""
        try:
            # Initialize Mistral client with API key from environment
            mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
            mistral_ft_model = os.getenv("MISTRAL_NEMO_FINETUNED")
            # Call Mistral API with streaming
            stream = mistral_client.chat.stream(
                model=mistral_ft_model,
                messages=messages,
            )
            
            for chunk in stream:
                content = chunk.data.choices[0].delta.content
                if content:
                    # Ensure content is properly encoded as UTF-8 string
                    if isinstance(content, bytes):
                        content = content.decode('utf-8')
                    chunk_queue.put(str(content))
            # Signal completion
            chunk_queue.put(None)
        except Exception as e:
            import traceback
            print(f"Error in process_stream: {e}")
            print(traceback.format_exc())
            exception_holder[0] = e
            chunk_queue.put(None)
    
    # Start processing stream in executor
    loop.run_in_executor(None, process_stream)
    
    # Yield chunks from queue
    while True:
        # Use run_in_executor to wait for queue.get() which is blocking
        chunk = await loop.run_in_executor(None, chunk_queue.get)
        if chunk is None:
            if exception_holder[0]:
                raise exception_holder[0]
            break
        yield chunk


