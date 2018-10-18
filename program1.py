#Author: Darin Ellis
#Email: dmel227@g.uky.edu
#Section 014
#Purpose: To create a program that correctly calculates and displays the cost per 
#gigabyte over a range of years input by the user.
#Date Completed: 8/27/2014
#Preconditions: 3 inputs from the user: start and end of the range, plus the step size.
#Postconditions: Outputs a table with range and cost. Prints to the shell.

from math import *

def main():
    
    #Program Title
    print(" ")
    print("Big Blue Hard Drive Storage Cost")
    print(" ")

    #Inputs
    start = int(input("Enter the starting year: "))
    end = int(input("Enter the ending year: "))
    step = int(input("What step size for the table? "))
    
    #Table Formatting
    print(" ")
    print("        Hard Drive Storage Costs Table")
    print(" ")
    print("Start Year = ", start)
    print("End Year =", end)
    print(" ")
    print("         Year             Cost Per Gigabyte ($)")
    print(" ")
    
    #Loop - calculates cost and prints table - also rounds to 3 decimal places
    for i in range(start, end + 1, step):
        print("        ",i, "                 ", str(round((10 ** (-0.2502 * (i-1980) +6.304)),3)))
        
main()

#Bonus
#As an exponential function, (10 ** (-0.2502 * (i-1980) +6.304)) never equals 0.
#It can, however, approach 0 as it becomes exponentially smaller as i increases.
#In my program, the first year to display 0 is 2019. This is a product of the round 
#function. When this program is run without the round function, 
#it returns an output of 0 at 3299. 