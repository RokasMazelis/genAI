#

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

import random

number_to_guess = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 2
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        break



