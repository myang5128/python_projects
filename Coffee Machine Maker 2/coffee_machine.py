class Machine():

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }

    def update(self, waterOrder, milkOrder, coffeeOrder, moneyOrder):
        self.resources['water'] -= waterOrder 
        self.resources['milk'] -= milkOrder 
        self.resources['coffee'] -= coffeeOrder 
        self.resources['money'] += moneyOrder

    def report(self):
        print("Current Resources: ")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}ml")
        print(f"Money: ${self.resources['money']}")
    
    def check(self, waterOrder, milkOrder, coffeeOrder):
        insuff = []
        insuffCheck = False
        if self.resources['water'] < waterOrder:
            insuff.append("Water")
            insuffCheck = True
        if self.resources['milk'] < milkOrder:
            insuff.append("Milk")
            insuffCheck = True
        if self.resources['coffee'] < coffeeOrder:
            insuff.append("Coffee")
            insuffCheck = True
        if insuffCheck:
            print("Insufficient item(s): \n")
            for i in range(0, len(insuff)):
                print(f"{i+1}. {insuff[i]}")
            return False
        return True
    
    def coinCount(self):
        total = 0
        quarters = input("How many quarters do you insert? ")
        while not quarters.isnumeric():
            quarters = input(f"How many quarters do you insert? ")
        total += int(quarters) * .25

        dimes = input("How many dimes do you insert? ")
        while not dimes.isnumeric():
            dimes = input(f"How many dimes do you insert? ")
        total += int(dimes) * .10

        nickels = input("How many nickels do you insert? ")
        while not nickels.isnumeric():
            nickels = input(f"How many nickels do you insert? ")
        total += int(nickels) * .05

        pennies = input("How many pennies do you insert? ")
        while not pennies.isnumeric():
            pennies = input(f"How many pennies do you insert? ")
        total += int(pennies) * .01
        return total
        