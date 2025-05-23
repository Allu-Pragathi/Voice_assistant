from transformers import pipeline

translator =pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
  # You can change to other language pair

def translate_text(text):
    translated = translator(text, max_length=40)[0]['translation_text']
    return f"Translated: {translated}"
