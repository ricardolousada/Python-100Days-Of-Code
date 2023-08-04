# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:01:48 2023

@author: LousadaR
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
billAmmount = float(input("What was the total bill? "))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15 ? "))
numberOfPersons = int(input("How many people to split the bill? "))

percentage = round(tipPercentage/100 + 1,2)
#print("tip percentage", percentage)

payPerPerson = round((billAmmount / numberOfPersons) * percentage,2)

print(f"Each person should pay: ${payPerPerson}")