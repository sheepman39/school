#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo"]

tloc = -50
for s in turtle_shapes:
  
  #Adds a new turtle to the horiz_turtles list
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-100, tloc)
  ht.setheading(0)
  
  #Adds a new turtle to the vert_turtles list
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 100)
  vt.setheading(270)
  
  #Changes the location of the turtles
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

  steps = 0
  while steps < 500: 
    steps += 1
    speed = 1
    for v in vert_turtles:
      for h in horiz_turtles:
        if(speed > 1 and speed < 5):
          speed += 1
        else:
          speed -+ 3
        ht.speed(speed)
        vt.speed(speed)
        ht.forward(3)
        vt.forward(3)
        if(abs(ht.xcor()-vt.xcor()) < 20 and abs(ht.ycor()-vt.ycor()) < 20):
          ht_shape = ht.shape()
          vt_shape = vt.shape()
          ht_color = ht.fillcolor()
          vt_color = vt.fillcolor()
          vt.fillcolor("#a2d145")
          ht.fillcolor("#a2d145")
          vt.shape("square")
          ht.shape("square")
          vt.forward(30)
          ht.forward(-30)
          vt.shape(vt_shape)
          ht.shape(ht_shape)
          vt.fillcolor(vt_color)
          ht.fillcolor(ht_color)
        if(ht.xcor() > 150 or vt.ycor() < -150):
          ht.fillcolor("pink")
          vt.fillcolor("pink")
          steps = 501
#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue
for v in vert_turtles:
  for h in horiz_turtles:
    h.fillcolor("#961E82")
    v.fillcolor("#961E82")
    h.color("#961E82")
    v.color("#961E82")
wn = trtl.Screen()
wn.mainloop()
