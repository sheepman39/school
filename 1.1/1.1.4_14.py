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
  # x will be increased by 50 each time 
  # y will be reset each time the loop runs to 200
  x = x + 50
  y = 200
  
  while (y > -200):
    
    # to control movement, y is subtracted by 50 each time
    # the loop will keep running as long as y is greater than -200
    y -= 50
    
    # the turtle will go to coordinates x,y and set the color to orange
    painter.goto(x,y)
    painter.color("orange")
    
    # if the x position is -150, it will set the color to purple instead
    if(x == -150):
      
      painter.color("purple")
    
    # then the turtle will stamp its shape in the same color as determined above
    painter.stamp()
    
    
#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

# creates and displays the screen
wn = trtl.Screen()
wn.mainloop()
