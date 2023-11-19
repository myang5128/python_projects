import os

# os.system('cls')

print("Welcome to the Secret Auction!\n")
cont = True
dic = {}
max = 0
winner = ""
while(cont):
    name = input("What is your name?\n")
    price = int(input("How much are you willing to bid?\n"))
    dic[name] = price
    check = input("Is there another bidder? (Y, N)\n").upper()
    if check == "Y":
        os.system('cls')
    else:
        cont = False 
for key in dic:
    if dic[key] > max:
        max = dic[key]
        winner = key 
print(f"The winner of this auction is {winner} with ${max}!")