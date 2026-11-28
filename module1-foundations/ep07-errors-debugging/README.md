# Ep 7: Errors, debugging and clean projects

Code from Episode 7 of **Python for AI** on Code Mind. We take a script that crashes, read its tracebacks, find the bad data with the VS Code debugger, make it robust with `try`/`except` and `logging`, and tidy the project so anyone can run it.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run report.py
```

Expected output:

```
WARNING: line 5: no temperature for Chennai, skipped
INFO: Chennai: 26.7 C from 2 readings
INFO: Bengaluru: 23.7 C from 3 readings
INFO: Delhi: 19.6 C from 3 readings
```

- `data/weather.csv`: weather rows in the format from Episode 5, including one row where the API sent no temperature.
- `report.py`: the finished, robust script: a path that works from anywhere (`pathlib`), `try`/`except` around the risky conversion, `logging` instead of `print`, and a `main()` function behind `if __name__ == "__main__":`.
- `exceptions.ipynb`: `try`/`except` on its own, and `raise` for your own errors.
- `challenge_broken.py`: the viewer challenge (see below).

## The errors from the video

The first version of `report.py` crashes twice:

```
FileNotFoundError: [Errno 2] No such file or directory: 'weather.csv'
```

The file was moved into `data/`, and a relative path is relative to the folder you run from, not the script. `Path(__file__).parent / "data" / "weather.csv"` always points next to the script.

```
ValueError: could not convert string to float: ''
```

One row has an empty temperature. The debugger shows it: set a breakpoint on the line with `float(...)`, start debugging, and look at `row` in the Variables panel.

## Sharing the project

`pyproject.toml` and `uv.lock` are all a uv user needs (`uv sync`). For people who use pip:

```
uv export --format requirements-txt --no-hashes > requirements.txt
pip install -r requirements.txt
```

## Challenge

`challenge_broken.py` has three bugs. Run it, read each traceback from the bottom up, fix one bug at a time, and post the average humidity it prints in the comments.
