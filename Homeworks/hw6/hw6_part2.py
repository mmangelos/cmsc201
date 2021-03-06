# File:        hw6_part2.py
# Author:      Mitchell Angelos
# Date:        4/20/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program weaves two strings together
#              and prints the result.

ENTER_STR = "Please enter a string: "
ENTER_STR_ALT = "Enter... SOMETHING ELSE: "

def alternateCharacters(phrase1, phrase2):

    if len(phrase1) == 0:
        return phrase2
    if len(phrase2) == 0:
        return phrase1
    return phrase1[0] + alternateCharacters(phrase2, phrase1[1:])
    
def main():

    strOne = input(ENTER_STR)
    strTwo = input(ENTER_STR_ALT)
    print(alternateCharacters(strOne, strTwo))

main()
