# File:        hw3_part4.py
# Author:      Mitchell Angelos
# Date:        2/25/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program allows us to become pokemon trainers and input BR
#              for all the pokemon we have caught.

def main():

    pokemonCaught = int(input("Please enter how many pokemon you've caught: "))
    while pokemonCaught < 1:
        pokemonCaught = int(input("Don't be silly. Enter how many pokemon you've caught: "))

    totalBR = 0 #this is used to add up all the BR for calculating average
    pokemonNumber = 1 #this variable tracks the pokemon number you're on
    while pokemonNumber <= pokemonCaught:
        print("Pokemon #" + str(pokemonNumber) + ":")
        totalBR += int(input("Input the BR of this pokemon: "))
        pokemonNumber += 1

    print("The " + str(pokemonCaught) + " pokemon you caught had an average BR of " + str(totalBR / pokemonCaught) + ".")

main()
