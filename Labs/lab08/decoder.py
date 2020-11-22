# File:    decoder.py
# Started: by Dr. Gibson
# Author:  YOUR NAME GOES EHRE
# Date:    DATE GOES HERE
# Section: SECTION NUMBER GOES HERE
# E-mail:  EMAIL_GOES_HERE@umbc.edu
# Description:
#   This file contains python code that uses a function to 
#   pull out the uppercase letters from a list of strings
#   to decode a secret message.


######################################################################
# decode() decodes a message by extracting all of the 
#          lowercase letters to reveal the hidden meaning
# Input:   msgList; a list of strings
# Output:  secret;  a string containing the hidden message
def decode(msgList):
    secret = ""

    #-----------------------------------------------#
    # your code that goes through the list, finding #
    #  the message hidden in lowercase, goes here   #
    #-----------------------------------------------#

    i = 0
    while i < len(msgList):
        strCount = 0
        while strCount < len(msgList[i]):
            if msgList[i][strCount] != msgList[i][strCount].upper():
                secret += msgList[i][strCount]
            strCount += 1
        i += 1
    
    return secret



def main():
    # message lists
    msg1 = ["THIs", "LIFe", "cANNOT", "rEALLY", "Be", "tRUE"]
    msg2 = ["WONdERING", "HoW", "gOOD", "SCOREs", "CaN", "REGULArLY", \
                "Be", "MANAgED", "YoU", "SHoULD", "STUdY"]
    msg3 = ["ThE", "DoG", "OCCUpIES", "HeR", "DAILy", "THoUGHTS", "THROuGH", \
            "WhICH", "aLL", "DAYdREAMS", "aRE", "gENERATED", "FrOM", "EVeN", \
            "aMONG", "tHE", "bEST", "FrIENDS", "THeY", "aRE", "kNOWN"]

    # calling the decode function for each
    ans1 = decode(msg1)
    ans2 = decode(msg2)
    ans3 = decode(msg3)

    # printing out the secret messages
    print("Message 1's secret was:")
    print(ans1)
    print()

    print("Message 2's secret was:")
    print(ans2)
    print()

    print("Message 3's secret was:")
    print(ans3)
    print()



main()

