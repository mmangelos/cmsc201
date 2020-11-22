# File:        hw3_part1.py
# Author:      Mitchell Angelos
# Date:        2/25/19
# Section:     12 
# E-mail:      a242@umbc.edu
# Description: This program simulates the up or down movement of a
#              hailstone in a storm.

def main():

    #"hailstoneHeight" is the user's entered value for the starting height of
    # their stone.
    hailstoneHeight = int(input("Please enter a starting height for the hailstone: "))

    while hailstoneHeight > 1:
        print("Hailstone is currently at height " + str(int(hailstoneHeight)))
        if hailstoneHeight % 2 == 0:
            hailstoneHeight /= 2 #if height is even, it will be cut in half.
        else:
            hailstoneHeight = (hailstoneHeight * 3) + 1 #if height is odd,
            #it will be tripled and have 1 added to it.

    print("Hailstone stopped at height " + str(int(hailstoneHeight)))

main()
