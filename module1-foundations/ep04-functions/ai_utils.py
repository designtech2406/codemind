# Ep 4: your own module of reusable AI helpers


def clean(values: list, low: float = -100) -> list:
    """Drop missing readings (None) and error codes below low."""
    return [v for v in values if v is not None and v > low]


def normalize(values: list[float], digits: int = 2) -> list[float]:
    """Scale numbers to 0..1 by dividing by the largest."""
    biggest = max(values)
    return [round(v / biggest, digits) for v in values]


if __name__ == "__main__":
    print(normalize([2, 4, 8]))
