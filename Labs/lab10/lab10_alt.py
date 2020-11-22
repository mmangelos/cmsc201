#File: broken_lab10.py
#Author: Brendan Waters
#Email: b101@umbc.edu
#Updated by: Dr. Gibson  (k.gibson)
#Chris Block (christ34)
#Author: YOUR NAME GOES EHRE
#Date:DATE GOES HERE
#Section: SECTION NUMBER GOES HERE
#E-mail:EMAIL_GOES_HERE@umbc.edu
#Description:This file contains python code that is broken and needs to be debugged.
MINN=1
MAXX=100
#gets an integer
def getValidInt(minn,maxx):
    m="Enter an integer between "+str(minn)+" and "+str(maxx)+" (inclusive): "#message to ask the user
    num=int(input(m))
    while num<MINN or num>MAXX:
        print("Invalid choice!")
        num=int(input(m))
    #return result
    return num
#counts dupes
def twoInARow(stuff):
    ans="No duplicates next to each other"
    c=0
    i=0
    #go through the list
    while i<len(stuff):
        if i + 1 == len(stuff):
            i += 1
        elif stuff[i]==stuff[i+1]:
            print("Found dupes of " + str(stuff[i]) +" next to each other.")
            c+= 1
        i += 1
    return c
#compare things
def equiv(i1,i2):
    res=""
    #if the same
    if i1 == i2:
        res="They match!"
    #if not thesame
    else:
        res="No match"
    return res
#avg
def average(n):
    i=0
    t = 0
    while i<len(n):
        t += n[i]
        i+=1
    a=t/len(n)
    #return average
    return a
def main():
    #TEST ONE FUNCTION AT A TIME, AND MAKE SURE IT WORKS
    #BEFORE UNCOMMENTING THE NEXT ONE
    num1=getValidInt(MINN,MAXX)
    print("Thank you for choosing",num1)
    #check for duplicates next to each other
    numbers = [1,0,4,4,3,2,6,2,7,7,9]
    print("Given the list:", numbers)
    result = twoInARow(numbers)
    print("The result of the nearby duplicate test:")
    print("There are " + str(result) + " matches")
    #check to see if the number from the user is the same as the last
    #number in the list of numbers from before, and print out the answer
    result = equiv(num1,numbers[len(numbers)-1])
    print("The result of the equivalence test:", str(result))
    #calculate the average of the list
    avg = average(numbers)
    print("The average is",str(avg))

    #this file should have given you a taste of why comments, function headers,
    #good variable names, and following coding standards is so important 
    #to making code readable both for yourself and others (like the TAs!)
    #you can get the REAL lab09.py file by using the command
    #cp /afs/umbc.edu/users/k/k/k38/pub/cs201/less_broken.py lab10.py
main()
