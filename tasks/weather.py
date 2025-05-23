import requests
from utils.config import OPENWEATHER_API_KEY

def get_weather(city):
    api_key = "e4af72dbb82b32e8811ea925eb2c0ecb"  # <-- Add quotes
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return f"Could not find weather for {city}."
    
    weather_description = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)  # Convert from Kelvin to Celsius
    return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."

