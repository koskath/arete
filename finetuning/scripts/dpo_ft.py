import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from peft import LoraConfig
from trl import DPOTrainer, DPOConfig
from huggingface_hub import login
from dotenv import load_dotenv

# 1. --- SETUP & AUTH ---
load_dotenv()
if not torch.cuda.is_available():
    raise RuntimeError("CUDA is not available. Please check your setup.")

# Using your 32GB VRAM card
print(f"Using GPU: {torch.cuda.get_device_name(0)}")

merged_model_path = "../models/arete-llama-sft-merged"
dataset_path = "new_dpo_ft.json"
output_dir = "../models/arete-llama-3.2-3b_3_dpo_final"

# 2. --- LOAD MERGED MODEL (4-BIT QLoRA) ---
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

print(f"Loading merged SFT model from: {merged_model_path}")
model = AutoModelForCausalLM.from_pretrained(
    merged_model_path,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(merged_model_path)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "left"  # Crucial for DPO

# 3. --- DPO LoRA CONFIG ---
peft_config = LoraConfig(
    r=128,
    lora_alpha=256,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)

# 4. --- DATASET ---
dataset = load_dataset("json", data_files=dataset_path, split="train")
dataset = dataset.shuffle(seed=42)


def format_conversational_dpo(example):
    # Ensure 'chosen' and 'rejected' are lists of messages (Conversational Format)
    return {
        "prompt": example["prompt"],
        "chosen": [example["chosen"]] if isinstance(example["chosen"], dict) else example["chosen"],
        "rejected": [example["rejected"]] if isinstance(example["rejected"], dict) else example["rejected"],
    }

dataset = dataset.map(format_conversational_dpo)

# 5. --- DPO CONFIGURATION ---
# NOTE: 'loss_type' belongs here in newer TRL versions
dpo_args = DPOConfig(
    output_dir=output_dir,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=16,
    learning_rate=5e-6,
    num_train_epochs=1,
    lr_scheduler_type="cosine",
    logging_steps=5,
    save_steps=50,
    bf16=True,
    beta=0.1,
    max_prompt_length=512,
    max_length=1024,
    gradient_checkpointing=True,
    remove_unused_columns=False,
    loss_type="sigmoid", # MOVED HERE
)

# 6. --- INITIALIZE TRAINER ---
trainer = DPOTrainer(
    model=model,
    ref_model=None,
    args=dpo_args,
    train_dataset=dataset,
    processing_class=tokenizer, # Use 'processing_class' or 'tokenizer' depending on version
    peft_config=peft_config,
)

# 7. --- TRAIN ---
print("Starting DPO training...")
trainer.train()

# Save final DPO adapters
final_adapter_path = os.path.join(output_dir, "final_dpo_adapter")
trainer.save_model(final_adapter_path)
print(f"DPO completed! Adapters saved to {final_adapter_path}")