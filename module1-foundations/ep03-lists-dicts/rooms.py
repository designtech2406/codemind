# Ep 3: one dictionary, three rooms

rooms = {
    "bedroom": [21.5, None, 22.1, -999, 21.8],
    "kitchen": [24.0, 24.6, None, 25.1],
    "balcony": [-999, 29.4, 30.2, 31.0],
}

for room, values in rooms.items():
    good = [v for v in values if v is not None and v > -100]
    print(f"{room}: {sum(good) / len(good):.1f} C from {len(good)} readings")

room = input("Which room? ")
print(room, "readings:", rooms.get(room.lower(), "no such room"))
