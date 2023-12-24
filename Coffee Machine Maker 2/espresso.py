class Espresso():
    def __init__(self):
        self.resources = {
            "name": "espresso",
            "water": 50,
            "milk": 0,
            "coffee": 18,
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