class Cappuccino():
    def __init__(self):
        self.resources = {
            "name": "cappuccino",
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "cost": 3,
        }
    
    def getWater(self):
        return self.resources['water']
    
    def getMilk(self):
        return self.resources['milk']
    
    def getCoffee(self):
        return self.resources['coffee']
    
    def getCost(self):
        return self.resources['cost']