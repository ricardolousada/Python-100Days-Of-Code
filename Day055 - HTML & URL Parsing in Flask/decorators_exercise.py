# Create the logging_decorator() function 👇



# Use the decorator 👇

def logging_decorator(function):
    def wrapper(*args,**kwargs):
        result = function(*args)
        print(f"You called {function.__name__} {args}")
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(n1,n2,n3):
    return n1+n2+n3

a_function(1,2,3)