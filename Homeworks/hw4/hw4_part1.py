# File:        hw4_part1.py
# Author:      Mitchell Angelos
# Date:        3/3/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program draws an isosceles right triangle.
#              The user enters a height and two symbols.

MIN_VALUE_TRIANGLE_HEIGHT = 0

def main():

    triangleHeight = int(input("Please enter a height greater than 0: "))
    #loop executes until triangle height enetered is greater than 0
    while triangleHeight <= MIN_VALUE_TRIANGLE_HEIGHT:
        triangleHeight = int(input("Please enter a height greater than 0: "))

    symbolOutline = input("Please enter a symbol for the triangle outline: ")
    symbolFill = input("Please enter a symbol for the triangle fill: ")

    #creates the triangle
    tempLen = triangleHeight
    isOuter = True
    while tempLen > 0:
        tempCount = tempLen
        while tempCount > 0:
            #checks if is outer part so it puts the right symbol
            if isOuter == True:
                print(symbolOutline, end="")
            else:
                #if is end
                if tempCount == tempLen:
                    print(symbolOutline, end="")
                #if is start (so first char of line)
                elif tempCount == 1:
                    print(symbolOutline, end="")
                #filler symbols
                else:
                    print(symbolFill, end="")
            tempCount -= 1
        print("")
        tempLen -= 1
        isOuter = False
        


main()
