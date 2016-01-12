import random


Attributes = {
    0: "Kracht",
    1: "Intelligentie",
    2: "Behendigheid"
}


def printCards(total, levels, statRange, costFactor, noiseFactor, type):
    if type == "character":
        with open("Karakterkaarten.txt", "w") as charCards:
            level = 0
            attribute = 0
            for card in range(total):
                if card % (total//levels) == 0:
                    level += 1
                if card % (total//levels//len(Attributes)) == 0:
                    attribute += 1
                    attribute %= len(Attributes)
                print("Karakterkaart", file=charCards)
                print("Level:\t\t", level, file=charCards)

                print(level)
                botLimit = statRange[0]+(level-1)*(statRange[1]//levels)
                topLimit = statRange[1]-(levels-level)*(statRange[1]//levels)
                att = random.randint(botLimit, topLimit)
                print(Attributes[attribute], ":\t", att, file=charCards)

                payment = 1000*round((att*costFactor+noiseFactor*random.uniform(-1, 1))/1000, 1)
                if payment < 100: payment = 100
                print("Loon:\t\t", payment,"\n", file=charCards)

    if type == "vault":
        with open("Kraakkaarten.txt", "w") as vaultCards:
            level = 0
            for card in range(total):
                if card % (total//levels) == 0:
                    level += 1
                print("Kraakkaart", file=vaultCards)
                print("Level:\t\t", level, file=vaultCards)
                attributes = random.sample(range(len(Attributes)), random.randint(1,len(Attributes)))

                totalCost = 0
                if attributes.count(0) > 0:
                    botLimit = statRange[0]+(level-1)*(statRange[1]//levels)
                    topLimit = statRange[1]-(levels-level)*(statRange[1]//levels)
                    rand = random.randint(botLimit, topLimit)
                    print(Attributes[0], ":\t", rand, file=vaultCards)
                    totalCost += rand
                if attributes.count(1) > 0:
                    botLimit = statRange[0]+(level-1)*(statRange[1]//levels)
                    topLimit = statRange[1]-(levels-level)*(statRange[1]//levels)
                    rand = random.randint(botLimit, topLimit)
                    print(Attributes[1], ":\t", rand, file=vaultCards)
                    totalCost += rand
                if attributes.count(2) > 0:
                    botLimit = statRange[0]+(level-1)*(statRange[1]//levels)
                    topLimit = statRange[1]-(levels-level)*(statRange[1]//levels)
                    rand = random.randint(botLimit, topLimit)
                    print(Attributes[2], ":\t", rand, file=vaultCards)
                    totalCost += rand

                buit = 1000*round((totalCost*costFactor+noiseFactor*random.uniform(-1, 1))/1000, 1)
                if buit < 100: buit = 100
                print("Buit:\t\t", buit, "\n", file=vaultCards)



if __name__ == "__main__":
    print("-------------------------------------------------------------------------------\n"
          "Hi There!\n"
          "Welcome to the \"Print Gamecards for Burglar in the Dark Forrest Application\".\n"
          "Let's print some cards!\n"
          "-------------------------------------------------------------------------------\n\n")

    while True:
        try:
            type = input("What type of cards do you want, character or vault?\n")
            if type != "character" and type != "vault":
                print("\n!!! You seem to have misspelled something. Please type either \"character\" or \"vault\" !!!\n")
            else: break
        except ValueError:
            print("\n!!! Woops! Something went wrong. Please type either \"character\" or \"vault\" !!!\n")

    while True:
        try:
            characterCards = int(input("How many cards do you want?\n"))
            break
        except (ValueError, TypeError):
            print("\n!!! Woops! Something went wrong. Please type in an integer !!!\n")

    while True:
        try:
            levels = int(input("How many levels do you want the cards to have?\n"))
            break
        except (ValueError, TypeError):
            print("\n!!! Woops! Something went wrong. Please type in an integer !!!\n")

    while True:
        try:
            statRange = [int(x) for x in input("What is the range of the values you want their attributes to lie in? "
                      "(enter two space separated numbers)\n").split()]
            if len(statRange) is not 2:
                print("\n!!! Not the correct number of values. Please type in two integers separated by a space !!!\n")
            else: break
        except (ValueError, TypeError):
            print("\n!!! Woops! Something went wrong. Please type in two integers separated by a space !!!\n")

    while True:
        try:
            costFactor = int(input("What cost/reward factor do you want?\n"))
            break
        except (ValueError, TypeError):
            print("\n!!! Woops! Something went wrong. Please type in an integer !!!\n")

    while True:
        try:
            noiseFactor = int(input("What noise factor do you want for the costs/rewards?\n"))
            break
        except (ValueError, TypeError):
            print("\n!!! Woops! Something went wrong. Please type in an integer !!!\n")

    printCards(characterCards, levels, statRange, costFactor, noiseFactor, type)

    print("There you go :)")