# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:12:46 2023

@author: LousadaR
"""

from art import logo

on = True

#add
def add(n1,n2):
    return n1 + n2

#subctract
def sub(n1,n2):
    return n1 - n2

#multiply
def mul(n1,n2):
    return n1 * n2

#divide
def div(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    
    print(logo)
    #gets the first number from the user
    num1 = float(input("What's the first number?: "))
    
    #prints all possible operations
    for operation in operations:
        print(operation)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        #calculates the result 
        function=operations[operation_symbol]
        answer = function(num1,num2)
        #prints the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()    
    
        



