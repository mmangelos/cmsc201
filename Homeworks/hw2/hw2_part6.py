# File:        hw2_part6.py
# Author:      Mitchell Angelos
# Date:        2/18/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program asks the user for the state of two switches.
#              With this knowledge, the program will decide the state of
#              a generator.

def main():

    print("We accept 'y' for yes and 'n' for no. The only accepted answers.")
    switchOneState = input("Is the first switch on? (y/n) ")
    switchTwoState = input("Is the second switch on? (y/n) ")

    if switchOneState != switchTwoState:
        print("The generator is on.")
    else:
        print("The generator is off")

main()
