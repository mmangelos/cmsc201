# File:        dessert.py
# Author:      Mitchell Angelos
# Date:        2/12/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: tbf
#

def main():

    favoriteDessert = input("What is you favorite dessert? ")

    if favoriteDessert == "pie":
        pieFlavor = input("What's your favorite pie flavor? ")
        if pieFlavor == "apple" or pieFlavor == "sweet potato":
            print("That is the correct answer!")
        else:
            print(pieFlavor, "is a really interesting flavor...")
    elif favoriteDessert == "ice cream":
        scoopAmount = int(input("How many scoops do you usually get? "))
        if scoopAmount <= 0:
            print("Add a few more scoops!")
        elif scoopAmount == 1 or scoopAmount == 2:
            print("That's a normal amount of ice cream.")
        elif scoopAmount >= 3:
            print("That's quite a lot of ice cream!")
    else:
        print("Sounds yummy!")


main()
