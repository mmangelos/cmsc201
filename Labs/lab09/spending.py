# File:    spending.py
# Started: by Dr. Gibson
# Author:  YOUR NAME GOES HERE
# Date:    DATE GOES HERE
# Section: SECTION NUMBER GOES HERE
# E-mail:  EMAIL_GOES_HERE@umbc.edu
# Description:
#   This file contains python code that tallies a list
#   of expenditures (both by category and in total).


# the category title is the first element of each list
CATEGORY_TITLE = 0

#-------------------------------------------------------------------------
# printSpending() prints the expenditures in all spending categories
# Input:          spendingList, a 2D list holding the expenditures
# Output:         None
#--------------------------------------------------------------------------
def printSpending(spendingList):

    print("\nSpending:")
    print("---------------")
    index = 0

    #loop through each category of expenditures
    while index < len(spendingList):
        # print out the category title with a colon afterwards
        print(spendingList[index][CATEGORY_TITLE], ":", end = "\t")
        #----------------------------------------#
        # write a while loop that prints out the #
        # expenditures (no brackets or commas)   #
        #----------------------------------------#
        col = 1
        numList = spendingList[index]
        while col < len(numList):
            print(str(numList[col]), end="\t")
            col += 1
        
        print()
        index += 1

#------------------------------------------------------------------
# tallySpending() Finds total amount of money spent this month
# Input:          spending;   2D list of expenditures
# Output:         totalSpent; float, the total expenditures
#                (Also prints out total of each category.)
#-----------------------------------------------------------------
def tallySpending(spending):

    totalSpent = 0

    categoryIndex = 0      # used to access each spending category

    # loop through the entire list of expenditures
    while categoryIndex < len(spending):
        # tally the total expenditures for this individual category
        categoryTotal = 0
        purchaseIndex = 1  # used to access each individual purchase
                           # (starts at 1 to skip the category title)
        #----------------------------------------------------#
        # write a while loop that goes through an individual #
        # category's expenditures and totals up the spending #
        #----------------------------------------------------#

        numList = spending[categoryIndex]
        while purchaseIndex < len(numList):
            categoryTotal += float(numList[purchaseIndex])
            purchaseIndex += 1
        
        # print the total expenditures for this category
        print("In category", spending[categoryIndex][CATEGORY_TITLE], \
                  "\t$" + str(categoryTotal), "was spent")
        
        categoryIndex += 1
        # add to running total of all expenditures
        totalSpent    += categoryTotal

    # return the total amount of expenditures
    return totalSpent



def main():
    spending = [['EAT OUT', 15.86, 42.79, 13.8 ,  9.16,  9.16,  5.42, 49.3], \
                    ['VEHICLE',    25.68, 89   ,  7.99, 23.11             ], \
                    ['GROCERIES',  54.33, 30.27,  5.88, 40.71             ], \
                    ['UTILITIES', 165.31, 17.32                           ], \
                    ['PERSONAL',   25   , 14.91, 40.52                    ], \
                    ['ENTERTAIN',  15.66, 13   ,  5.99, 33.04             ], \
                    ['PET CARE',  100   , 13.91, 48.98, 17.22, 42.45      ], \
                    ['RENTING',  1300                                     ]]

    
    # print the current spending list
    printSpending(spending)
    print("\n")
    
    ######################################################
    # write the line of code to call the tallySpending() #
    # function -- pay attention to the input and output  #
    ######################################################

    totalSpent = tallySpending(spending)

    # uncomment this line once tallySpending() has been called
    print("\nYou spent a total of \t$" + str(totalSpent), "this month")
    
main()
