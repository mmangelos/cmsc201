# File:        hw5_part4.py
# Author:      Mitchell Angelos
# Date:        3/11/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program translates English to Pig Latin.

SPACE_KEYWORD = " "
PIG_LATIN_START_COUNT = 1
VOWELS = ["A", "E", "I", "O", "U", "Y"]

def main():

    #gets phrase from user
    englishPhrase = input("Please enter an English phrase: ")
    #puts each individual word in a list
    indivWordList = []
    count = 0
    startPos = 0
    nextSpaceIndex = 0
    while count < len(englishPhrase):
        if englishPhrase[count] == SPACE_KEYWORD:
            nextSpaceIndex = count
            indivWordList.append(englishPhrase[startPos : nextSpaceIndex])
            startPos = nextSpaceIndex + 1
        elif count + 1 == len(englishPhrase):
            nextSpaceIndex = len(englishPhrase)
            indivWordList.append(englishPhrase[startPos : nextSpaceIndex])
        count += 1

    #gets translations of all english words into pig latin, put into new list
    pigLatinList = []
    count = 0
    while count < len(indivWordList):
        pigLatinList.append(translate(indivWordList[count]))
        count += 1

    #prints pig latin translation
    count = 0
    print("I think you meant to say: ", end="")
    while count < len(pigLatinList):
        print(pigLatinList[count], end=" ")
        count += 1

################################################################
# translate() takes a single english word, translates it to pig latin
# Parameters: english_word; an English word
# Return:     The pig latin translation
def translate(english_word):

    #if first letter of word contains a vowel
    if english_word[0].upper() in VOWELS:
        return english_word + "ay"
    #if first letter of word does not contain a vowel
    elif english_word[0].upper() not in VOWELS:
        return english_word[1:len(english_word)] + english_word[0] + "ay"

main()
