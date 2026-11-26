# Ep 3: Lists, dicts and comprehensions, the AI way

Code from Episode 3 of **Python for AI** on Code Mind. We clean messy sensor readings in one line, and meet the four collections every AI project uses: lists, tuples, dictionaries and sets.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run clean_readings.py
uv run rooms.py
```

Expected output of `clean_readings.py`:

```
Loop:          [21.5, 22.1, 21.8]
Comprehension: [21.5, 22.1, 21.8]
Fahrenheit:    [70.7, 71.8, 71.2]
Average: 21.8 C
```

Open `collections.ipynb` in VS Code and choose the `.venv` kernel to try lists, slicing, tuples, dictionaries and sets one cell at a time.

If you followed along in your own `python-for-ai` project, just add these files to it. No new packages are needed.

## The error from the video

If the last line of `rooms.py` uses `rooms[room]` and you type `Kitchen` with a capital K, you get:

```
KeyError: 'Kitchen'
```

Dictionary keys must match exactly. `rooms.get(room.lower(), "no such room")` makes the name lower case first, and returns a message instead of crashing when the room doesn't exist.

## Challenge

Count how often each word appears in this sentence, using a dictionary:

```
sentence = "the model saw the data and the model learned"
```

Hint: `sentence.split()` gives you a list of words. Post your dictionary in the comments.
