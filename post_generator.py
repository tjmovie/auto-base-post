from gpt4all import GPT4All

def generate_post():
    model_path = "models/gpt4all-lora-quantized.bin"
    gptj = GPT4All(model_path)

    prompt = """
Generate a fresh, human-like crypto post for the Base ecosystem.
Include:
- engaging text
- 3 relevant hashtags
- 2 emojis
- modern, fun tone
- short & viral
"""

    response = gptj.generate(prompt)
    post = response.replace("\n", " ").strip()
    return post
