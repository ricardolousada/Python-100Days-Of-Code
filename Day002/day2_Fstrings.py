# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:29:55 2023

@author: LousadaR
"""

#calculations

print(round(8/3,2))
print(8 // 3) #returns an integer

result = 4 / 2
result /= 2
print(result)

score = 0
score += 1
print(score)

score = 0
score /= 1
print(score)

score = 0
score *= 1
print(score)


#f strings
score = 0
height = 1.8
isWinnig = True

print(f"score is: {score} your height is {height} and you are {isWinnig}")