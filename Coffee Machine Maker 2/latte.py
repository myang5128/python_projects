class Latte():
    def __init__(self):
        self.resources = {
            "name": "latte",
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "cost": 1.5,
        }
    
    def getWater(self):
        return self.resources['water']
    
    def getMilk(self):
        return self.resources['milk']
    
    def getCoffee(self):
        return self.resources['coffee']
    
    def getCost(self):
        return self.resources['cost']
    