import turtle as trtl

# create and setup the painter turtle
painter = trtl.Turtle()
painter.turtlesize(3)
painter.pensize(5)
painter.pencolor('black')

# this is a function that will take the number and length of sides you want and make that shape
def shape_creator(sides,length):
  repeat = 0
  
  while repeat < sides:
    painter.right(360/sides)
    painter.forward(length)
    repeat = repeat + 1

# moveto is a function to move the turtle to a new location
def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  
# creates a 4 sided shape with a length of 100 pixels  
shape_creator(4,100)
moveto(70,0)

# creates an 8 sided shape with a length of 60 pixels
shape_creator(8,60)
moveto(-100,100)

# creates a 5 sided shape with a length of 80 pixels
shape_creator(5,80)


wn = trtl.Screen()
wn.mainloop()
