# File:        proj1.py
# Author:      Mitchell Angelos
# Date:        4/2/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program puts all of our learning into use to create a
#              Hawaiian word pronunciation program.


# info for getting choice
ANSWERS = ["y", "yes", "n", "no"]
CONTINUE = "Do you want to enter another word? (y/yes/n/no): "

# info about characters
OKINA = "'"
VOWELS = ["a", "e", "i", "o", "u"]
VOWEL_SOUNDS = ["ah", "eh", "ee", "oh", "oo"]
COMP_VOWELS = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
COMP_SOUNDS = ["eye", "eye", "ow", "ow", "ay", "eh-oo", "ew", "oy", "ow",\
               "ooey"]
CONSONANTS = ["h", "k", "l", "m", "n", "p", "w"]

# prominent keywords
W_KEYWORD = "w"
V_KEYWORD = "v"
HYPHEN = "-"
SPACE_KEYWORD = " "

# prominent numbers
WORD_START_INDEX = 0

#############################################
# getChoice() prompts and repromts the user until
#             they select a valid word choice
# Parameters: question; a string to be asked
#             options; a list of string options
# Return:     choice; a string chosen by the user
def getChoice(question, options):
    choice = ""
    
    #ensures case insensitive
    i = 0
    while i < len(options):
        options[i] = options[i].lower()
        i += 1

    while choice not in options:
        choice = input(question)
        choice = choice.lower()

    return choice

###################################################################
# getHawaiianPhrase() prompts the user for a Hawaiian phrase
#                     until a valid one is allowed
# Parameters:         none
# Return:             phrase; a string of the user's chosen phrase
def getHawaiianPhrase():
    phrase = ""
    
    isValid = False
    while isValid == False:
        isValid = True
        phrase = input("Please enter a Hawaiian phrase: ")
        #ensures case insensitivity
        phrase = phrase.lower()
        #gathers a list of individual words
        words = getListOfWords(phrase)

        #checks if any word does not end in a vowel
        i = 0
        while i < len(words):    
            if endsInVowel(words[i]) == False:
                print("The word " + words[i].upper() + \
                      " does not end in a vowel.")
                isValid = False
            i += 1

        #checks if any single character is invalid
        i = 0
        while i < len(phrase):
            if phrase[i] not in VOWELS and phrase[i] not in CONSONANTS \
               and phrase[i] != OKINA and phrase[i] != SPACE_KEYWORD:
                print("The letter " + phrase[i].upper() + " is not valid.")
                isValid = False
            i += 1
            
    return phrase

###################################################################
# pronounceW() determines how a "w" should be pronounced
# Parameters:  word; a string of the word where 'w' is in
#              index; an integer index where 'w' is in the word
# Return:      pronunciation; a single character string with the
#              correct pronunciation
def pronounceW(word, index):
    pronunciation = ""

    #if the w is first letter in word, or before o or u
    if index == WORD_START_INDEX or word[index - 1] == VOWELS[3] or \
       word[index - 1] == VOWELS[4]:
        pronunciation = W_KEYWORD
    #if the w before is a, e or i
    elif word[index - 1] == VOWELS[0] or word[index - 1] == VOWELS[1] or \
         word[index - 1] == VOWELS[2]:
        pronunciation = V_KEYWORD

    return pronunciation

####################################################################
# simpleVowel() determines how a vowel should be pronounced
# Parameters:   letter; a single character string vowel
# Return:       pronunciation; a string representing how the vowel
#               is pronounced
def simpleVowel(letter):
    pronunciation = ""

    #finds index of vowel in list
    i = 0
    while i < len(VOWELS):
        if letter == VOWELS[i]:
            pronunciation = VOWEL_SOUNDS[i]
        i += 1

    #returns the pronunciation and a hyphen stuck onto the end of it
    return pronunciation + HYPHEN

###################################################################
# complexVowel() determines how a complex two letter vowel sounds
# Parameters:    vowels; a two character string vowel
# Return:        pronunciation; a string with how the complex vowel
#                is pronounced
def complexVowel(vowels):
    pronunciation = ""

    i = 0
    while i < len(COMP_VOWELS):
        if vowels == COMP_VOWELS[i]:
            pronunciation = COMP_SOUNDS[i]
        i += 1

    #returns the complex vowel pronunciation with a hyphen on the end of it
    return pronunciation + HYPHEN

###################################################################
# pronunce()  determines how to pronounce an entire phrase
# Parameters: phrase; a string, possibly multiple words
# Return:     pronunciation; a string with the complete phrase's
#             pronunciation
def pronounce(phrase):
    pronunciation = ""
    words = getListOfWords(phrase)

    i = 0
    while i < len(words):
        pronunciation = pronunciation + pronounceWord(words[i])
        i += 1
    
    return pronunciation

####################################################################
# pronounceWord() determines how to pronounce a single word
# Parameters:     word; a string, no spaces in it, of the word
# Return:         pronunciation; a string containing the word's
#                 pronunciation
def pronounceWord(word):
    pronunciation = ""
    tempWord = word.lower()
    
    i = 0
    while i < len(tempWord):
        #if letter is consonant or okina, add appropriate char
        if tempWord[i] in CONSONANTS or tempWord[i] == OKINA:
            #if letter is "w", get appropriate pronunciation
            if tempWord[i] == W_KEYWORD:
                pronunciation = pronunciation + pronounceW(tempWord, i)
            #adds consonant or okina to the pronunciation
            else:
                pronunciation = pronunciation + tempWord[i]
            i += 1
        #if letter is vowel...
        elif tempWord[i] in VOWELS:
            #...and is end of the word, or next letter is not vowel
            if (i+1) >= len(tempWord) or tempWord[i+1] not in VOWELS:
                pronunciation = pronunciation + simpleVowel(tempWord[i])
                i += 1
            #...and next letter is vowel, but the two != complex vowel
            elif tempWord[i + 1] in VOWELS and tempWord[i: i+2] \
                 not in COMP_VOWELS:
                pronunciation = pronunciation + simpleVowel(tempWord[i])
                i += 1
            #...and next letter is vowel, but the two == complex vowel
            elif tempWord[i + 1] in VOWELS and tempWord[i: i+2] \
                 in COMP_VOWELS:
                pronunciation = pronunciation + complexVowel(tempWord[i: i+2])
                i += 2

    #removes the hyphen off the end of the word
    pronunciation = removeLastHyphen(pronunciation)
    #returns the pronunciation with a space for the next word
    return pronunciation + SPACE_KEYWORD

####################################################################
# endsInVowel() checks if the word given by the user ends in a vowel
#               or not
# Parameters:   word; the string being checked
# Return:       isValid; a boolean variable showing if the word does
#               doesn't contain a vowel
def endsInVowel(word):
    isValid = False
    #checks if last letter is a vowel
    if word[len(word) - 1] in VOWELS:
        isValid = True
    return isValid

#######################################################################
# removeLastHyphen() removes the last hyphen in a string if there's one
# Parameters:        phrase; the phrase to remove the last hyphen from
# Return:            editedPhrase; the phrase without the end hyphen
def removeLastHyphen(phrase):
    editedPhrase = phrase
    #checks if the last character is a hyphen
    if editedPhrase[len(editedPhrase) - 1] == HYPHEN:
        editedPhrase = editedPhrase[0: (len(editedPhrase) - 1)]
    return editedPhrase

############################################################################
# getListOfWords() finds all different words in the phrase and seperates
#                  them into a list
# Parameters:      phrase; the entire phrase to find all the words in
# Return:          words; a list of all the seperated words
def getListOfWords(phrase):
    words = []

    i = 0
    startIndex = i
    while i < len(phrase):
        #if next character is a space, or if that's the end of the word...
        if phrase[i] == SPACE_KEYWORD or (i + 1) == len(phrase):
            #checks if next char is end of word
            if (i+1) == len(phrase):
                #adds one to the index so the following append works
                i += 1
            #...then put that word into the list
            words.append(phrase[startIndex: i])
            #this index is the start of the next word
            startIndex = i + 1
        i += 1
    
    return words

def main():
    
    phrase = ""
    tempChoice = "y"
    
    while tempChoice == ANSWERS[0].lower()  or \
          tempChoice == ANSWERS[1].lower():
        phrase = getHawaiianPhrase().upper()
        print("The phrase " + phrase + " is pronounced: ")
        print("\t" + pronounce(phrase))
        tempChoice = getChoice(CONTINUE, ANSWERS)

    
main()
