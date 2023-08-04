# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:29:47 2023

@author: LousadaR
"""

#Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    num_cans = (height * width) / coverage
    num_cans_int = int(math.ceil(num_cans))
    print(f"You'll need {num_cans_int} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)