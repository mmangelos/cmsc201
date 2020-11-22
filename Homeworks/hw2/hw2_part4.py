# File:        hw2_part4.py
# Author:      Mitchell Angelos
# Date:        2/17/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program is a small game where it asks about the player's
#              dog and attempts to guess the breed. Only 5 breeds can be
#              chosen though.

def main():

    print("The following questions only accept 'yes' or 'no' as answers.")
    isFluffy = input("Is your dog fluffy? ")
    if isFluffy == "yes":
        isSmall = input("Is it a small dog? ")
        if isSmall == "yes":
            print("Your dog is a Japanese Spitz!")
        elif isSmall == "no":
            needsHaircut = input("Ok, does it need a specific haircut to do its job? ")
            if needsHaircut == "yes":
                print("You have a Standard Poodle!")
            elif needsHaircut == "no":
                print("You have a Kuvasz!")
    elif isFluffy == "no":
        isAmericanBreed = input("Is your dog an American breed? ")
        if isAmericanBreed == "yes":
            print("You have a Chesapeake Bay Retriever!")
        elif isAmericanBreed == "no":
            print("You have a Vizsla!")


main()
