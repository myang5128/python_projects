import os
# simple calculator

# basic functions
def add(n1, n2):
    return n1 + n2 

def minus(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error"
    else: 
        return n1 / n2
    
# function dictionary
operations = {
    "+": add,
    "-": minus,
    "*": mult,
    "/": divide,
}


def calculator ():
    cont = True
    # ask for inputs
    num1 = input("What's the first number?: ")
    while not num1.isnumeric():
        num1 = input("Please pick an actual number: ")
    num2 = input("What's the second number?: ")
    while not num2.isnumeric():
        num2 = input("Please pick an actual number: ")
    num1 = float(num1)
    num2 = float(num2)

    # print out available inputs
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from above: ")
    while operations.get(operation_symbol) == None:
        operation_symbol = input("Please pick an operation from above: ")

    # final
    calc = operations[operation_symbol]
    num3 = calc(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {num3}")

    while cont:
        # continue?
        goOn = input("Continue or reset? (Y, N, R): ").upper()
        while not goOn == "Y" and not goOn == "N" and not goOn == "R":
            goOn = input("Continue? (Y, N)").upper()
        if goOn == "R":
            os.system('cls')
            print("Clearing...\n")
            calculator()
        elif goOn == "N":
            cont = False
            break

        # picks next operation
        operation_symbol = input("What's your next operation: ")
        while operations.get(operation_symbol) == None:
            operation_symbol = input("Please pick  valid operation: ")

        # picks next number
        num1 = input("What's the second number?: ")
        while not num1.isnumeric():
            num1 = input("Please pick an actual number: ")
        num1 = float(num1)

        # calculation
        num2 = float(num3) 
        calc = operations[operation_symbol]
        num3 = calc(num2, num1)
        print(f"{num2} {operation_symbol} {num1} = {num3}")

    if not cont:
        print("Thank you for using the basic calculator!")

calculator()
    