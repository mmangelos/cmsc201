# File:        names.py
# Started:     by Brianna Richardson (& Dr. Gibson)
# Author:      Mitchell Angelos
# Date:        3/12/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This file contains python code that uses functions to allow 
#              a user to get information about a list of names entered.

SENTINEL = "-1"

###################################################################
# printList() prints out a list, showing the index of each element
# Input:      theList; a list of any types of variables
# Output:     None
def printList(theList):
    #---------------------------------------------------------#
    # your function to print the list (indexes too) goes here #
    #---------------------------------------------------------#
    i = 0
    while i < len(theList):
        print("At index " + str(i) + " the name is " + theList[i] + ".")
        i += 1
    
######################################################################
# printMinStr() prints the string with the minimum length from a list
# Input:        theList; a list of strings
# Output:       None
def printMinStr(theList):
    #---------------------------------------------------------------#
    # your function to find and print the shortest string goes here #
    #---------------------------------------------------------------#
    i = 0
    minim = theList[0]
    while i < len(theList):
        if len(theList[i]) < len(minim):
            minim = theList[i]
        i += 1
    print("The shortest string in the list is " + minim + ".")

######################################################################
# printMaxStr() prints the string with the maximum length from a list
# Input:        theList; a list of strings
# Output:       None
def printMaxStr(theList):
    #--------------------------------------------------------------#
    # your function to find and print the longest string goes here #
    #--------------------------------------------------------------#
    i = 0
    maxim = theList[0]
    while i < len(theList):
        if len(theList[i]) > len(maxim):
            maxim = theList[i]
        i += 1
    print("The longest string in the list is " + maxim + ".")

def main():
    nameList = []

    msg = "Enter a name (or " + SENTINEL + " to quit): "

    name = input(msg)

    # ask the user for names until they choose to exit
    while(name != SENTINEL):
        # check beforehand, so we only save valid names
        nameList.append(name)
        name = input(msg)

    # call the print function
    #------------------------------------------------------#
    # your code to call the function printList() goes here #
    #------------------------------------------------------#
    printList(nameList)
    # print out the minimum and maximum length names
    #-------------------------------------------#
    #  your code to call the two functions for  #
    # printMinStr() and printMaxStr() goes here #
    #-------------------------------------------#
    printMinStr(nameList)
    printMaxStr(nameList)
    
main()
