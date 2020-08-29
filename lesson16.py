# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.speed(10)
painter.pensize(5)
def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
 
# add code here for a circle
painter.circle(100)

# move the turtle to another part of the screen
moveto(-150,-150)

# add code here for an arc
painter.circle(100,274)

# move the turtle to another part of the screen
moveto(150, 150)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(100, 290, 5)

# move the turtle to another part of the screen
moveto(-150,150)

# add code here to create a polygon of your choice using the circle method
painter.setheading(180)
painter.circle(100,360,8)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()