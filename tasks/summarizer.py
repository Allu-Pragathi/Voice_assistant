import openai
from utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this:\n{text}"}]
    )
    return response.choices[0].message["content"]
