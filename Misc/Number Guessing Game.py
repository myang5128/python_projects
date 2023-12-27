import random

def diffPicker():
    numGuesses = 0
    print("Welcome to the Number Guessing Game!\n")
    difficulty = input("What difficulty do you want? (EASY, MEDIUM, HARD)\n").upper()
    while (difficulty != "EASY") and (difficulty != "MEDIUM") and (difficulty != "HARD"):
        difficulty = input("What difficulty do you want? (EASY, MEDIUM, HARD)\n").upper()
    if difficulty == "HARD": 
        numGuesses = 5
    elif difficulty == "MEDIUM":
        numGuesses = 10
    elif difficulty == "EASY":
        numGuesses = 15
    return numGuesses

def numberPicker():
    numRange = input("What's the max range number that is positive?\n")
    while not numRange.isnumeric():
        numRange = input("What's the max range number that is positive?\n")
    maxNumber = int(numRange)
    return maxNumber

def guessPicker(maxNumber):
    guess = input(f"Guess a number between 0 and {maxNumber}: ")
    while not guess.isnumeric():
        guess = input(f"Please guess an actual number between 0 and {maxNumber}: ")
    return int(guess)

def picker():
    numGuesses = diffPicker()
    numGuesses = int(numGuesses)

    maxNumber = numberPicker()
    while maxNumber < 1:
        maxNumber = numberPicker()

    number = random.randint(0, maxNumber)
    
    while numGuesses > 0:
        guess = guessPicker(maxNumber)
        while guess < 0 or guess > maxNumber:
            guess = guessPicker(maxNumber)
        if guess == number:
            print(f"Congratulations! You guessed the correct number: {number}!\n")
            break
        else:
            numGuesses -= 1
            print(f"Incorrect. Number of tries left: {numGuesses}\n")
    if numGuesses == 0:
        print(f"The correct number was {number}.\n")
    print("Thanks for playing!")

picker()





