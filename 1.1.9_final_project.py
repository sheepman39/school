# 1.1.9_final_project.py
import turtle as trtl
import random
# create the turtle object
painter = trtl.Turtle()
screen = trtl.Screen()
screen.setup(280, 190)
trtl.bgcolor("#72b964")
painter.color("white")

def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()

def random_num(low, high):
  return random.randrange(low,high)

#Variables
triangle_team = []
square_team = []

#Builds the center line and circle
#First and center circle
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
painter.forward(115)
painter.left(90)
painter.forward(150)
painter.left(90)
painter.forward(225)
painter.left(90)
painter.forward(150)
painter.left(90)
painter.forward(110)
painter.goto(0,-66)

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
painter.forward(110)
painter.pendown()
for i in range(2):
  painter.left(90)
  painter.forward(37.5)
painter.left(90)
painter.forward(75)
painter.left(90)
painter.forward(37.5)

#Tricky part of spawning in the teams
#tt stands for triangle team
#st stands for square team
i = 0
while(i <= 10):
  tt = trtl.Turtle(shape="triangle")
  st = trtl.Turtle(shape="square")
  square_team.append(st)
  triangle_team.append(tt)
  tt.turtlesize(0.5)
  st.turtlesize(0.5)
  tt.color("blue")
  st.color("red")
  tt.penup()
  st.penup()
  tt.goto(random_num(-150, 150), random_num(-80, 80))
  st.goto(random_num(-150, 150), random_num(-80, 80))
  i += 1

wn = trtl.Screen()
wn.mainloop()
