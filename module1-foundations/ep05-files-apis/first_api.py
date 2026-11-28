# Ep 5: call a web API in 5 lines
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current=temperature_2m"
response = requests.get(url, timeout=10)
print(response.status_code)
print(response.json()["current"]["temperature_2m"])
