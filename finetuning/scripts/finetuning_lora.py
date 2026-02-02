import torch
import os
from datasets import load_dataset
from peft import LoraConfig
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from trl import SFTTrainer, SFTConfig
from huggingface_hub import login
from dotenv import load_dotenv

# 1. --- SETUP & AUTH ---
load_dotenv()
hf_api_key = os.getenv("HF_TOKEN")
if hf_api_key:
    login(hf_api_key)

print(f"Is CUDA available? {torch.cuda.is_available()}")

model_name = "Qwen/Qwen2.5-3B-Instruct"
output_dir = "../models/Qwen2.5-3B-arete_1"
final_file = "Qwen2.5-3B-arete_1"
fine_tuning_dataset = "../datasets/finetuning_dataset_21.json"

# 2. --- MODEL & TOKENIZER ---
bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_cfg,
    device_map="auto",                
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# 3. --- DATASET ---
dataset = load_dataset("json", data_files=fine_tuning_dataset, split="train")
dataset = dataset.shuffle(seed=42)

# 4. --- LoRA CONFIG ---
peft_cfg = LoraConfig(
    lora_alpha=256,      # Increased for better learning capacity
    lora_dropout=0.05,
    r=128,               # High rank to capture more nuance
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
)

# 5. --- TRAINING CONFIG ---
sft_cfg = SFTConfig(
    output_dir=output_dir,
    save_steps=100,
    logging_steps=10,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,   
    optim="adamw_torch_fused",       
    learning_rate=2e-4, 
    num_train_epochs=1,
    lr_scheduler_type="cosine", 
    warmup_ratio=0.03,
    max_grad_norm=0.3,
    bf16=True,
    # These parameters are now explicitly part of SFTConfig
    max_length=1024, #proly 1024 since 2048 breaks
    dataset_text_field="messages", 
    packing=False,
)

# 6. --- INITIALIZE TRAINER ---
# Removed 'tokenizer=tokenizer' to fix the TypeError.
# The SFTTrainer will use the tokenizer associated with the model 
# or you can set it via model.config if necessary.
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=sft_cfg,
    peft_config=peft_cfg,
)

# 7. --- TRAIN & SAVE ---
print("Starting the fine-tuning process...")
trainer.train()

print("Fine-tuning completed successfully!")
final_output_dir = os.path.join(output_dir, final_file)
trainer.save_model(final_output_dir)
print(f"Fine-tuned model adapters saved to {final_output_dir}")