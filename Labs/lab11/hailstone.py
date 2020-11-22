# File:    hailstone.py
# Started: by Dr. Gibson
# Author:  Mitchell Angelos
# Date:    4/12/19
# Section: 12
# E-mail:  a242@umbc.edu
# Description:
#   This file contains python code that implements the
#   "flight" of a hailstone, following the HOTPO rules
#   (also known as the Collatz Conjecture), recursively

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
# flight() recursively calculates the path of a hailstone
# Input:   the height of the hailstone
#          the current step
# Output:  a recursive call, which at the end returns 
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height, step):

    print("Height of:", str(height))
    
    if height <= 0:
        print("Invalid height of", str(height))
        return 0
    if height == 1:
        return step
    if height % 2 == 0:
        return flight(int(height / 2), step + 1)
    elif height % 2 != 0:
        return flight(int((height * 3) + 1), step + 1)

    return step

    #return steps
    
    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0

    # stops when it reachs height of 1 (the ground)

    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2

    # if the current height is odd, multiply it by 3, then add 1


def main():

    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))

    # recursive call goes here
    steps = flight(startHeight, 0)

    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")

main()

    

