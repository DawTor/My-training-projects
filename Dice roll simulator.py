import random

if __name__ == '__main__':
    while True:
        question = input("Do you want to roll dice?(yes/no): ")

        if question == "yes":
            roll = random.randint(1, 6)
            print(f"Dice shows {roll}")

        else:
            break
    print("Bye!")

#Easier way to write this code (Thanks to https://github.com/DanielChabrowski)
#import random

#if __name__ == '__main__':
#   while input('Do you want to roll dice?(yes/no): ') == 'yes':
#       roll = random.randint(1, 6)
#       print(f"Dice shows {roll}")
#   print("Bye!")
