# flashcards.py

import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0

for card in data["cards"]:
    guess = input(card["q"] + " > ")

    if guess.lower() == card["a"].lower():
        score += 1
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", card["a"])
        print(f"Current score: {score}/{total}")

print(f"Thanks for playing! You scored {score}/{total} correct!")
