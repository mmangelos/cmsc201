# File:        hw2_part5.py
0;136;0c# Author:      Mitchell Angelos
# Date:        2/18/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This is a day of the week calculator for a 28 day month
#              with the first day starting on Friday (the 1st)

def main():

    dayOfTheWeek = int(input("Please enter the day of the month: "))

    if dayOfTheWeek < 1 or dayOfTheWeek > 28:
        print("The date " + str(dayOfTheWeek) + " is an invalid day.")
    elif dayOfTheWeek % 7 == 1:
        print("Today's a Friday!")
    elif dayOfTheWeek % 7 == 2:
        print("Today's a Saturday!")
    elif dayOfTheWeek % 7 == 3:
        print("Today's a Sunday!")
    elif dayOfTheWeek % 7 == 4:
        print("Today's a Monday!")
    elif dayOfTheWeek % 7 == 5:
        print("Today's a Tuesday!")
    elif dayOfTheWeek % 7 == 6:
        print("Today's a Wednesday!")
    elif dayOfTheWeek % 7 == 0:
        print("Today's a Thursday!")
    
main()
