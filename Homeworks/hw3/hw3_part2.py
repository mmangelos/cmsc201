# File:        hw3_part2.py
# Author:      Mitchell Angelos
# Date:        2/28/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program calculates the answer to a multiplication
#              question without using multiplication or division.

def main():

    firstNum = int(input("Please enter the first number: "))
    secondNum = int(input("Please enter the second number: "))

    tempNumber = 0 #this number helps aid the while loop.
    output = 0 #this is the variable that calculation is stored in

    while tempNumber < firstNum:
        output += secondNum
        tempNumber += 1

    print(str(firstNum) + " * " + str(secondNum) + " = " + str(output))

main()
