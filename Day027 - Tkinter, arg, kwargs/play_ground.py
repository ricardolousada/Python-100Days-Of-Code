def add(*args):
    print(args[0])

    result = 0
    for n in args:
        result += n
    return result

print(add(5,10,15,20))

def calculate (n,**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5)

class Car():

    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan",model="GTR")
my_car2 = Car(make="Nissan")
print(my_car.model)
print(my_car2.model)