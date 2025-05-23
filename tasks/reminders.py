import json
import os

REMINDER_FILE = "reminders.json"

def add_reminder(text):
    reminder = text.replace("reminder", "").replace("remind me to", "").strip()
    reminders = []
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            reminders = json.load(f)
    reminders.append(reminder)
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f)
    return f"Reminder added: {reminder}"
