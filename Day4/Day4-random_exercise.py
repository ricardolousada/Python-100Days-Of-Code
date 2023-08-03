# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:51:23 2023

@author: LousadaR
"""

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

number = random.randint(0, 1)
if number == 1:
    print("Heads.")
else:
    print("Tails.")