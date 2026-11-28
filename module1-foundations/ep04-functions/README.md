# Ep 4: Functions and modules, the AI way

Code from Episode 4 of **Python for AI** on Code Mind. We write one `normalize()` function, put it in our own module, and reuse it on three different datasets.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run normalize_all.py
```

Expected output:

```
Temps:  [0.97, 1.0, 0.99]
Scores: [0.61, 0.68, 0.76, 0.82, 0.92, 1.0]
Prices: [0.5, 0.7, 0.4, 1.0, 0.8]
```

- `ai_utils.py` is your own module: `clean()` (the comprehension from Episode 3) and `normalize()`, with type hints and docstrings. Run it directly (`uv run ai_utils.py`) and its self-test under `if __name__ == "__main__":` prints `[0.25, 0.5, 1.0]`; when another file imports it, the test is skipped.
- `normalize_all.py` imports both and uses them on temperatures, exam scores and house prices.
- `functions.ipynb` has the notebook part: `def` and `return`, print vs return, default and keyword arguments, returning several values, and `lambda` (including top-k predictions). Open it in VS Code and choose the `.venv` kernel.

If you followed along in your own `python-for-ai` project, just add these files to it. No new packages are needed.

## The error from the video

If you forget `return`, a function gives back `None`:

```python
def accuracy(correct, total):
    correct / total

result = accuracy(172, 200)
print(result * 100)
```

```
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

Add `return` in front of `correct / total` and it prints `86.0`.

## Challenge

Add a `minmax(values)` function to `ai_utils.py` that scales numbers so the smallest becomes 0 and the largest becomes 1:

```
(value - smallest) / (largest - smallest)
```

Run it on `scores` and post your list in the comments. Bonus: what happens if every value is the same? Make your function handle it.
