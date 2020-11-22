# File:        hw3_part6.py
# Author:      Mitchell Angelos
# Date:        2/25/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program prints a counting box.

def main():

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))

    #the following three variables help aid the creation of the counting box.
    tempHeight = 1
    tempWidth = 1
    theNumber = 1
    while tempHeight <= boxHeight:
        tempWidth = 1
        while tempWidth <= boxWidth:
            print(str(theNumber), end=" ")
            tempWidth += 1
            theNumber += 1
        print("")
        tempHeight += 1

main()
