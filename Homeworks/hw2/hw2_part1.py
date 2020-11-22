# File:        hw2_part1.py
# Author:      Mitchell Angelos
# Date:        2/17/19
# Section      12
# E-mail:      a242@umbc.edu
# Description: This program gives feedback afer asking the user what they're
#              majoring in.

def main():

    print("Please input your major(s). Enter 'NONE' for no response.")
    firstMajor = input("Please enter your first major: ")
    secondMajor = input("Please enter your second major: ")

    if firstMajor == "NONE" and secondMajor == "NONE":
        print("You need to pick a major soon!")
    elif firstMajor == secondMajor:
        print("You can't double major in the same thing!")
    elif firstMajor != "NONE" and secondMajor == "NONE":
        print("It's cool that you're focusing on " + firstMajor)
    elif firstMajor == "NONE" and secondMajor != "NONE":
        print("It's cool that you're focusing on " + secondMajor)
    elif (firstMajor == "CMSC" and secondMajor == "CMPE") or (firstMajor == "CMPE" and secondMajor == "CMSC"):
        print("You can't major in CMSC and CMPE, unfortunately.")
    else:
        print(firstMajor + " and " + secondMajor + " sounds like a good combination!")

main()
