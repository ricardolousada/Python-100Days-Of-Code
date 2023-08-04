# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:52:33 2023

@author: LousadaR
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_choise=int(input("What do you chosse? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list_of_moves = [rock,paper,scissors]
print(list_of_moves[player_choise])
computer_choise = random.randint(0, len(list_of_moves)-1)
print("Computer chose:")
print(list_of_moves[computer_choise])
if player_choise == 0:
    if computer_choise == 1:
        print("You Lose.")
    elif computer_choise == 2:
        print("You Win.")
    else:
        print("Draw")
elif player_choise == 1:
    if computer_choise == 1:
        print("Draw")
    elif computer_choise == 2:
        print("You Lose.")
    else:
        print("You Win.")
else:
    if computer_choise == 1:
        print("You Won.")
    elif computer_choise == 2:
        print("Draw.")
    else:
        print("You Lose.")
    
