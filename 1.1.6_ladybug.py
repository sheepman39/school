#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
#creates legs
legs = 0
ladybug.pensize(10)
while(legs < 3):
  ladybug.goto(0,-25)
  ladybug.setheading(155+legs*25)
  ladybug.forward(60)
  ladybug.backward(120)
  legs += 1
# and body
ladybug.penup()
ladybug.goto(-5, -25) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

  
# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 13, ypos + 30)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos += 25
  ypos += 5
  num_dots += 1
  

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
