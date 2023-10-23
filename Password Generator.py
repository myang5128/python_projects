import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

total_length = num_letters + num_numbers + num_symbols

total_list = ["X"] * total_length

password = []

for n in range(0, total_length):
    if num_letters > 0:
        password += random.choice(letters)
        num_letters -= 1
    elif num_symbols > 0:
        password += random.choice(symbols)
        num_symbols -= 1
    elif num_numbers > 0:
        password += random.choice(numbers)
        num_numbers -= 1
random.shuffle(password)
finalPass = "" 
for char in password:
    finalPass += char
print(finalPass)
