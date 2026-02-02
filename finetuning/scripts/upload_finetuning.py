from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1. Load the base model in high precision (BF16)
base_model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-3B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# 2. Load your fine-tuned adapters
model = PeftModel.from_pretrained(base_model, "../fine-tuning/arete-llama-3.2-3b_2/arete-llama-3.2-3b_2")

# 3. Merge adapters into the base weights
merged_model = model.merge_and_unload()

# 4. Save and Push
repo_id = "Koskath/arete-llama-3.2-3b"
merged_model.push_to_hub(repo_id)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")
tokenizer.push_to_hub(repo_id)