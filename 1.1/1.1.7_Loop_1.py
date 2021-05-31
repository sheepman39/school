#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# creates lists of shapes and corresponding colors for them
# ex the first circle-shaped turtle will be green
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

# this for loop takes each shape and temporarily stores it in the 's' variable
for s in turtle_shapes:

  # temp_turtle is a new turtle that is created with the shape 's' and is added to the my_turtles list using the .append method
  temp_turtle = trtl.Turtle(shape=s)
  my_turtles.append(temp_turtle)

  # the .pop() method of turtle_colors removes the last index of the list and stores it in the current_color variable
  current_color = turtle_colors.pop()

  # this color is then set to the temp_turtle
  temp_turtle.pencolor(current_color)
  temp_turtle.color(current_color)

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

# Sets the starting position of the first turtle
startx = 0
starty = 0
rotate = 270
forward = 55

# in this case, the variable i represents how many times the loop has iterated
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
  forward = 55 + i*5
  t.forward(int(forward))
  
  # next loop, the turtle will move forward more
  i += 1

#	Sets the next position up for the next turtle
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
