#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
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
