from voice_input import get_voice_input
from tts import speak
from nlp_engine import detect_intent
from intent_router import handle_intent
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

def main():
    print("Starting Personal Assistant. Say 'exit' to quit.")
    while True:
        user_input = get_voice_input()
        print(f"User Input: {user_input}")
        if user_input.lower() == "exit":
            speak("Exiting the assistant.")
            break
        intent = detect_intent(user_input)
        response = handle_intent(intent, user_input)
        speak(response)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
