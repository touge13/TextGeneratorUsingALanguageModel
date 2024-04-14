Completed by: `Grudinin Mikhail Artemovich (Грудинин Михаил Артемович)`

# Text Generation using Hugging Face API

This project demonstrates how to generate text using the Hugging Face API. It uses a pre-trained language model to generate responses based on user input.

# Start a project

Set up your API key and model name:
Create a `config.py` file.
Add your Hugging Face API key and model name to the `config.py` file:
```
api_key = "YOUR_API_KEY"
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

max_new_tokens = 200
temperature = 0.5
top_p = 0.8
repetition_penalty = 1.2
```

Run the `main.py` script and enter your text input when prompted. The model will generate a response based on your input.
```python main.py```

# Configuration
You can customize the text generation parameters in the `config.py`:

`max_new_tokens`: Maximum number of tokens in the generated text.
`temperature`: Controls the randomness of the generated text.
`top_p`: Controls the diversity of the generated text.
`repetition_penalty`: Controls the repetition in the generated text.