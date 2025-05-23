import requests

def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url).json()
        return f"{response['setup']} ... {response['punchline']}"
    except:
        return "Sorry, I couldn't fetch a joke right now."

