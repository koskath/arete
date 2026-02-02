# -------------------------------- OPEN SOURCE --------------------------------
import os
import gc
import re
import glob
import torch

# 1. SET MEMORY CONFIGURATIONS (Must be first)
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# 2. DEFINE MEMORY CLEANUP
def clear_memory():
    """Forcefully clears GPU and System memory."""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()

# Clear memory immediately at start
clear_memory()

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader

# --- SETTINGS ---
device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "Qwen/Qwen3-Embedding-0.6B"
db_name = "ml_vstore"
data_path = "ML"

# 3. INITIALIZE EMBEDDINGS WITH OPTIMIZATIONS
# Using FP16 (float16) reduces VRAM usage by 50%
print(f"Loading model {model_name} onto {device}...")
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={
        "device": device,
        "trust_remote_code": True,
        "model_kwargs": {"torch_dtype": torch.float16} 
    },
    encode_kwargs={
        "batch_size": 1,  # Crucial for long docs: process one at a time
        "normalize_embeddings": True
    }
)

# 4. LOAD AND ENRICH DOCUMENTS
print("Loading documents from disk...")
folders = glob.glob(data_path)
text_loader_kwargs = {'encoding': 'utf-8'}
documents = []

for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(
        folder, 
        glob="**/*.md", 
        loader_cls=TextLoader, 
        loader_kwargs=text_loader_kwargs
    )
    folder_docs = loader.load()
    
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        source_path = doc.metadata.get("source", "")
        filename = os.path.basename(source_path)
        
        # Regex for lecture/slide IDs
        match = re.search(r"lecture_(\d+)_slide_(\d+)", filename)
        if match:
            doc.metadata["lecture_id"] = int(match.group(1))
            doc.metadata["slide_id"] = int(match.group(2))
        
        documents.append(doc)

print(f"Found {len(documents)} documents.")

# 5. SEQUENTIAL INGESTION (Avoids the 1.92 GiB Allocation Spike)
print(f"Starting ingestion into {db_name}...")

if not documents:
    print("No documents found. Exiting.")
else:
    # Initialize the vectorstore with the first document
    vectorstore = Chroma.from_documents(
        documents=[documents[0]],
        embedding=embeddings,
        persist_directory=db_name
    )

    # Add the rest one by one to keep VRAM usage flat
    for i in range(1, len(documents)):
        try:
            vectorstore.add_documents([documents[i]])
            
            # Progress tracking and periodic cleanup
            if i % 10 == 0:
                print(f"Progress: {i}/{len(documents)} documents ingested.")
                clear_memory()
                
        except torch.cuda.OutOfMemoryError:
            print(f"OOM triggered on doc {i}. Attempting emergency recovery...")
            clear_memory()
            # Retry once after clearing memory
            vectorstore.add_documents([documents[i]])

    print(f"SUCCESS: Vectorstore created with {vectorstore._collection.count()} documents.")