# Ep 1: Python for AI setup in 10 minutes

Code from Episode 1 of **Python for AI** on Code Mind. Two ways to run it.

## Google Colab (nothing to install)

Open [colab.research.google.com](https://colab.research.google.com), upload `colab_first_ai.ipynb`, and run the cells with Shift+Enter. For the GPU cell, choose Runtime → Change runtime type → T4 GPU first.

## VS Code + uv (your own machine)

Install uv:

```
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Run this folder's code:

```
uv python install 3.12
uv sync
uv run main.py
```

Expected output: `Average model score: 88.5`

Then open `hello_ai.ipynb` in VS Code, click **Select Kernel**, and choose `.venv`.

To build the same project from scratch, as in the video:

```
uv init --no-package python-for-ai
cd python-for-ai
uv add numpy pandas matplotlib ipykernel
```

`--no-package` makes uv create `main.py`. Plain `uv init` in recent versions creates a `src/` folder instead.

## Challenge

In the last cell of `hello_ai.ipynb`, change `hours = 7` to any number and post your predicted score in the comments. Expected result for 7 hours: 91.0.
