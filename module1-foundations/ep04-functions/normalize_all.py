# Ep 4: one function, three datasets
from ai_utils import clean, normalize

temps = clean([21.5, None, 22.1, -999, 21.8])
scores = [52, 58, 65, 70, 78, 85]
prices = [45, 62, 38, 90, 75]   # house prices, in lakh

print("Temps: ", normalize(temps))
print("Scores:", normalize(scores))
print("Prices:", normalize(prices, digits=1))
