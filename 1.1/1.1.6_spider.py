#   a116_spider.py
import turtle as trtl

# create spider turtle 
spider = trtl.Turtle()

# starts by making the head of the spider
spider.pensize(40)
spider.circle(5)

# creates eyes by stamping the turtles shape
spider.pensize(5)
spider.turtlesize(1)

# sets the color and shape of the turtle
spider.pencolor('red')
spider.color('#d91a09')
spider.shape('triangle')

# controls movement of the turtle
spider.penup()
spider.setheading(90)
spider.goto(10,15)
spider.stamp()
spider.goto(-10,15)
spider.stamp()

#creates legs using a while loop
spider.pencolor('black')
legs = 0
spider.pensize(10)

# creates 4 legs
while(legs < 4):

  spider.goto(0,-30)
  spider.setheading(100+legs*25)
  spider.pendown()
  spider.circle(45,120)
  spider.penup()
  spider.backward(100)
  legs += 1

# resets legs value and continues creating more legs
# the difference between this and the previous loop is the inverted direction of the circle method
legs = 0
spider.pensize(10)

while(legs < 4):

  spider.goto(0,-30)
  spider.setheading(180+legs*25)
  spider.pendown()
  spider.circle(45,-120)
  spider.penup()
  spider.backward(100)
  legs += 1

# Creates the body of the spider
spider.penup()
spider.goto(15, -30) 
spider.color("black")
spider.pendown()
spider.pensize(40)
spider.circle(20)
spider.setheading(270)
spider.color("black")
spider.penup()

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

# hides the turtle at the end
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
