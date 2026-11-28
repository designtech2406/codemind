# Ep 6: Classes behind every AI library

Code from Episode 6 of **Python for AI** on Code Mind. We build a tiny machine learning library with classes, two models with `fit` and `predict`, and then do the same job with scikit-learn to see why every ML library looks the way it does.

## Run it

You need uv and Python 3.12 from [Episode 1](../ep01-setup/).

```
uv sync
uv run tiny_model.py
uv run sklearn_compare.py
```

Expected output of `tiny_model.py`:

```
AverageModel(not fitted)
AverageModel(fitted) [68.0, 68.0]
LineModel(not fitted)
LineModel(fitted) [91.0, 97.6]
```

And `sklearn_compare.py` finds the same line:

```
[91.  97.6]
6.57 45.0
```

- `classes.ipynb`: your first class (`Sensor`), `__init__`, `self`, methods, and a method that returns `self` so calls can be chained.
- `tiny_model.py`: a base class `Model` (shared `__repr__`), and two models that inherit from it, each with `fit(X, y)` and `predict(X)`.
- `sklearn_compare.py`: scikit-learn's `LinearRegression` with the same data.

If you followed along in your own `python-for-ai` project, add scikit-learn:

```
uv add scikit-learn
```

## The error from the video

Forget `self` in a method:

```python
def describe():
    return f"{self.room}: {self.temp} C"
```

```
TypeError: Sensor.describe() takes 0 positional arguments but 1 was given
```

When you call `bedroom.describe()`, Python passes `bedroom` in as the first argument. A method must accept it, and by convention that argument is called `self`.

## Challenge

Add a `score(X, y)` method to the `Model` base class that returns the **mean absolute error**: the average of how far each prediction is from the real value. Because it's in the base class, both models get it for free. Score both models on the training data and post your two numbers in the comments. Which model is better?
