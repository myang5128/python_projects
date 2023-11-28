import random
import os
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run


# initial variables
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
conti = True 
forceEnd = False
gameStatus = "N/A"
name = "N/A"
cash = 1000
win = 0
loss = 0
draws = 0
profit = 0
bet = 0
winstreak = 0
dealerScore = 0
dealerPile = []
playerScore = 0
playerPile = []
turn = True
dic = {
    "draw": "Dang, you guys had a draw. Let's play again.\n",
    "start": "Welcome to Blackjack!\n",
    "rules": "Would you like to hear the rules for Blackjack? (Y, N) ",
    "rules2": "Please enter Y or N to hear the rules for Blackjack. (Y, N) ",
    "rulesGo": "INSERT RULES\n",
    "name": "What is your name? ",
    "bet": "How much do you want to bet? ",
    "bet2": "Please enter a valid amount of money you want to bet. ",
    "bet3": "You don't have enough money. Bet a different amount. ",
    "noCash": "You lost all your money. You've got kicked out of the casino!\n",
    "dealing": "The dealer now deals out the cards. Good luck!\n",
    "newGame": "Do you want to start a new game? (Y, N)\n",
    "restarting": "Restarting...\n"
}

def startingCode() :
    print(dic["start"])
    getRules = input(dic["rules"]).upper()
    while getRules != "Y" and getRules != "N":
        getRules = input(dic["rules2"]).upper()
    if getRules == "Y":
        print(dic["rulesGo"])
    name = input(dic["name"]).upper()
    print(f"Player: {name}\nCash: {cash}\nWin/Lose/Draw: {win}/{loss}/{draws}\nCurrent Win Streak: {winstreak}\n")

def giveCards(p, n) :
    cur = 0
    while cur < n:
        randomCard = random.choice(cards)
        p.append(randomCard)
        cur += 1

def calculateScore(p) :
    cur = 0
    for i in range(len(p)):
        if p[i] == "A":
            if cur == 10:
                cur += 11
            else:
                cur += 1
        elif p[i] == "J" or p[i] == "Q" or p[i] == "K":
            cur += 10
        else:
            cur += int(p[i])
    return cur

def printCards(p) :
    if p == playerPile: 
        playerScore = calculateScore(playerPile)
        print("Player's cards:")
        print(*p)
        print(f"Player's score: {playerScore}\n")
    elif p == dealerPile:
        dealerScore = calculateScore(dealerPile)
        print("Dealer's cards:")
        print(*p)
        print(f"Dealer's score: {dealerScore}\n")

def betting() :
    global cash
    if cash <= 0:
        print(dic["noCash"])
        forceEnd = True
    bet = input(dic["bet"])
    while not bet.isnumeric() :
        bet = input(dic["bet2"])
    while int(bet) > cash :
        bet = input(dic["bet3"])
    bet = int(bet)
    cash -= bet 
    print(f"You bet ${bet} and your new cash total is ${cash}!\n")

def checkWin() :
    global dealerScore 
    global playerScore
    

def main() :
    while not forceEnd and conti:
    # blackjack starting section
        startingCode()

        # betting
        betting()

        # give out cards
        print(dic["dealing"])
        giveCards(playerPile, 2)
        printCards(playerPile)
        giveCards(dealerPile, 2)
        printCards(dealerPile)

    if forceEnd:
        restart = input(dic["newGame"]).upper()
        while getRules != "Y" and getRules != "N":
            getRules = input(dic["newGame"]).upper()
        if getRules == "Y":
            print(dic["restarting"])
            os.system('cls')
            main()

main()