# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:38:21 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    price = 15
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

if add_pepperoni == "Y":
    if size == "S":
        price = price + 2
    else:
        price = price + 3

if extra_cheese == "Y":
    price = price + 1

print(f"Your final bill is: ${price}.")
        
    