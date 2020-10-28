import turtle as trtl

painter = trtl.Turtle()
x = 20
repeat = 0
hexSize = 30
painter.turtlesize(3)
painter.pensize(5)
painter.pencolor('#48f542')
colorArray = ['#ed0c1f','#48f542','#1dbabf','#c712ac','#f5ad14','#ed0c1f']

#Creates the square with dots
painter.right(45)
while repeat < 4:
  painter.forward(100)
  painter.right(90)
  painter.dot(x)
  repeat = repeat + 1
painter.setheading(0)

#Creates the circles
repeat = 0
while repeat < len(colorArray):
  painter.circle(repeat*10+10)
  painter.pencolor(colorArray[repeat])
  repeat = repeat +1

painter.penup()
painter.goto(-150,50)
painter.pendown()
painter.pencolor('#0ced93')

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue
#Creates the hexagon
repeat = 0
while repeat < 6:
  painter.forward(hexSize)
  painter.right(60)
  painter.stamp()
  repeat = repeat + 1

wn = trtl.Screen()
wn.mainloop()

