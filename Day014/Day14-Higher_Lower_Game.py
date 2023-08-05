# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:32:12 2023

@author: LousadaR
"""

from art import logo,vs
from game_data import data
import random
import os 

#print(data[0]['name'])

#Global variables
score = 0 #Keep track of score
game_over = False # Flag to keep the game going or to finnish


clear = lambda: os.system('cls')

#Function to chose a random person
def pick_person(list_of_persons):
    """
    retunrs the dictionary with the person
    """
    return random.choice(list_of_persons)

def print_persons(personA, personB):
    """
    receives two dictionaries with both persons and prints the compare text
    
    """
    if personA['name'] == personB['name']:
        personB = pick_person(data)
    else:
        if score != 0:
            print(f"You are right! Current score: {score}.")
        print(f"Compare A {personA['name']}, a {personA['description']}, from {personA['country']}.")
        print(vs)
        print(f"Against B {personB['name']}, a {personB['description']}, from {personB['country']}.")
        
def compare_persons(personA,personB,player_choise):
    """
    Compares the number of followers of person a with person b and returs True if the player choise is correct
    and False if the player choise is incorrect
    """
    pA_followers = personA['follower_count']
    #print("PA followers:", pA_followers)
    pB_followers = personB['follower_count']
    #print("PB followers:", pB_followers)
    if pA_followers > pB_followers:
        winner = personA
    else:
        winner = personB
    #print("Winner is:",winner['name'])
    #print("Player choise is:",player_choise['name'] )
    if winner['name'] == player_choise['name']:
        return True
    else:
        return False

# start game
print(logo)
# select two random persons
person1 = pick_person(data)
person2 = pick_person(data)
print_persons(person1, person2)
while not game_over:
    player_input = input("Who has more followers? Type 'A' or 'B': ")
    if (player_input != 'A') and (player_input !="B"):
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    elif player_input == 'A':
        if compare_persons(person1, person2, person1):
            score += 1
            person2 = pick_person(data)
            print_persons(person1, person2)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
    else:
        if compare_persons(person1, person2, person2):
            score += 1
            person1 = pick_person(data)
            print_persons(person1, person2)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
            