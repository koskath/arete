import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import os

# 1. --- PATHS ---
# This is the merged SFT model you created before starting DPO
merged_sft_model_path = "../models/arete-llama-sft-merged"
# This is where your DPO trainer saved the final adapters
dpo_adapter_path = "../models/arete-llama-3.2-3b_3_dpo_final/final_dpo_adapter"
# This is the final, ready-to-use model folder
final_model_path = "../models/arete-llama-3.2-3b-final"

print("--- Step 1: Loading Merged SFT Model in BF16 ---")
# Use BF16 for high precision during the merge
base_model = AutoModelForCausalLM.from_pretrained(
    merged_sft_model_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

print("--- Step 2: Loading DPO Adapters ---")
model = PeftModel.from_pretrained(base_model, dpo_adapter_path)

print("--- Step 3: Merging DPO weights ---")
final_merged_model = model.merge_and_unload()

print(f"--- Step 4: Saving Final Model to {final_model_path} ---")
final_merged_model.save_pretrained(final_model_path)
tokenizer = AutoTokenizer.from_pretrained(merged_sft_model_path)
tokenizer.save_pretrained(final_model_path)

print("Success! Your final DPO-aligned model is ready.")