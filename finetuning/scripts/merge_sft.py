import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import os

# Paths
base_model_id = "meta-llama/Llama-3.2-3B-Instruct"
sft_adapter_path = "../models/arete-llama-3.2-3b_3/arete-llama-3.2-3b_3"
merged_model_path = "../models/arete-llama-sft-merged"

print("--- Step 1: Loading Base Model in BF16 ---")
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id, 
    torch_dtype=torch.bfloat16, 
    device_map="auto",
    trust_remote_code=True
)

print("--- Step 2: Loading SFT Adapters ---")
model = PeftModel.from_pretrained(base_model, sft_adapter_path)

print("--- Step 3: Merging Weights ---")
# This creates a single standalone model
merged_model = model.merge_and_unload()

print(f"--- Step 4: Saving Merged Model to {merged_model_path} ---")
merged_model.save_pretrained(merged_model_path)
tokenizer = AutoTokenizer.from_pretrained(base_model_id)
tokenizer.save_pretrained(merged_model_path)

print("Merge complete! You can now run the DPO script.")