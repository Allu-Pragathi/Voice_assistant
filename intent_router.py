from tasks import weather, google_search, summarizer, reminders,time,joke,translate

def handle_intent(intent, query):
    if intent == "weather":
        words=query.lower().split()
        city = None
        if "in" in words:
            city_index = words.index("in") + 1
            city=" ".join(words[city_index:])
        return weather.get_weather(city)  # Optionally extract city
    elif intent == "google":
        return google_search.search_google(query)
    elif intent == "summarize":
        return summarizer.summarize_text(query)
    elif intent == "reminder":
        return reminders.add_reminder(query)
    elif intent == "time":
        return time.get_current_time()
    elif intent == "joke":
        return joke.tell_joke()
    elif intent == "translate":
        return translate.translate_text(query)
    else:
        return "I didn't understand that."
