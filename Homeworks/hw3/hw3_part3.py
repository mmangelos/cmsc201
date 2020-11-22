# File:        hw3_part3.py
# Author:      Mitchell Angelos
# Date:        2/28/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program collects data from the user about info found
#              from an alien planet.

PLANT_TYPE = "plant"
ANIMAL_TYPE = "animal"
MINERAL_TYPE = "mineral"

THREAT_LEVEL_LOWER_BOUND = 0.0
THREAT_LEVEL_UPPER_BOUND = 1.0

def main():

    faunaType = input("Please enter the type of object you are observing: ")
    while faunaType != PLANT_TYPE and faunaType != ANIMAL_TYPE and faunaType != MINERAL_TYPE:
        print("Invalid type. Must be " + PLANT_TYPE + ", " + ANIMAL_TYPE + ", or " + MINERAL_TYPE + ".")
        faunaType = input("Please enter the type of object you are observing: ")

    weight = float(input("Please enter its weight: "))
    while weight <= 0.0:
        print("Please enter a valid weight. Must be over 0.0.")
        weight = float(input("Please enter its weight: "))

    threatLevel = float(input("Please enter a threat level between 0 and 1: "))
    while threatLevel < 0.0 or threatLevel > 1.0:
        if threatLevel < 0.0:
            threatLevel = float(input("Invalid level. Threat is too low. Please enter a value between 0 and 1: "))
        elif threatLevel > 1.0:
            threatLevel = float(input("Invalid level. Threat is too high. Please enter a value between 0 and 1: "))

    print("Data recorded for " + str(faunaType) + ", weighing in at " + str(weight) + " grams, with a threat level of " + str(threatLevel) + ".")

main()
