import requests
import random
import os

def generate_image():
    os.makedirs("output", exist_ok=True)
    prompts = [
        "futuristic crypto Base blockchain, dark Web3 style, high quality, no text",
        "minimalist crypto design, Base ecosystem, modern, dark theme",
        "crypto tech abstract art, Base, futuristic, Web3 vibe"
    ]
    prompt = random.choice(prompts)

    url = "https://image.pollinations.ai/prompt/" + prompt.replace(" ", "%20")
    image_data = requests.get(url).content

    with open("output/image.png", "wb") as f:
        f.write(image_data)
