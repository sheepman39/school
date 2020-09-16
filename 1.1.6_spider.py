#   a116_spider.py
import turtle as trtl

# create spider head
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(5)

#create eyes
spider.pensize(5)
spider.turtlesize(1)
spider.pencolor('red')
spider.color('#d91a09')
spider.shape('triangle')
spider.penup()
spider.setheading(90)
spider.goto(10,15)
spider.stamp()
spider.goto(-10,15)
spider.stamp()
#creates legs
spider.pencolor('black')
legs = 0
spider.pensize(10)
while(legs < 4):
  spider.goto(0,-30)
  spider.setheading(100+legs*25)
  spider.pendown()
  spider.circle(45,120)
  spider.penup()
  spider.backward(100)
  legs += 1
  
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
# and body
spider.penup()
spider.goto(15, -30) 
spider.color("black")
spider.pendown()
spider.pensize(40)
spider.circle(20)
spider.setheading(270)
spider.color("black")
spider.penup()
'''spider.goto(0, 5)
spider.pensize(2)
spider.pendown()
spider.forward(75)
'''

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
