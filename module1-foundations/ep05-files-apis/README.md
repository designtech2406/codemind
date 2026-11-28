# Ep 5: Files, JSON and APIs, the AI way

Code from Episode 5 of **Python for AI** on Code Mind. We read and write text, JSON and CSV files, call a live weather API with `requests`, keep API keys out of our code with `.env`, and build a dataset that grows every time the script runs.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run first_api.py
uv run weather.py
```

`first_api.py` prints `200` and the current temperature in Chennai. `weather.py` fetches the current temperature and humidity for Chennai, Bengaluru and Delhi and appends them to `weather.csv`. Run it again later and the file grows.

The weather comes from [Open-Meteo](https://open-meteo.com), which is free and needs no API key, so the numbers you see will be today's, not the ones in the video.

`files_json_csv.ipynb` has the notebook part: writing, appending and reading text files, JSON with `json.dump` and `json.load`, and CSV with `csv.DictWriter` and `csv.DictReader`. Open it in VS Code and choose the `.venv` kernel.

If you followed along in your own `python-for-ai` project, add the two new packages:

```
uv add requests python-dotenv
```

## API keys and .env

Most APIs need a key. Never type it into your code. Put it in a file called `.env` next to your script:

```
WEATHER_API_KEY=paste-your-key-here
```

`load_dotenv()` reads it and `os.getenv("WEATHER_API_KEY")` gets it. Add `.env` to `.gitignore` so it never reaches GitHub. `.env.example` shows the format without a real key.

## The error from the video

```python
print(response.json()["temperature_2m"])
```

```
KeyError: 'temperature_2m'
```

The temperature isn't at the top of the reply: it's inside `"current"`. Print the whole reply first, then index into it: `response.json()["current"]["temperature_2m"]`.

## Challenge

Ask Open-Meteo for the hourly forecast (`hourly=temperature_2m`) for your city, and save the next 10 hours (time and temperature) to `forecast.csv`. Hint: the times and temperatures are two lists inside `response.json()["hourly"]`. Post your first three rows in the comments.
