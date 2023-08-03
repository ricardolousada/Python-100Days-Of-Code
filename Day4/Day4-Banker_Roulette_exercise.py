# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:55:11 2023

@author: LousadaR
"""
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
import random
number_of_persons=len(names)
random_payer = random.randint(0, number_of_persons-1)
print(f"{names[random_payer]} is going to buy the meal today!") 
