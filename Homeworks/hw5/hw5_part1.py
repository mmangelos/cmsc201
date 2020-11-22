# File:        hw5_part1.py
# Author:      Mitchell Angelos
# Date:        3/11/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program gets a name from the user and
#              then prints their initials.

SPACE_KEYWORD = " "

def main():

    # gets the name from the user
    userName = input("Enter your name: ")
    getInitials(userName)

############################################################
# getInitials() Prints the initials of a given name
# Parameters:   name; a string containing the given name
# Return:       None
def getInitials(name):

    #finds the initials and assigns them to a list
    count = 1
    initialsList = []
    initialsList.append(name[count - 1: count])
    while count < len(name) - 1:
        if name[count : count + 1] == SPACE_KEYWORD:
            initialsList.append(name[count + 1 : count + 2])
        count += 1

    #prints the initials from the list
    count = 0
    print("Your initials are ", end="")
    while count < len(initialsList):
        print(initialsList[count].upper() + ".", end="")
        count += 1
    print("")

main()
