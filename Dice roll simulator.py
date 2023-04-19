import random

while True:

    roll = random.randint(1, 6)

    question = input("Do you want to roll dice?(yes/no): ")

    if question == "yes":
        print(f"Dice shows {roll}")
    else:
        break
print("Bye!")
