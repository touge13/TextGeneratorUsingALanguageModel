from config import model_name
from text_generation_request import text_generation_request, max_new_tokens

# Function to get input text from user and generate response
def generate_text():
    input_text = input("Input text: ")
    if not input_text:
        print("Input text cannot be empty. Please provide a valid input.")
        return
    prompt = f"Your configuration has {max_new_tokens} tokens, so keep it short!\nUser: {input_text}\nModel:"

    generated_text = text_generation_request(prompt, model_name)
    print("Output text:", generated_text.replace(prompt, ""))
