# File:        hw2_part2.py
# Author:      Mitchell Angelos
# Date:        2/17/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: Rounds a number up or down based on user input.

def main():

    userNumber = float(input("Input a number you want to round: "))
    roundAnswer = input("Please enter if you want to round 'up' or 'down': ")
    
    print("Original number: " + str(userNumber))
    if roundAnswer != "up" and roundAnswer != "down":
        print("Invalid choice. No further action needed.")
    if roundAnswer == "up":
        if userNumber % 1 == 0:
            print("No rounding needed.")
            print("Rounded number: " + str(int(userNumber)))
        else:
            if userNumber > 0:
                print("Rounding up!")
                print("Rounded number: " + str((int(userNumber)) + 1))
            else:
                print("Rounding up!")
                print("Rounded number: " + str(int(userNumber)))
    elif roundAnswer == "down":
        if userNumber % 1 == 0:
            print("No rounding needed.")
            print("Rounded number: " + str(int(userNumber)))
        else:
            print("Rounding down...")
            print("Rounded number: " + str(int(userNumber)))
    
main()
