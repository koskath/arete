import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
from threading import Thread


def get_device():
    """Device Agnostic Code for running the model on the best available device."""
    if torch.cuda.is_available():
        return "cuda", torch.float16
    elif torch.backends.mps.is_available():
        return "mps", torch.float32  # MPS works better with float32
    else:
        return "cpu", torch.float32


def load_model_and_tokenizer():
    """Load the Llama-3.2-1B-Instruct model and tokenizer from Hugging Face."""
    model_name = "meta-llama/Llama-3.2-1B-Instruct"
    device, dtype = get_device()
    
    print(f"Loading model: {model_name}...")
    print(f"Using device: {device} with dtype: {dtype}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Use device_map="auto" for CUDA, manual placement for MPS/CPU
    if device == "cuda":
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map="auto",
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            device_map=None,
        )
        model = model.to(device)
    
    print("Model loaded successfully!")
    return model, tokenizer, device


def format_prompt(user_input):
    """Format the user input according to Llama-3.2 chat template."""
    messages = [
        {"role": "user", "content": user_input}
    ]
    return messages


def stream_response(model, tokenizer, messages, device):
    """Stream the model's response token by token."""
    # Format the messages using the tokenizer's chat template
    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    # Tokenize the input
    inputs = tokenizer(formatted_prompt, return_tensors="pt")
    # Move inputs to the same device as the model
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    # Create a streamer
    streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    
    # Generation parameters
    generation_kwargs = {
        **inputs,
        "max_new_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.9,
        "do_sample": True,
        "streamer": streamer,
    }
    
    # Start generation in a separate thread
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()
    
    # Stream the output
    print("Assistant: ", end="", flush=True)
    for token in streamer:
        print(token, end="", flush=True)
    print()  # New line after streaming is complete


def main():
    """Main function to run the interactive chat."""
    model, tokenizer, device = load_model_and_tokenizer()
    
    print("\n" + "="*50)
    print("Llama-3.2-1B-Instruct Chat Interface")
    print(f"Running on device: {device}")
    print("Type 'quit' or 'exit' to end the conversation")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            messages = format_prompt(user_input)
            stream_response(model, tokenizer, messages, device)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            break


if __name__ == "__main__":
    main()
