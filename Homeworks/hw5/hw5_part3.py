# File:        hw5_part3.py
# Author:      Mitchell Angelos
# Date:        3/11/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program searches a phrase for a certain word, and prints
#              the index(es) at which the word is found.

def main():

    #gets string from user
    phrase = input("Please enter a phrase: ")
    #gets word to search for, ensuring it's length is less than the var phrase
    searchWord = input("Please enter a word to search for: ")
    while len(searchWord) >= len(phrase):
        print("The word cannot be longer than the phrase.")
        searchWord = input("Please enter a shorter word to search for: ")
    inPhrase(phrase, searchWord)

################################################################
# inPhrase()  Finds a keyword in a phrase, then prints the index(es) of the
#             start of where the keyword is found.
# Parameters: phrase; the phrase given by the user.
#             word; the keyword to be found in the phrase.
# Return:     None
def inPhrase(phrase, word):

    #this var, addFor, helps me check for the keyword later in the function
    addFor = len(word)
    #finds the index(es) where the word is found, puts them in a list
    count = 0
    indexList = []
    while count < len(phrase):
        if phrase[count : count + addFor].lower() == word.lower():
            indexList.append(count)
        count += 1

    #prints the index(es)
    count = 0
    while count < len(indexList):
        print("Found " + word + " at index " + str(indexList[count]))
        count += 1
    print("Found " + word + " a total of " + str(len(indexList)) + " times.")

main()
