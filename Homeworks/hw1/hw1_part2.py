# File:        hw1_part2.py
# Author:      Mitchell Angelos
# Date:        2/9/19
# Section:     Section 12
# E-mail:      a242@umbc.edu
# Description: This program calculates the user's earned amount
#              of candy bars based on their daily income and
#              favorite candy bar cost.

def main():

    dailyIncome = int(input("Please enter your daily income: "))
    candyBarCost = int(input("Please enter how much your favorite candy costs: "))
    print("You earned", (dailyIncome / candyBarCost), " candy bars today!")



main()
