'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #3
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user to input the year and output if this year is a leap year or not

OUTPUT to monitor:
 num_year is a leap year or num_year is not a leap year

INPUT from keyboard:
 num_year - give a year

FORMULAS:
num_year % 4 == 0
num_year % 100 == 0
num % 400 == 0






'''




# Explain purpose of program to user
# This program to check if a input year is a leap year or not



import math


FOUR = 4
ZERO = 0
HUNDRED = 100
FOUR_HUNDRED = 400

print("This program determines if a given year is a leap year or not")
  
def main():
    num_year_str = input("Enter a year (Common Era only):   ")
    num_year = int(num_year_str)

#if else statement  
      
    if (num_year % FOUR == ZERO) and  ( num_year % HUNDRED != 0 )or\
       ( num_year % FOUR_HUNDRED == ZERO):
        print ("%d is a leap year" %num_year)
    else:
        print ("%d is not a leap year" %num_year)
        
    print ()


# for 1800 to 2100

    for num_year in range (1800, 2101, 10):
         if (num_year % FOUR == ZERO) and  ( num_year % HUNDRED != 0 )or\
            ( num_year % FOUR_HUNDRED == ZERO):
           print ("%d is a leap year" %num_year)
         else:
           print ("%d is not a leap year" %num_year)
          
main()
  















