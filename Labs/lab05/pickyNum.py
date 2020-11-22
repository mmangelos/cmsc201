# File:        pickyNum.py
# Created by:  Dr. Gibson (k.gibson)
# Author:      Mitchell Angelos
# Date:        2/26/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description:
#   This file contains python code that helps choose
#   a number to statisfy your very picky friend.

def main():

    print("You have a friend who is very picky about their numbers.  They've")
    print("asked you to choose a number that meets certain requirements, but")
    print("you're a lazy computer scientist, so you decided to code a program")
    print("that will check it for you, instead of thinking about it too hard.")
    print("")
    print("The requirements are that the number satisfy the following:")
    print("     positive (greater than zero), less than 1000, ")
    print("     divisible by 4, end in an 8, NOT end in a 2")
    
    isValid = True
    
    while isValid != False:
        num = int(input("Please enter your number: "))
        isValid = False

        # The different conditionals should go here.  Don't forget
        # to tell the user EVERYTHING that was wrong with their
        # number, and to update the value of the Boolean flag!

        if num <= 0:
            print("The number must be greater than 0.")
            isValid = True
        if num >= 1000:
            print("The number must be less than 1000.")
            isValid = True
        if num % 4 != 0:
            print("The number must be divisible by 4.")
            isValid = True
        if num % 10 != 8:
            print("The number must end with an 8.")
            isValid = True    
        if num % 10 == 2:
            print("The number must not end in a 2.")
            isValid = True
            
    print("Congrats!  Your friend accepts the number", num)


main()
