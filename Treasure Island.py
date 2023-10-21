print("Welcome to Treasure Island!\n")
print("Find the missing treasure or die trying.\n")

initial = input("You arrive at Treasure Island after some long hours at sea.\n" +
                "In front of you, you see a path leading into a cave and forest.\n" +
                "Where do you want to go? (FOREST, CAVE)\n").upper()
print(initial)
if initial == "FOREST":
    forest1 = input("You decide to travel down the forest path.\n" + 
          "Suddenly, you see a large bear approaching you.\n" +
          "You can either fight it or run. (FIGHT, RUN)\n")
    forest1.upper()
    if forest1 == "FIGHT":
        print("You decide to fight the bear. The bear easily rips through you." +
              "You perish without even finding the treasure.")
    elif forest1 == "RUN":
        print("You decide to run. However, the bear easily catches up to you." + 
              "You become another dinner for the bear.")
    else:
        forest1 = input("You're panicking. What do you do? (FIGHT, RUN)\n").upper()
elif initial == "CAVE":
    print("You walk down to the cave. You walk in and you see the treasure trove!" +
          "You grabbed everything you can and you ran back to the ship a happy man!")
else:
    initial = input("Where do you want to go? (FOREST, CAVE)\n").upper()