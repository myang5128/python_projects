from coffee_machine import Machine
from espresso import Espresso
from latte import Latte 
from cappuccino import Cappuccino

def menuCheck(menu, type):
    x = False
    for i in range(0, len(menu)):
        if menu[i] == type:
            x = True 
            break
    return x

def main():
    machine = Machine()
    espresso = Espresso()
    latte = Latte()
    cappuccino = Cappuccino()
    menu_Items = ["off", "espresso", "latte", "cappuccino"]
    
    while True:
        machine.report()
        type = input("What would you like to order? (espresso, latte, cappuccino) ").lower()
        while not menuCheck(menu_Items, type):
            type = input("What would you like to order? (espresso, latte, cappuccino) ").lower()
        
        if type == "off":
            print("Turning off...")
            exit()
        elif type == "espresso":
            type = espresso
        elif type == "latte":
            type = latte
        elif type == "cappuccino":
            type = cappuccino

        checker = machine.check(type.resources['water'], type.resources['milk'], type.resources['coffee'])
        if checker:
            coins = machine.coinCount()
            if coins >= type.resources['cost']:
                print(f"Received ${coins}. Thank you!\n")
                refund = coins - type.resources['cost']
                if refund > 0:
                    print(f"Refunding ${refund}...\n")
                    coins -= refund 
                machine.update(type.resources['water'], type.resources['milk'], type.resources['coffee'], coins)
                print(f"Serving up a cup of {type.resources['name']}, enjoy!\n")
            else:
                print("Insufficient cash. Refunding ${coins}...\n")

main()

