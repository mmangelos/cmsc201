# File:        hw6_part3.py
# Author:      Mitchell Angelos
# Date:        4/20/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program performs the mod function, but recursively.

NUM_ONE = "Enter a number: "
NUM_TWO = "Enter another number: "

############################################################
# recursiveMod() recursively calculates the remainder of
#         dividing two numbers
# Paramters:    numer; the numerator
#               denom; the denominator
# Output:       the integer representation of the remainder
def recursiveMod(numer, denom):

    if numer < denom:
        return numer
    return recursiveMod(numer - denom, denom)

def main():

    one = int(input(NUM_ONE))
    two = int(input(NUM_TWO))
    print(str(one) + " % " + str(two) + " = " + \
          str(recursiveMod(one, two)))

main()
