# File:        hw2_part3.py
# Author:      Mitchell Angelos
# Date:        2/17/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: A simple calculator with a subtraction and modulus
#              function, always yielding a positive number.

def main():

    firstInt = int(input("Please enter the first integer: "))
    secondInt = int(input("Please enter the second integer: "))

    print("The options are minus or mod.")
    operationPerformed = input("Enter the operation you want to perform: ")

    if operationPerformed != "minus" and operationPerformed != "mod":
        print("Invalid operation.")
    elif operationPerformed == "minus":
        if firstInt > secondInt:
            print(str(firstInt) + " - " + str(secondInt) + " = " \
                  + str(firstInt - secondInt))
        elif firstInt < secondInt:
            print(str(secondInt) + " - " + str(firstInt) + " = " \
                  + str(secondInt - firstInt))
    elif operationPerformed == "mod":
        if firstInt > secondInt:
            print(str(firstInt) + " % " + str(secondInt) + " = " \
                  + str(firstInt % secondInt))
        elif firstInt < secondInt:
            print(str(secondInt) + " % " + str(firstInt) + " = " \
                  + str(secondInt % firstInt))
    

main()
