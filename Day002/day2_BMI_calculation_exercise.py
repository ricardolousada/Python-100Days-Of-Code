# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:23:54 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / (float(height) ** 2)
print(int(bmi))