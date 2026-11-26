# Ep 3: lists, dicts and comprehensions, the AI way
# Temperature readings from a room sensor. Some are broken:
# None = no reading, -999 = sensor error.

readings = [21.5, None, 22.1, -999, 21.8]

# The long way: a for loop
clean = []
for r in readings:
    if r is not None and r > -100:
        clean.append(r)
print("Loop:         ", clean)

# The same thing in one line: a list comprehension
clean = [r for r in readings if r is not None and r > -100]
print("Comprehension:", clean)

fahrenheit = [round(r * 9 / 5 + 32, 1) for r in clean]
print("Fahrenheit:   ", fahrenheit)
print(f"Average: {sum(clean) / len(clean):.1f} C")
