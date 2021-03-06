# File:        hw4_part2.py
# Author:      Mitchell Angelos
# Date:        3/3/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program gathers a list of unique superpowers that the user
#              enters. When the user's done, it prints the number of powers.

SENTINEL_VALUE = "QUIT"

UNDERPOWERED = "You're underpowered!"
PERFECT_HERO = "You're a perfect hero!"
TOO_STRONG = "You're too strong! Wow!"

POWER_THRESHOLD = 3

def main():

    superpowers = []
    powerAmount = 0 #this variable tracks the amount of superpowers.
    tempPower = input("Please enter a superpower ('QUIT' to stop): ")
    #this var above is a helper var that temporarily stores a power.
    while tempPower != SENTINEL_VALUE:
        if tempPower in superpowers:
            print("You've already entered that superpower!")
        elif tempPower not in superpowers:
            superpowers.append(str(tempPower))
            powerAmount += 1
        tempPower = input("Please enter a superpower ('QUIT' to stop): ")

    print("You have " + str(powerAmount) + " superpowers.")
    if powerAmount < POWER_THRESHOLD:
        print(UNDERPOWERED)
    elif powerAmount == POWER_THRESHOLD:
        print(PERFECT_HERO)
    elif powerAmount > POWER_THRESHOLD:
        print(TOO_STRONG)
    

main()
