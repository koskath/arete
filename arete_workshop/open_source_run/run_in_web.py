import gradio as gr
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


def chat_response(message, history):
    """Generate a streaming response for Gradio chat interface."""
    # Format the conversation history + new message
    messages = []
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": message})
    
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
    
    # Stream the output token by token
    response = ""
    for token in streamer:
        response += token
        yield response


# Load model and tokenizer once at startup
model, tokenizer, device = load_model_and_tokenizer()

# Create Gradio interface
demo = gr.ChatInterface(
    fn=chat_response,
    title="Llama-3.2-1B-Instruct Chatbot",
    description=f"Chat with Llama-3.2-1B-Instruct model running on {device.upper()}",
    examples=["Hello! How are you?", "What is machine learning?", "Explain quantum computing"],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch(share=False)
