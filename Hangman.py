import random

# current word list
word_list = ["aardvark", "baboon", "camel", "horse", "cat", "elephant", "giraffe"]

# player variables
player_lives = 7
game_Cond = True

# picks random word and makes the list
correct_Word =random.choice(word_list)
alp_list = ["_"] * len(correct_Word)

while game_Cond:
    print(f"Current lives: {player_lives}")
    print(alp_list)

    letter_Cond = False

    letter_Guess = input("Choose a letter.\n").lower()
    while alp_list.count(letter_Guess) >0:
        letter_Guess = input(f"Choose a different letter, {letter_Guess} is already used.\n").lower()
    for n in range(0, len(alp_list)):
        if letter_Guess == correct_Word[n]:
           alp_list[n] = letter_Guess
           letter_Cond = True
    if alp_list.count("_") == 0:
        game_Cond = False
    if not letter_Cond:
        player_lives -= 1
        if player_lives == 0:
            game_Cond = False

if not game_Cond:
    if player_lives > 0:
        print(correct_Word)
        print("You win!")
    else:
        print("You lose...")