import data

def askForCoffee():
    order = input("What would you like? (espresso, latte, cappuccino) ").lower()
    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "off":
        order = input("What would you like? (espresso, latte, cappuccino) ").lower()
    return order

def report():
    # global water, milk, coffee, money
    print(f"Water: {data.resources['water']}ml \nMilk: {data.resources['milk']}ml \nCoffee: {data.resources['coffee']}ml \nMoney: ${data.resources['money']}\n")

def check(type):
    insuff = []
    if data.resources["water"] < data.MENU[type]["ingredients"]["water"] or data.resources["milk"] < data.MENU[type]["ingredients"]["milk"] or data.resources["coffee"] < data.MENU[type]["ingredients"]["coffee"]:
        if data.resources["water"] < data.MENU[type]["ingredients"]["water"]:
            insuff.append("water")
        if data.resources["milk"] < data.MENU[type]["ingredients"]["milk"]:
            insuff.append("milk")
        if data.resources["coffee"] < data.MENU[type]["ingredients"]["coffee"]:
            insuff.append("coffee")
        print(f"There is not enough {insuff}")
        return False 
    return True

def takeMoney():
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

def update(type):
    data.resources["water"] -= data.MENU[type]["ingredients"]["water"]
    data.resources["coffee"] -= data.MENU[type]["ingredients"]["coffee"]
    data.resources["milk"] -= data.MENU[type]["ingredients"]["milk"]
    data.resources["money"] += data.MENU[type]["cost"]

def main():
    cont = True
    while cont:
        report()
        order = askForCoffee()
        if order == "off":
            print("Turning off...")
            exit()
        else:
            checkEnough = check(order)
            if checkEnough:
                cash = takeMoney()
                if cash >= data.MENU[order]["cost"]:
                    print(f"Received: ${cash}, thank you!\n")
                    if cash - data.MENU[order]["cost"] > 0:
                        print(f"Refunding ${cash - data.MENU[order]['cost']}\n")
                    update(order)
                    print(f"Serving {order}, thank you for your business!\n")
                else:
                    print("Insufficient cash. Refunding...\n")

                
main()

