# Ep 7 challenge: this script has 3 bugs.
# Run it, read each traceback from the bottom up, fix one bug at a time.
import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "weather.csv"


def average(values):
    return sum(values) / len(value)


humidity = []
with open(DATA, newline="") as f:
    for row in csv.DictReader(f):
        humidity.append(row["humidty"])

print("Average humidity:", round(average(humidity), 1))
