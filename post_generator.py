import requests
import os
import json

API_KEY = "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"  # Replace with your key
MODEL = "Llama 3.3 70B Versatile"
ENDPOINT = f"https://api.groq.com/openai/v1/models/{MODEL}:generateContent?key={API_KEY}"

def generate_post():
    prompt = """
Generate a fresh, human-like crypto post for the Base ecosystem.
Include:
- engaging text
- 3 relevant hashtags
- 2 emojis
- modern, fun tone
- short & viral
"""

    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.9,
            "topK": 1,
            "topP": 1,
            "maxOutputTokens": 512
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    result = response.json()
    post_text = result['candidates'][0]['content']['parts'][0]['text']
    return post_text
