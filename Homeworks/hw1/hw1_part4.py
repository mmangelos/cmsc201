# File:        hw1_part4.py
# Author:      Mitchell Angelos
# Date:        2/9/19
# Section:     Section 12
# E-mail:      a242@umbc.edu
# Description: This program calculates the total cost of a road trip.

def main():

    gasCost = float(input("Please enter gas cost: "))
    snacksCost = float(input("Please enter a snacks cost: "))
    tollsCost = float(input("Please enter tolls cost: "))
    drivingGlovesCost = float(input("Please enter the cost for your driving gloves: "))
    totalTripCost = gasCost + snacksCost + tollsCost + drivingGlovesCost
    print("The total cost of trip will be", totalTripCost)


main()
