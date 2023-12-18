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


# initial variables
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
conti = True 
forceEnd = False
end = False
gameStatus = "N/A"
name = "N/A"
cash = 1000
profit = 0
bet = 0
dealerScore = 0
dealerPile = []
dealerPile2 = []
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
    "youLost": "You got over 21...you lost this round!\n",
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
    print(f"Player: {name}\nCash: {cash}\n")

def giveCards(p, n) :
    cur = 0
    while cur < n:
        randomCard = random.choice(cards)
        p.append(randomCard)
        cur += 1

def calculateScore(p) :
    cur = 0
    if p == dealerPile or p == playerPile:
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
    
    for i in range(len(p)):
        if p[i] == "A":
            if cur == 10:
                cur += 11
            else:
                cur += 1
        elif p[i] == "J" or p[i] == "Q" or p[i] == "K":
            cur += 10
        elif p[i] == "?":
            cur += 0
        else:
            cur += int(p[i])
    return cur

def printCards(p, b) :
    global playerScore 
    global dealerScore 
    global dealerPile 
    global dealerPile2 
    global playerPile

    if p == playerPile: 
        playerScore = calculateScore(playerPile)
        print("Player's cards:")
        print(*p)
        print(f"Player's score: {playerScore}\n")
    elif p == dealerPile and b == True:
        dealerScore = calculateScore(dealerPile)
        print("Dealer's cards:")
        print(*dealerPile)
        print(f"Dealer's score: {dealerScore}\n")
    elif p == dealerPile:
        temp = ["?"]
        for i in range(1, len(p)):
            temp.append(p[i])
        dealerPile2 = temp
        dealerScore = calculateScore(dealerPile)
        print("Dealer's cards:")
        print(*dealerPile2)
        print(f"Dealer's score: {calculateScore(dealerPile2)}\n")

def betting() :
    global cash
    global bet

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

def giveMoreCards(p) :
    global cash 
    global end 
    global score
    global bet
    
    if p == playerPile:
        passTake = input("Do you want to get a new card or pass? (Y, N)\n").upper()
        while not passTake == "Y" and not passTake == "N":
            passTake = input("Do you want to get a new card or pass? (Y, N)\n").upper()
        if passTake == "Y":
            randomCard = random.choice(cards)
            p.append(randomCard)
            printCards(p, False)
            score = calculateScore(p)
            if score < 21:
                giveMoreCards(p)
            elif score == 21:
                print(f"PCongratulations! You've won ${bet * 2}!\n")
                cash += (bet * 2)
                end = True
            elif score > 21:
                print(dic["youLost"])
                end = True
    elif p == dealerPile:
        score = calculateScore(dealerPile)
        score2 = calculateScore(dealerPile2)
        if (score < 21 and score2 < 21) and (score > playerScore or score2 > playerScore):
                printCards(p, True)
                print(dic["youLost"])
                end = True
        while score < 21:
            randomCard = random.choice(cards)
            p.append(randomCard)
            printCards(p, False)
            score = calculateScore(p)
        if score == 21:
            printCards(p, True)
            print(dic["youLost"])
            end = True
        elif score > 21:
            print(f"DCongratulations! You've won ${bet * 2}!\n")
            cash += (bet * 2)
            end = True
    

def main() :
    global forceEnd
    global end
    global playerPile 
    global dealerPile
    global bet
    global cash

    while not forceEnd and not end:
    # blackjack starting section
        startingCode()

        # betting
        betting()

        # give out cards
        print(dic["dealing"])
        giveCards(playerPile, 2)
        printCards(playerPile, False)
        if playerScore == 21:
            print(f"Congratulations! You've won ${bet * 2}!\n")
            cash += (bet * 2)
            end = True
            break

        giveCards(dealerPile, 2)
        printCards(dealerPile, False)
        if dealerScore == 21:
            print(dic["youLost"])
            print("Dealer's cards:")
            print(*dealerPile)
            print(f"Dealer's score: {dealerScore}\n")
            end = True
            break

        giveMoreCards(playerPile)
        if end:
            break
        giveMoreCards(dealerPile)

    if end:
        restart = input("Do you wish to keep playing? (Y, N)\n").upper()
        while not restart == "Y" and not restart == "N":
            restart = input("Do you wish to keep playing? (Y, N)\n").upper()
        if restart == "Y":
            end = False 
            dealerPile = []
            playerPile = []
            main()
        elif restart == "N":
            print("Thank you for playing!")

    
    elif forceEnd:
        restart = input(dic["newGame"]).upper()
        while restart!= "Y" and restart != "N":
            restart = input(dic["newGame"]).upper()
        if restart == "Y":
            print(dic["restarting"])
            forceEnd = False
            os.system('cls')
            dealerPile = []
            playerPile = []
            main()
        elif restart == "N":
            print("Thank you for playing!")

main()