import os
from openai import OpenAI
from dotenv import load_dotenv
from rag_pipeline import retrieve_relevant_context
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from instruct_model import query_llama_cloud, session_id
from sql_related import save_to_database


device = "cuda"
embeddings_model_name = "Qwen/Qwen3-Embedding-0.6B"
db_name = "../vectorstores/ml_vstore"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name, model_kwargs={"device": device})
vectorstore = Chroma(persist_directory=db_name, embedding_function=embeddings)

load_dotenv(override=True)


with open("../system_messages/ml_system_message.txt", "r") as file:
    system_prompt = file.read()
messages=[{"role": "system", "content": system_prompt}]

# # ------------------------------ Cloud -----------------------------------
client = OpenAI(
    base_url="https://lt5s2924rgrqevma.eu-west-1.aws.endpoints.huggingface.cloud/v1",
    api_key=os.getenv("HF_TOKEN")
)

while True:
    user_prompt = input("You: ")
    rag_user_prompt = retrieve_relevant_context(vectorstore,user_prompt)
    messages.append({"role": "user", "content": rag_user_prompt})
    response = query_llama_cloud(client, stream=True, messages=messages)
    messages.append({"role": "assistant", "content": response})
    save_to_database(session_id, rag_user_prompt, response)
