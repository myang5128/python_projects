import random

print("Welcome to Rock Paper Scissor!\n")
end = False
while not end:
    print("What do you choose?\n")
    enemyChoice = random.randint(0,2)
    player_Choice = int(input("0 for ROCK, 1 for PAPER, 2 for SCISSOR\n"))
    while (player_Choice != 0) and (player_Choice != 1) and (player_Choice != 2):
        player_Choice = input("0 for ROCK, 1 for PAPER, 2 for SCISSOR\n")
    # 0 = 0, 0 < 1, 0 > 2
    # 1 > 1, 1 = 1, 1 < 2
    # 2 < 0, 2 > 1, 2 = 2
    if player_Choice == 0:
        if enemyChoice == 0:
            print("You picked ROCK and the bot picked ROCK, it's a tie!\n")
        elif enemyChoice == 1:
            print("You picked ROCK and the bot picked PAPER, you lose!\n")
        elif enemyChoice == 2:
            print("You picked ROCK and the bot picked SCISSOR, you win!\n")
    elif player_Choice == 1:
        if enemyChoice == 0:
            print("You picked PAPER and the bot picked ROCK, you win!\n")
        elif enemyChoice == 1:
            print("You picked PAPER and the bot picked PAPER, it's a tie!\n")
        elif enemyChoice == 2:
            print("You picked PAPER and the bot picked SCISSOR, you lose!\n")
    else:
        if enemyChoice == 0:
            print("You picked SCISSOR and the bot picked ROCK, you lose!\n")
        elif enemyChoice == 1:
            print("You picked SCISSOR and the bot picked PAPER, you win!\n")
        elif enemyChoice == 2:
            print("You picked SCISSOR and the bot picked SCISSOR, it's a tie!\n")
    print("Do you want to play again?")
    keepPlaying = input("Y for YES, N for NO\n").upper()
    if keepPlaying == "N":
        end = True
print("Thanks for playing!")