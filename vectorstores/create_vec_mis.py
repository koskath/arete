# -------------------------------- MISTRAL --------------------------------
import os
import glob
import getpass
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("MISTRAL_API_KEY")


model_name = "codestral-embed"
db_name = "iot_vstore"  
embeddings = MistralAIEmbeddings(model=model_name)
folders = glob.glob("IoT")
text_loader_kwargs = {'encoding': 'utf-8'}

documents = []
for folder in folders:
    # Check if folder exists to avoid errors if path is wrong
    if os.path.isdir(folder):
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
        folder_docs = loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)
    else:
        print(f"Warning: Folder '{folder}' not found.")

if documents:
    # 4. Create Vectorstore
    vectorstore = Chroma.from_documents(
        documents=documents, 
        embedding=embeddings, 
        persist_directory=db_name
    )
    print(f"Vectorstore created at '{db_name}' with {vectorstore._collection.count()} documents")
else:
    print("No documents found to index.")


















# -------------------------------- no metadata --------------------------------
# model_name = "Qwen/Qwen3-Embedding-0.6B"
# db_name = "sc_vstore"

# embeddings = HuggingFaceEmbeddings(model_name=model_name, model_kwargs={"device": device}, encode_kwargs={"batch_size": 4})

# folders = glob.glob("../vectorstore_content/SC")
# text_loader_kwargs = {'encoding': 'utf-8'}

# documents = []
# for folder in folders:
#     doc_type = os.path.basename(folder)
#     loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
#     folder_docs = loader.load()
#     for doc in folder_docs:
#         doc.metadata["doc_type"] = doc_type
#         documents.append(doc)


# vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=db_name)
# print(f"Vectorstore created with {vectorstore._collection.count()} documents")

