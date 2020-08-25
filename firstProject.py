import turtle as trtl

painter = trtl.Turtle()

#Startup things.  repeat is used for the while loops
repeat = 0
painter.turtlesize(3)
painter.pensize(5)
painter.pencolor('#ebeef0')

#goes to the upper corner to start
painter.penup()
painter.goto(-150,150)
painter.setheading(180)
painter.pendown()

#while loop draws the rectangle without writing the same code again
painter.fillcolor('#272932')
painter.begin_fill()
while repeat < 2:
  painter.left(90)
  painter.forward(200)
  painter.left(90)
  painter.forward(150)
  repeat = repeat + 1
painter.end_fill()


#draws the triangle
painter.fillcolor('#47484b')
painter.begin_fill()
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(150)
painter.right(117)
painter.forward(167.7)
painter.right(126)
painter.forward(160)
painter.end_fill()

wn = trtl.Screen()
wn.mainloop()

