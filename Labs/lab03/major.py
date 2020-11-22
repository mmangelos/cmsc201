# File:        major.py
# Author:      Mitchell Angelos
# Date:        2/12/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: Asks user for their major and returns if they need a
#              B or C to have CMSC 201 count.

def main():

    major = input("Please enter your major: ")

    if major == "CMSC" or major == "CMPE":
        print("You need at least a B for CMSC 201 to count.")
    else:
        print("You need at least a C for CMSC 201 to count.")

main()
