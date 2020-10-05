# 1.1.9_final_project.py
import turtle as trtl
import random

# create the turtle object
painter = trtl.Turtle()
screen = trtl.Screen()

#Changes the size of the canvas
screen.setup(280, 200)

#Changes the background color and painter color
trtl.bgcolor("#72b964")
painter.color("white")

#Shortcut moveto function helps 
#Moving the turtle to a specific location
def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()

#Shortcut for creating random numbers
def random_num(low, high):
  if(low > high):
    return random.randrange(high,low)
  return random.randrange(low,high)

#Variables
triangle_team = []
arrow_team = []

#First and center circle
painter.speed(-1)
painter.turtlesize(0.5)
painter.setheading(90)
painter.shape("circle")

#Draws the larger circle
moveto(0,0)
painter.stamp()
painter.setheading(0)
moveto(0,-20)
painter.pensize(3)
painter.circle(20)
painter.right(90)

#Draws the center line
painter.shape("arrow")
painter.pensize(5)
painter.goto(0,80)
painter.setheading(90)
painter.left(90)

#Draws the perimiter of the
#Soccer Field
painter.forward(115)
painter.left(90)
painter.forward(160)
painter.left(90)
painter.forward(230)
painter.left(90)
painter.forward(160)
painter.left(90)
painter.forward(115)
painter.goto(0,-80)

#draws the arcs
moveto(-115,80)
painter.circle(80,-180,200)
moveto(115,-80)
painter.circle(80,-180,200)

#Left Goal
moveto(0,0)
painter.setheading(180)
painter.penup()
painter.forward(115)
painter.pendown()
for i in range(2):
  painter.right(90)
  painter.forward(37.5)
painter.right(90)
painter.forward(75)
painter.right(90)
painter.forward(37.5)

#Right Goal
moveto(0,0)
painter.setheading(0)
painter.penup()
painter.forward(115)
painter.pendown()
for i in range(2):
  painter.left(90)
  painter.forward(37.5)
painter.left(90)
painter.forward(75)
painter.left(90)
painter.forward(37.5)

'''
 The rest of the code is for
 Spawning in the two teams
 in the correct locations
 
 tt stands for triangle team
 at stands for arrow team
'''

#While loop creates new turtle objects and puts them in the array
i = 0
while(i <= 9):
  
  #Creates the turtle, assigns a color, size, shape, and sets the location to a random spot
  tt = trtl.Turtle(shape="triangle")
  at = trtl.Turtle(shape="arrow")
  arrow_team.append(at)
  triangle_team.append(tt)
  tt.turtlesize(0.5)
  at.turtlesize(0.5)
  tt.color("blue")
  at.color("red")
  tt.penup()
  at.penup()
  
  #Balences out the teams so they spawn in different locations
  #2 midfield per team
  if(i<=1):
    tt.goto(random_num(-20, 20), random_num(-50, 70))
    at.goto(random_num(-20, 20), random_num(-50, 70))

  #4 defence per team
  elif(i >= 2 and i <= 5):
    tt.goto(random_num(-75, -25), random_num(-50, 70))
    at.goto(random_num(25, 75), random_num(-50, 70))

  #4 Offence per team
  elif(i >= 6 and i <= 9):
    tt.goto(random_num(25, 75), random_num(-50, 70))
    at.goto(random_num(-75, -25), random_num(-50, 70))
  
  #Changes the direction depending on which side of the field they are on.
  if(tt.xcor() <= 0):
    tt.setheading(0)
  
  elif(tt.xcor() >= 0):
    tt.setheading(180)
 
  #Same thing above but for the arrow team
  if(at.xcor() <= 0):
    at.setheading(180)
  
  elif(at.xcor() >= 0):
    at.setheading(0)
  
  #For loop controls collisions between the different teams
  for j in triangle_team:
      if(abs(j.xcor()-at.xcor()) < 15 and abs(j.ycor()-at.ycor()) < 15):
        at.forward(-15)
        j.goto(j.xcor(),j.ycor()-25)

  #For loops controls collisisons among the same team members
  for k in triangle_team:
    for z in triangle_team:
      if(k != z):
        if(abs(k.xcor()-z.xcor()) < 15 and abs(k.ycor()-z.ycor()) < 15):
          z.forward(20)
          k.goto(k.xcor(),k.ycor()-25)
  
  for k in arrow_team:
    for z in arrow_team:
      if(k != z):
        if(abs(k.xcor()-z.xcor()) < 15 and abs(k.ycor()-z.ycor()) < 15):
          z.forward(20)
          k.goto(k.xcor(),k.ycor()+25)
  
  i += 1
wn = trtl.Screen()
wn.mainloop()
