# Ep 2: Variables, types and math, the AI way

Code from Episode 2 of **Python for AI** on Code Mind. We calculate a spam filter's accuracy by hand, and find out why accuracy alone can lie.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run accuracy.py
uv run check_model.py
```

Expected output of `accuracy.py`:

```
Spam filter v1 accuracy: 0.86
Spam filter v1: 86.0% accurate
Ready to ship? False
Lazy model: 90.0% accurate, spam caught: 0 of 20
Accuracy: 86.0%  Recall: 70.0%
```

Open `types_and_math.ipynb` in VS Code and choose the `.venv` kernel to try types, operators, `0.1 + 0.2` and type conversion one cell at a time.

If you followed along in your own `python-for-ai` project from Episode 1, just add these files to it. No new packages are needed.

## The error from the video

Without `int(...)`, `check_model.py` fails:

```
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

`input()` always returns text, even when you type a number. Wrap it in `int()` to turn it into a number.

## Challenge

Spam filter v1 has `tp = 14` (spam caught) and `fp = 22` (normal emails wrongly flagged). Precision is the share of flagged emails that really were spam:

```
precision = tp / (tp + fp)
```

Add it to `accuracy.py`, print it as a percentage with one decimal, and post your answer in the comments.
