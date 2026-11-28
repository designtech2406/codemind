# Ep 6: a tiny machine learning library, built with classes


class Model:
    """What every model shares: it starts unfitted and prints nicely."""

    def __init__(self):
        self.fitted = False

    def __repr__(self):
        status = "fitted" if self.fitted else "not fitted"
        return f"{type(self).__name__}({status})"


class AverageModel(Model):
    """Always predicts the average score it saw in training."""

    def fit(self, X, y):
        self.average = sum(y) / len(y)
        self.fitted = True
        return self

    def predict(self, X):
        return [round(self.average, 1) for x in X]


class LineModel(Model):
    """Fits a straight line: score = slope * hours + intercept."""

    def fit(self, X, y):
        mean_x, mean_y = sum(X) / len(X), sum(y) / len(y)
        top = sum((x - mean_x) * (v - mean_y) for x, v in zip(X, y))
        bottom = sum((x - mean_x) ** 2 for x in X)
        self.slope = top / bottom
        self.intercept = mean_y - self.slope * mean_x
        self.fitted = True
        return self

    def predict(self, X):
        return [round(self.slope * x + self.intercept, 1) for x in X]


hours = [1, 2, 3, 4, 5, 6]
scores = [52, 58, 65, 70, 78, 85]

for model in (AverageModel(), LineModel()):
    print(model)
    model.fit(hours, scores)
    print(model, model.predict([7, 8]))
