# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:24:44 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year % 4 != 0:
    print("Not leap year.")
elif year % 100 != 0:
    print("Leap year.")
elif year % 400 !=0:
    print("Not leap year.")
else:
    print("Leap year.")
    
    