import requests
import json
import os

api_key = "YOUR_API_KEY_HERE"  # Remplacez par votre clé API OpenWeatherMap
city = None

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'City not found')}"
        
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    except requests.RequestException as e:
        return f"An error occurred: {e}"
