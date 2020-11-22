# File:        hw4_part3.py
# Author:      Mitchell Angelos
# Date:        3/3/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program asks the user to enter a password then checks
#              if it's valid. If not, the user must get a valid password.

MIN_PASS_LENGTH = 6
MAX_PASS_LENGTH = 20

MIN_SMALL_PASS = 6
MAX_SMALL_PASS = 13

MIN_LONG_PASS = 14
MAX_LONG_PASS = 20

SMALL_PASS_CONTAIN = "7"
LONG_PASS_CONTAIN = "2"

CHAR_NO_ACCEPT_ONE = "O"
CHAR_NO_ACCEPT_TWO = "0"

def main():

    #the boolean flag that checks
    valid = False

    while valid != True:
        password = input("Please enter a password: ")
        valid = True

        hasUppercase = False
        uppercaseCount = 0
        while uppercaseCount < len(password):
            #checks if char in password is uppercase
            if password[uppercaseCount].isupper():
                hasUppercase = True
            uppercaseCount += 1
        #checks if boolean flag to show if an uppercase is present is false
        if hasUppercase == False:
            print("You must have one uppercase letter in your password.")
            valid = False

        hasLowercase = False
        lowercaseCount = 0
        while lowercaseCount < len(password):
            #checks if char in password is lowercase or not
            if password[lowercaseCount].islower():
                hasLowercase = True
            lowercaseCount += 1
        #checks bool flag with lowercase status
        if hasLowercase == False:
            print("You must have one lowercase letter in your password.")
            valid = False
        
        #checks if password length is between 6 and 20.
        if len(password) >= MIN_PASS_LENGTH and len(password) <= MAX_PASS_LENGTH:
            #checks if password length is between 6 and 13
            if len(password) >= MIN_SMALL_PASS and len(password) <= MAX_SMALL_PASS:
                hasSeven = False
                hasSevenCount = 0
                while hasSevenCount < len(password):
                    #if this character in the string has "7" in it
                    if password[hasSevenCount] == SMALL_PASS_CONTAIN:
                        hasSeven = True
                    hasSevenCount += 1
                #checks boolean var that marked if there was a 7 in the
                #password string
                if hasSeven == False:
                    print("Since your password is between 6 and 13"\
                          ,"characters, you need a 7 in your password.")
                    valid = False
            #if password length is between 14 and 20.
            elif len(password) >= MIN_LONG_PASS and len(password) <= MAX_LONG_PASS:
                hasTwo = False
                hasTwoCount = 0
                while hasTwoCount < len(password):
                    #if this character in the string has "2" in it
                    if password[hasTwoCount] == LONG_PASS_CONTAIN:
                        hasTwo = True
                    hasTwoCount += 1
                #checks boolean var that marked if there was a 2 in the
                #password string or not
                if hasTwo == False:
                    print("Since your password is in between 14 and"\
                          ,"20 characters, you need a 2 in your password.")
                    valid = False
        #if password length is not between 6 and 20
        else:
            print("Password must be between 6 and 20 characters.")
            valid = False

        hasLetterO = False
        hasNumberZero = False
        passwordLengthCount = 0
        while passwordLengthCount < len(password):
            #checks if the character in the password has "O" in it
            if password[passwordLengthCount] == CHAR_NO_ACCEPT_ONE:
                hasLetterO = True
            #checks if the character in the password has "0" in it
            if password[passwordLengthCount] == CHAR_NO_ACCEPT_TWO:
                hasNumberZero = True
            passwordLengthCount += 1
        #checks if both boolean flags are true to see if both 0 and O are in
        #the password.
        if hasLetterO == True and hasNumberZero == True:
            print("Your password must not have the capital letter O"\
                  ,"and the number 0 in the password at the same time.")
            valid = False
        

    print("Your accepted password is",password)
main()
