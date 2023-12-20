import Data
import random
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def main():
    streak = 0
    cont = True

    while cont:
        choice1 = random.choice(list(Data.data))
        choice2 = random.choice(list(Data.data))
        while choice2["name"] == choice1["name"]:
            choice2 = random.choice(list(Data.data))

        print(logo)
        print(f"Your current winstreak: {streak}\n")
        print(f"{choice1['name']}, a {choice1['description']}, from {choice1['country']}.")
        print(vs)
        print(f"{choice2['name']}, a {choice2['description']}, from {choice2['country']}.")

        if choice1["follower_count"] > choice2["follower_count"]:
            correct = choice1["name"]
        else:
            correct = choice2["name"]


        guess = input("Who has the highest follower count on Instagram? (A, B, name) ").upper()
        while guess != "A" and guess != "B" and guess != choice1["name"] and guess != choice2["name"]:
            guess = input("Who has the highest follower count on Instagram? (A, B, name) ").upper()

        if guess == "A":
            guess = choice1["name"]
        elif guess == "B":
            guess = choice2["name"]

        print(f"correct: {correct}\n")
        print(f"guess: {guess}\n")
        
        if guess == correct:
            print(f"Congratulations, {correct} was correct!\n")
            streak += 1
            os.system('cls')
        else:
            print(f"Sorry! {correct} was the correct answer. Your highest win streak was {streak}!\n")
            cont = False

def code():
    main()

    restart = input("Do you want to play again? (Y, N) ").upper()
    while restart != "N" and restart != "Y":
        restart = input("Do you want to restart? (Y, N) ").upper()
    if restart == "N":
        print("Thank you for playing!")
    elif restart == "Y":
        os.system('cls')
        code()

code()