# File:        hw5_part2.py
# Author:      Mitchell Angelos
# Date:        3/11/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program counts how many words in a sentence look
#              like they're past tense.

PAST_TENSE_KEYWORD = "ed"

def main():

    # gets string from user
    userEntry = input("Tell me something: ")
    countPastTense(userEntry)
    
########################################################
# countPastTense() counts past tense words
# ParameterS:      phrase; a string to count past tense words from
# Return:          none
def countPastTense(phrase):

    #counts how many past tense words there are, then prints amount
    pastTenseCount = 0
    count = 0
    while count < len(phrase):
        if phrase[count : count + 2] == PAST_TENSE_KEYWORD:
            pastTenseCount += 1
        count += 1
    #prints the result
    print("There appear to be " + str(pastTenseCount) + " past tense words.")
    
main()
