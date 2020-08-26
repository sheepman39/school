import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(3)
painter.pensize(5)
painter.pencolor('black')
def shape_creator(sides,length):
  repeat = 0
  while repeat < sides:
    painter.right(360/sides)
    painter.forward(length)
    repeat = repeat + 1

shape_creator(4,100)
painter.penup()
painter.goto(50,0)
painter.pendown()
shape_creator(8,60)
