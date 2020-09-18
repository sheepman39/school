#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
# This comment was written by me. ha
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  current_color = turtle_colors.pop()
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  t.pencolor(current_color)
  t.color(current_color)

# Sets the starting position
startx = 0
starty = 0
rotate = 270
forwar = 55
i = 1
# For the number of shapes that are available, go right 45 and move forward 50
for t in my_turtles:
  
  t.penup()
  t.pensize(5)
  t.goto(startx, starty)
  t.setheading(rotate)
  rotate += 45 
  t.pendown()
  t.right(45)
  forwar = 55+i*5
  t.forward(int(forwar))
  i += 1

#	Sets the next position up 50,50
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
