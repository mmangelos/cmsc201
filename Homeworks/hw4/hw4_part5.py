# File:        hw4_part5.py
# Author:      Mitchell Angelos
# Date:        3/5/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program outputs specific responses based on whether a word
#              starts with "pre" or "post" or neither.

LIST_SIZE = 10

START_CHAR = 0
ADD_FOR_PRE = 3
ADD_FOR_POST = 4

PRE_STRING = "pre"
POST_STRING = "post"

def main():

    count = 0
    words = []
    #adds words to list
    while count < LIST_SIZE:
        toAdd = input("Please enter a word: ")
        words.append(toAdd)
        count += 1

    count = 0
    #checks for words and their starts, then prints appropriate message
    while count < LIST_SIZE:
        #checks for pre
        if words[count][START_CHAR : START_CHAR + ADD_FOR_PRE] == PRE_STRING:
            print("You should " + words[count][START_CHAR + ADD_FOR_PRE : len(words[count])] + " early.")
        #checks for post
        elif words[count][START_CHAR : START_CHAR + ADD_FOR_POST] == POST_STRING:
            print("You should " + words[count][START_CHAR + ADD_FOR_POST : len(words[count])]\
                  + " later.")
        else:
            print("You can " + words[count] + " whenever!")
        count += 1


                                 
main()
