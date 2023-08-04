# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:32:43 2023

@author: LousadaR
"""

#Write your code below this line 👇
def prime_checker(number):
    flag = False
    if number == 1:
        print("It's a prime number.")
        return
    elif number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                flag=True
                break
    if flag:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)