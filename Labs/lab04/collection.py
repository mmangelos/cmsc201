# File:        collection.py
# Author:      Mitchell Angelos
# Date:        2/19/19
# Section:     12 
# E-mail:      a242@umbc.edu
# Description: tbf

def main():

    userNumber = float(input("Enter how many beanie babies you have: "))
    while userNumber <= 0:
        print("Please enter a number greater than 0.")
        userNumber = float(input("Enter how many beanie babies you have: "))

    i = 0
    minVal = 0
    maxVal = 0
    while i < userNumber:
        bbValue = float(input("Enter a beanie baby value: "))
        if i == 0:
            minVal = bbValue
            maxVal = bbValue
        if bbValue < minVal:
            minVal = bbValue
        elif bbValue > maxVal:
            maxVal = bbValue
        i += 1

    print("The min value was " + str(minVal) + ".")
    print("The max value was " + str(maxVal) + ".")

    
main()
