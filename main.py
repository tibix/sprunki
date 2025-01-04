import random

characters = [
    "Brud",
    "Clukr",
    "Durple",
    "Fun_Bot",
    "Garnold",
    "Jevin",
    "Mr_Fun_Computer",
    "Mr_Sun",
    "Mr_Tree",
    "OWACKX",
    "Oren",
    "Raddy",
    "Simon",
    "Pinky",
    "Sky",
    "Vineria",
    "Wenda",
]

random_choice = random.randint(0, len(characters) - 1)
print(f"Caracterul selectat aleator este {characters[random_choice]}")
