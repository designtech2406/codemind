# Ep 7: average temperature per city, robust to bad rows
import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("report")

DATA = Path(__file__).parent / "data" / "weather.csv"


def load_temps(path):
    temps = {}
    with open(path, newline="") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            try:
                temp = float(row["temp_c"])
            except ValueError:
                log.warning("line %d: no temperature for %s, skipped", line_no, row["city"])
                continue
            city = row["city"]
            if city not in temps:
                temps[city] = []
            temps[city].append(temp)
    return temps


def main():
    try:
        temps = load_temps(DATA)
    except FileNotFoundError:
        log.error("data/weather.csv not found. Run weather.py from Episode 5 first.")
        return
    for city, values in temps.items():
        log.info("%s: %.1f C from %d readings", city, sum(values) / len(values), len(values))


if __name__ == "__main__":
    main()
