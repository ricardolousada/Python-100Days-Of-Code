# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:03:09 2023

@author: LousadaR
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters = ""
pass_symbols = ""
pass_numbers = ""

# get the random letters
for i in range(0,nr_letters):
    pass_letters += letters[random.randint(0, len(letters)-1)]
#print(pass_letters)

# get the random sysmbols
for i in range(0,nr_symbols):
    pass_symbols += symbols[random.randint(0, len(symbols)-1)]
#print(pass_symbols)

# get the random numbers
for i in range(0,nr_numbers):
    pass_numbers += numbers[random.randint(0, len(numbers)-1)]
#print(pass_numbers)

easy_pass = pass_letters + pass_symbols + pass_numbers
print("easy_password is: ", easy_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_of_characters_in_pass = []
#create a list of all characters in the password
for c in easy_pass:
    list_of_characters_in_pass.append(c)

#print(list_of_characters_in_pass)

# create a list of numebers from o to nº characters in the password
list_of_numbers = [i for i in range(0,len(list_of_characters_in_pass))]
#print(list_of_numbers)

#shuffle the list
random.shuffle(list_of_numbers)
#print(list_of_numbers)

#loops trhough the new shuffled list and creates the hard password
hard_pass = ""
for number in list_of_numbers:
    hard_pass += list_of_characters_in_pass[number]
print("hard_password is: ", hard_pass)

#Podia ter usado random.choice(listas)
# random.choice(symbols)
#tambem podia ter usado o .shuffle na lista de caracteres da password
