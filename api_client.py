import os
import requests
from dotenv import load_dotenv

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=pl"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data["main"]["temp"])
        print(data["main"]["feels_like"])
load_dotenv()
key = os.getenv("key")
get_weather("Bochnia")