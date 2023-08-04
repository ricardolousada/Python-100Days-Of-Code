# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:40:41 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

yearsTo90 = 90 - int(age)
#print("yearsto90:", yearsTo90)
months = yearsTo90 * 12
#print("monhts:", months)
weeks = yearsTo90 * 52
#print("weeks: ", weeks)
days = yearsTo90 * 365
#print("days: ", days)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

