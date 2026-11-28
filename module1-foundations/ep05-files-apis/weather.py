# Ep 5: live weather for three cities, saved as a growing dataset
import csv
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()                                   # copies the lines of .env into environment variables
API_KEY = os.getenv("WEATHER_API_KEY")          # Open-Meteo needs no key, but most APIs do
print("API key loaded:", API_KEY is not None)

URL = "https://api.open-meteo.com/v1/forecast"
CITIES = {"Chennai": (13.08, 80.27), "Bengaluru": (12.97, 77.59), "Delhi": (28.61, 77.21)}


def get_weather(lat, lon):
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m,relative_humidity_2m"}
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()                 # stop with a clear error if the request failed
    return response.json()["current"]


new_file = not os.path.exists("weather.csv")
with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if new_file:
        writer.writerow(["time", "city", "temp_c", "humidity"])
    for city, (lat, lon) in CITIES.items():
        now = get_weather(lat, lon)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), city, now["temperature_2m"], now["relative_humidity_2m"]])
        print(f"{city}: {now['temperature_2m']} C, {now['relative_humidity_2m']}% humidity")
