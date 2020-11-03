import turtle as trtl
#Startup things.  repeat is used for the while loops
painter = trtl.Turtle()
repeat = 0
painter.turtlesize(3)
painter.pensize(5)
painter.pencolor('#000c45')
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
#Draws the lower triangle
painter.penup()
painter.fillcolor('#272932')
painter.goto(-80,-50)
painter.setheading(315)
painter.pendown()
painter.begin_fill()
painter.forward(100)
painter.setheading(180)
painter.forward(120)
painter.setheading(55)
painter.forward(100)
painter.end_fill()
#draws an octagon
repeat = 0
painter.penup()
painter.goto(35,150)
painter.setheading(0)
painter.pensize()
painter.fillcolor("red")
painter.pendown()
painter.begin_fill()
while repeat < 8:
  painter.forward(35)
  painter.right(360/8)
  repeat = repeat + 1
painter.end_fill()
painter.hideturtle()
#Draws the turtle
wn = trtl.Screen()
wn.mainloop()
