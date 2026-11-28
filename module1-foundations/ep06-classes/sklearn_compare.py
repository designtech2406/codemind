# Ep 6: the same job with scikit-learn
from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5], [6]]   # scikit-learn wants one list of features per row
scores = [52, 58, 65, 70, 78, 85]

model = LinearRegression()
model.fit(hours, scores)
print(model.predict([[7], [8]]).round(1))
print(round(model.coef_[0], 2), round(model.intercept_, 2))
