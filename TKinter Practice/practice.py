def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
    
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)

class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        
my_Car = Car(make="Toyota", model="Sienna")