#Number Guessing Project

from art import logo
import random

def easy_level():
    NUMBER_TO_GUESS = random.randint(1, 100)
    print("\nCool ! You have 10 credits to guess the number.")
    for tries in reversed(range(0, 10)):
        user_input = int(input("Try to guess the number: "))
        if user_input != NUMBER_TO_GUESS:
            if user_input > NUMBER_TO_GUESS:
                print("\nThe number that you have entered is greater than the number I'm thinking of.")
                print(f"You still have: {tries} credits left.\n")
            else:
                print("\nThe number that you have entered is lower than the number I'm thinking of.")
                print(f"You still have: {tries} credits left.\n")
        else:
            return print("\nWOW ! You mastered it ! Well Done !\n")

    return print("\nWell you didn't get it at this time, perhaps another time ?\n")

def hard_level():
    NUMBER_TO_GUESS = random.randint(1, 100)
    print("\nCool ! You have 5 credits to guess the number.")
    for tries in reversed(range(0, 5)):
        user_input = int(input("Try to guess the number: "))
        if user_input != NUMBER_TO_GUESS:
            if user_input > NUMBER_TO_GUESS:
                print("\nThe number that you have entered is greater than the number I'm thinking of.")
                print(f"You still have: {tries} credits left.\n")
            else:
                print("\nThe number that you have entered is lower than the number I'm thinking of.")
                print(f"You still have: {tries} credits left.\n")
        else:
            return print("\nWOW ! You mastered it ! Well Done !\n")

    return print("\nWell you didn't get it at this time, perhaps another time ?\n")


print(logo + "\n")

print("I'm thinking a number between 1 and 100 - Try to guess it ! :) ")

wrong_input = True
while wrong_input:
    user_level = input("Pick a level. Type 'easy' or 'hard': ").lower()
    if user_level != 'hard' and user_level != 'easy':
        print("That's an invalid enter.")
    else:
        wrong_input = False

if user_level == 'easy':
    easy_level()
else:
    hard_level()
