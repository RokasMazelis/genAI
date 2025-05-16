# Does not handle 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")
print("Jei nori pabaigti žaidimą, įvesk 'end'.")

import random

number_to_guess = random.randint(1, 20)
attempts = 0


while True:
        user_input = input("Enter your guess, or ""	end"" to quit: ")
        
        if user_input == "end":
            print("Game over")
            break
        if not user_input.isdigit():
            print("Įvesk skaičių nuo 1 iki 20 arba 'end'. ")
            continue
        
        guess = int(user_input)

        if not 1 <= user_input <= 20:
            print ("Ivedei nesamone, jei nori pabaigti žaidimą įvesk - end: ")
            continue
            
        print(f"You guessed: {user_input}")
        attempts += 1

        if user_input < number_to_guess:
            print("Too low! Try again.")
        elif user_input > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
print(f"Then number was : = {number_to_guess}")
