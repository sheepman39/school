# Add your code here and add comments to your code 
#   to describe what each section of code is doing
#   code is asking the user their name and what the name of their pirate ship will be
user_name=input("Avast me harty! This be ye new pirate vessel. But before we can transfer the deed to ye we gonna be needin' some information from ye. Fer starters, wat ye be called?")
ship_name=input("Welcome aboard "+user_name+" This be yer new vessel. But first she be needin' a name. Wat ye be callin' yer vessel.")

#   we are congratumalating the user on their name?
print("That be a nice name "  + user_name + " We be callin' ye vessel the " + ship_name)
import turtle as turtl
painter = turtl.Turtle()

def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()
  
painter.turtlesize(3)
painter.pensize(3)
painter.speed(10)
painter.pencolor("#6b3813")
painter.fillcolor("#a16032")
painter.begin_fill()
moveto(-50,-50)
painter.right(90)
painter.circle(100,180,90)
painter.setheading(180)
painter.forward(200)


painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.end_fill()

painter.penup()
painter.backward(100)
painter.pencolor('#3d1d06')
painter.pensize(8)
painter.right(90)
painter.pendown()
painter.forward(150)
wn = turtl.Screen()
