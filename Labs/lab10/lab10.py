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
    m=int(input("Enter an integer between"+str(minn)+"and"+str(maxx)+"(inclusive):"))#message to ask the user
    num=int(input(m))
    while num<=minn and num>=maxx:
        print("Invalid choice!")
        num=int(input(m))
    #return result
    return num
#counts dupes
def twoInARow():
    ans="No duplicates next to each other"
    c=0
    i=0
    #go through the list
    while i<len(stuff):
        if stuff[i]==stuff[i+1]:
            print("Found dupes of",stuff[i],"next to each other.")#print out the result if a dupe is found
        c+=1
    return c
#compare things
def equiv(i1,i2):
    res=""
    #if the same
    if i1==i2:
        res="They match!"
    #if not thesame
    else:
        res="No match"
#avg
def average():
    i=0
    while i<len(n):
        i+=1
    t+=i
    a=t/n
    #return average
    return a
def main():
    #TEST ONE FUNCTION AT A TIME, AND MAKE SURE IT WORKS
    #BEFORE UNCOMMENTING THE NEXT ONE
    num1=getValidInt(MINN,MAXX)
    print("Thank you for choosing",num)
    #check for duplicates next to each other
    ###numbers = [1,0,4,4,3,2,6,2,7,7,9
    ###twoInARow(numbers
    ###print("Given the list:", numbers)
    ###print("The result of the nearby duplicate test:")
    ###print("There are",result,"matches")
    #check to see if the number from the user is the same as the last
    #number in the list of numbers from before, and print out the answer
    ###result = equiv(num1,numbers[len(numbers)-1])
    ###print("The result of the equivalence test:",res)
    #calculate the average of the list
    ###average = average(numbers)
    ###print("The average is",average)

    #this file should have given you a taste of why comments, function headers,
    #good variable names, and following coding standards is so important 
    #to making code readable both for yourself and others (like the TAs!)
    #you can get the REAL lab09.py file by using the command
    #cp /afs/umbc.edu/users/k/k/k38/pub/cs201/less_broken.py lab10.py
main()