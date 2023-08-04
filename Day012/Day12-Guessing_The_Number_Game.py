# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:38:27 2023

@author: LousadaR
"""

from art import logo
import random

print(logo)

#Define Global Variables
input_not_correct = True
random_number_to_guess = random.randint(1, 100)
game_over = False

def make_a_guess(attemps):
    """"
    function that prints the number of attemps the player has\n
    Then asks for an input and forces the input to be a number.\n
    Finally it returns the input number.
    """
    print(f"You have {attemps} attempts to guess the number")
    is_number = False
    while not is_number:
        number = input("Make a guess: ")
        if number.isdecimal():
            is_number = True
            return int(number)
        
def is_guess_correct(number):
    """
    Function that takes a number and compares to the number to guess.
    Provides the user with the tips, too low or two hight.
    If the player guesses returns 1 to indicate that the game is over
    """
    if number < random_number_to_guess:
        print("Too Low.\nGuess again.")
    elif number > random_number_to_guess:
        print("Too High.\nGuess again.")
    else:
        print(f"You got it! the answer was {random_number_to_guess}.")
        return 1
        
    

print("Welcome to the Number Guessing Game!")
print("I'm think in a number betwin 1 and 100.")
while input_not_correct:
    difficulty = input("Choose a dificulty. Type 'easy' or 'hard':")
    if (difficulty != "easy") and (difficulty != "hard"):
        print("You may have a typo, please enter 'easy' or hard'")
    if difficulty == 'easy':
        number_of_attempts = 10
        input_not_correct = False
    if difficulty == 'hard':
        number_of_attempts = 5
        input_not_correct = False
        
#start a loop with the number of attempts
while (not game_over) and (number_of_attempts > 0):
    guess = make_a_guess(number_of_attempts)
    #Call a function to check the guess
    if is_guess_correct(guess) == 1:
        game_over = True
    number_of_attempts -= 1
else:
    if number_of_attempts < 0:
        print(f"You've run out of guesses, you lose. The answer was {random_number_to_guess}.")
    game_over = True
        

