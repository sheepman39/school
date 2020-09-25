# 1.1.9_final_project.py
import turtle as trtl

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
#Builds the center line and circle

#First and center circle
painter.turtlesize(0.7)
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
painter.pensize(5)
painter.goto(0,190)
painter.goto(0,-190)

wn = trtl.Screen()
wn.mainloop()
