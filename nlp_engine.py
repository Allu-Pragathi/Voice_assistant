import spacy
nlp = spacy.load("en_core_web_sm")

def detect_intent(text):
    text = text.lower()
    if "weather" in text:
        return "weather"
    elif "reminder" in text or "remind" in text:
        return "reminder"
    elif "open" in text or "google" in text or "search" in text:
        return "google"
    elif "summarize" in text:
        return "summarize"
    elif "time" in text :
        return "time"
    elif "news" in text:
        return "news"
    elif "joke" in text:
        return "joke"
    elif "translate" in text:
        return "translate"
    else:
        return "unknown"
