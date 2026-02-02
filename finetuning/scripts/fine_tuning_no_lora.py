import torch
import os
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer, SFTConfig
from huggingface_hub import login
from dotenv import load_dotenv

# 1. --- SETUP & AUTH ---
load_dotenv()
hf_api_key = os.getenv("HF_TOKEN")
if hf_api_key:
    login(hf_api_key)

model_name = "Qwen/Qwen2.5-0.5B-Instruct"
output_dir = "./arete-qwen"
final_file = "arete-qwen-0.5b-full"
fine_tuning_dataset = "instruct_finetuning.json"

# 2. --- LOAD MODEL & TOKENIZER ---
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.bfloat16,  # 'dtype' instead of 'torch_dtype'
    device_map="auto",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# 3. --- LOAD DATASET ---
dataset = load_dataset("json", data_files=fine_tuning_dataset, split="train")

# 4. --- CONFIGURE SFTConfig ---
# Note: max_length and dataset_text_field belong here in latest TRL
sft_cfg = SFTConfig(
    output_dir=output_dir,
    dataset_text_field="messages",
    max_length=512,               # Use max_length instead of max_seq_length
    packing=False,
    per_device_train_batch_size=1, 
    gradient_accumulation_steps=16,
    learning_rate=2e-5,
    num_train_epochs=3,
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    bf16=True,
    logging_steps=10,
    save_steps=100,
    optim="adamw_torch",
    report_to="none",
)

# 5. --- INITIALIZE TRAINER ---
# Note: 'tokenizer' is now 'processing_class'
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=sft_cfg,
    processing_class=tokenizer,   # This is the new name for the tokenizer argument
)

print("Starting FULL fine-tuning process...")
trainer.train()

# 6. --- SAVE EVERYTHING ---
final_output_dir = os.path.join(output_dir, final_file)
print(f"Saving final model to {final_output_dir}...")

trainer.save_model(final_output_dir)
tokenizer.save_pretrained(final_output_dir)

print("Process completed successfully!")