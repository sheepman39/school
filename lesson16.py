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
moveto(-100,-100)

# add code here for an arc
painter.circle(75,274)

# move the turtle to another part of the screen
moveto(25, -100)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(75, 290, 5)

# move the turtle to another part of the screen
moveto(-100,100)

# add code here to create a polygon of your choice using the circle method
painter.setheading(90)
painter.circle(45,360,8)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
