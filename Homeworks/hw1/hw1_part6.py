# File:        hw1_part6.py
# Author:      Mitchell Angelos
# Date:        2/9/19
# Section:     Section 12
# E-mail:      a242@umbc.edu
# Description: This program calculates the bill after accomodating for tax
#              and tip percentage, values supplied by the user.

def main():

    billAmount = float(input("Please enter how much the bill is: "))
    taxAmount = float(input("Please enter how much the tax is in your area: "))
    tipAmount = float(input("Please enter tip percentage: "))

    taxAmount /= 100
    taxAmount += 1
    #print(taxAmount)
    tipAmount = billAmount * (tipAmount / 100)
    #print(tipAmount)
    totalBill = billAmount * taxAmount
    totalBill += tipAmount
    print("The total cost of the meal will be", totalBill)
    


main()
