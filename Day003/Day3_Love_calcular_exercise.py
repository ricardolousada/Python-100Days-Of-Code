# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:57:11 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1Lower = name1.lower()
name2Lower = name2.lower()

tScore = name1Lower.count("t") + name2Lower.count("t")
rScore = name1Lower.count("r") + name2Lower.count("r")
uScore = name1Lower.count("u") + name2Lower.count("u")
eScore = name1Lower.count("e") + name2Lower.count("e")

trueScore = tScore + rScore + uScore + eScore
print("True Score",trueScore)

lScore = name1Lower.count("l") + name2Lower.count("l")
oScore = name1Lower.count("o") + name2Lower.count("o")
vScore = name1Lower.count("v") + name2Lower.count("v")
eScore = name1Lower.count("e") + name2Lower.count("e")

loveScore = lScore + oScore + vScore + eScore
print("love Score", loveScore)

totalScoreString = str(trueScore) + str(loveScore)
totalScoreNumber = int(totalScoreString)
print("total score string",totalScoreString)
print("total score number", totalScoreNumber)

if totalScoreNumber < 10 or totalScoreNumber > 90:
    print(f"Your score is {totalScoreNumber}, you go together like coke and mentos.")
elif totalScoreNumber >= 40 and totalScoreNumber <= 50:
    print(f"Your score is {totalScoreNumber}, you are alright together.")
else:
    print(f"Your score is {totalScoreNumber}.")
    


