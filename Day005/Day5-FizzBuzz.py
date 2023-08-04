# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 11:55:45 2023

@author: LousadaR
"""

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz.")
    elif number % 3 == 0:
        print("Fizz.")
    elif number % 5 == 0:
        print("Buzz.")
    else:
        print(number)
        
        