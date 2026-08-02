import random

print("Welcome to Virtual Dice Roller🎲!!")

while True:
    input("Please click enter to roll the dice...")

    number = random.randint(1, 6)

    print(f"You rolled the number: {number}")

    next_roll = input("Roll again? (yes/no): ").lower()

    if next_roll == "no":
        print("Thanks for playing!!")
        break