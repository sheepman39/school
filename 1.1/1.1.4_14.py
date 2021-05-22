#   a114_nested_loops_2.py 
import turtle as trtl

# setup of the turtle
painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

# sets the default x position to -200
x = -200

while (x < 200): 

  # since this loop will continue
  x = x + 50
  y = 200
  while (y > -200):
    y -= 50
    painter.goto(x,y)
    painter.color("orange")
    if(x == -150):
      painter.color("purple")
    painter.stamp()
#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue
wn = trtl.Screen()
wn.mainloop()
