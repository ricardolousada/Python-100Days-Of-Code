# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:30:49 2023

@author: LousadaR
"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    
}

#print(programming_dictionary["Bug"])

programming_dictionary["loop"] = "The action of doing something over and over"

#print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionaty
#programming_dictionary = {}


#edit a ditct
programming_dictionary["Bug"] = "Change the value"
#print(programming_dictionary)

#Loop trhoug a dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


