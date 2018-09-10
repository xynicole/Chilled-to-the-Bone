'''
Xinyi Huang (Nicole)
xhuang78@binghamton.edu
B58 Jia Yang
Assignment #2
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many points does the star have
  and output the picture of star

OUTPUT to monitor:
  turtle - picture of star

INPUT from keyboard:
  points_count (int) - number of points of star


GIVENS: 
  POINTS_COUNT (int) >= 3
  POINTS_COUNT (int) <= 15
  
FORMULA:
 360 / n
 n = points_count

'''

 



# Explain purpose of program to user
# This program outputs the picture of the star polygon


def main():

  import turtle
  wn = turtle.Screen()
  ella = turtle.Turtle()
 

  print("This program draws a polygon star given the number of points")

  # Ask user for number of points of star
  points_count_str = input("Enter the number of points in the star to be drawn    ")
  
  # Convert str data to int
  points_count = int(points_count_str)

  #fomula and data
 
  angle = 360 / points_count
  length_side = 50

  
  

  #Creat loop

  for i in range(points_count):
      ella.right(60)
      ella.forward(length_side)
      ella.left(120)
      ella.forward(length_side)
      ella.right(60 - angle)
   

  wn.exitonclick()
  
main() 
