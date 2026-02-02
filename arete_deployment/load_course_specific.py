"""
Module to handle course-specific configuration for system messages and vectorstores.
"""
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from typing import Tuple

# Load environment variables
load_dotenv(override=True)


def load_course_config(course: str) -> Tuple[str, Chroma]:
    """
    Load the system message and vectorstore for a specific course.
    
    Args:
        course: Course name - either "ml" (Machine Learning), "sc" (Supply Chain Management), or "iot" (Internet of Things)
    
    Returns:
        Tuple of (system_prompt, vectorstore)
    
    Raises:
        ValueError: If course is not "ml", "sc", or "iot"
    """
    # Normalize course name to lowercase
    course = course.lower()
    
    if course == "ml":
        system_message_path = "../system_messages/ml_system_message.txt"
        db_name = "../vectorstores/ml_vstore"
        embeddings_model_name = "Qwen/Qwen3-Embedding-0.6B"
    elif course == "sc":
        system_message_path = "../system_messages/sc_system_message.txt"
        db_name = "../vectorstores/sc_vstore"
        embeddings_model_name = "Qwen/Qwen3-Embedding-0.6B"
    elif course == "iot":
        system_message_path = "../system_messages/iot_system_message.txt"
        db_name = "../vectorstores/iot_vstore"
        embeddings_model_name = "mistralai/codestral-embed"
    else:
        raise ValueError(f"Invalid course: {course}. Must be 'ml', 'sc', or 'iot'")
    
    # Load system prompt
    with open(system_message_path, "r") as file:
        system_prompt = file.read()
    
    # Initialize embeddings and vectorstore
    if course == "iot":
        # Use MistralAI embeddings for IoT (codestral-embed)
        embeddings = MistralAIEmbeddings(model="codestral-embed")
    else:
        # Use HuggingFace embeddings for ML and SC
        device = "cuda"
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name, model_kwargs={"device": device})
    
    vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)
    
    return system_prompt, vectorstore

