"""
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

#First class objects, can be passed as arguments e.g int/string/flot

def calculate(calc_function,n1,n2):
   return calc_function(n1,n2)

print(calculate(add,5,10))
print(calculate(mul,5,10))

# Nested function
def outer_function():
    print("I'm outter")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()
"""

# Functions can be returned from other functions

def outer_function():
    print("I'm outter")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()

#Python decorators
import time
def delay_decorator(function):
    def wrapper_function():
        # do something before the function execution
        time.sleep(2)
        function()
        function()
        #Do something after the function
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")


def say_greatting():
    print("greatiing")

decotared_function = delay_decorator(say_greatting)
decotared_function()

say_greatting()
say_hello()
