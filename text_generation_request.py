import requests
from config import api_key, max_new_tokens, temperature, top_p, repetition_penalty

# Function to send a request for text generation
def text_generation_request(input_text, model_name):
    # Define the API URL
    url = f"https://api-inference.huggingface.co/models/{model_name}"
    
    # Define request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define request payload
    payload = {
        "inputs": input_text,
        "parameters": {
            "max_new_tokens": max_new_tokens,         # Maximum number of tokens in generated text
            "temperature": temperature,               # Controls randomness of generated text
            "top_p": top_p,                           # Controls diversity of generated text
            "repetition_penalty": repetition_penalty  # Controls repetition in generated text
        }
    }
    
    try:
        # Send POST request to Hugging Face API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        generated_text = response_json[0].get("generated_text") if response_json else "Hmm.. Blank answer, please make sure the question asked is correct."
    
    except requests.exceptions.RequestException as e:
        print("Failed to generate text:", e)
        generated_text = "Failed to generate text. Please try again later."
    
    return generated_text
