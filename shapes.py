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
    
def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  
  
shape_creator(4,100)
moveto(70,0)
shape_creator(8,60)
moveto(-100,100)
shape_creator(5,80)


wn = trtl.Screen()
wn.mainloop()
