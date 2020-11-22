# File:        hw1_part1.py
# Author:      Mitchell Angelos
# Date:        2/9/19
# Section:     Section 12
# E-mail:      a242@umbc.edu
# Description: This program prints out the amount of
#              monitors, mice and empty bottles on the
#              user's desk. Then prints the total amount
#              of items the user has on the desk.

def main():

    numMonitors = 2
    numMice = 1
    numEmptyBottles = 4
    numTotalItems = numMonitors + numMice + numEmptyBottles
    
    print("You have", numMonitors, "monitors on your desk.")
    print("You have", numMice, "mice on your desk.")
    print("You have", numEmptyBottles, "empty bottles on your desk.")
    print("You have", numTotalItems, "items on your desk.")


main()
