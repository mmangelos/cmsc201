# File:        hw5_part5.py
# Author:      Mitchell Angelos
# Date:        3/11/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program gets words from a user and then prints them in
#              reverse order, as well as the words being backwards.

def main():

    # gets the amount of words the user wants
    wordCount = int(input("Plese enter how many words you want backwards: "))
    wordList = []
    count = 1
    while len(wordList) != wordCount:
        toAdd = input("Please enter string #" + str(count) + ": ")
        wordList.append(toAdd)
        count += 1

    #prints all words backwards
    count = len(wordList) - 1
    while count >= 0:
        print("The string '" + wordList[count] + "' reversed is '" + \
              backwards(wordList[count]) + "'.")
        count -= 1

#########################################################
# backwards() gets a string and returns it backwards
# Parameters: forString; a string to reserve
# Return:     backString; the reserved string
def backwards(forString):

    #takes given string and reverses it
    count = len(forString) - 1
    backString = ""
    while count >= 0:
        backString += forString[count]
        count -= 1
    return backString
    
main()
