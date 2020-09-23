#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
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
  tloc += 25

# TODO: move turtles across and down screen, stopping for collisions

  steps = 0
  while steps < 50: 
    steps = steps + 1
    speed = 1
    for v in vert_turtles:
      for h in horiz_turtles:
        if(speed > 1 and speed < 5):
          speed += 1
        else:
          speed -+ 1
        ht.speed(speed)
        vt.speed(speed)
        ht.forward(3)
        vt.forward(3)
        if(abs(ht.xcor()-vt.xcor()) < 20 and abs(ht.ycor()-vt.ycor()) < 20):
          ht_shape = ht.shape()
          vt_shape = vt.shape()
          vt.fillcolor("#a2d145")
          ht.fillcolor("#a2d145")
          vt.shape("square")
          ht.shape("square")
          #vert_turtles.remove(v)
          #horiz_turtles.remove(h)
          vt.forward(-30)
          ht.forward(-45)
        #else: 
          #vt.shape(vt_shape)
          #ht.shape(ht_shape)
        if(abs(ht.xcor()) > 180 or abs(ht.ycor() > 180)):
          ht.fillcolor("gray")
          horiz_turtles.remove(h) 
        if(abs(vt.xcor()) > 180 or abs(vt.ycor() > 180)):
          vt.fillcolor("gray")
          vert_turtles.remove(v)
wn = trtl.Screen()
wn.mainloop()
