# File:        hw4_part4.py
# Author:      Mitchell Angelos
# Date:        3/5/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program lets the user create a grocery list, then giving
#              them a breakdown on what to buy including amount.

SENTINEL_VALUE = "END"

def main():

    groceryList = []
    amountToBuy = [] 
    listAdd = input("Please enter an item, or '" + SENTINEL_VALUE + \
                    "' to stop: ")
    listAmount = ""
    #adds items to grocery list with respective amount
    while listAdd != SENTINEL_VALUE:
        listAmount = input("Please enter the amount to buy: ")
        groceryList.append(listAdd)
        amountToBuy.append(listAmount)
        listAdd = input("Please enter an item, or '" + SENTINEL_VALUE + \
                        "' to stop: ")

    count = 0
    totalItems = 0
    #prints items and amounts
    while count < len(groceryList):
        print("Purchase " + str(amountToBuy[count]) + " of "\
              + groceryList[count])
        totalItems += int(amountToBuy[count])
        count += 1
    print("Total of " + str(totalItems) + " items to be purchased")

main()
