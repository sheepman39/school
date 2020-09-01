# Add your code here and add comments to your code 
#   to describe what each section of code is doing
#   code is asking the user their name and what the name of their pirate ship will be
user_name=input("Avast me harty! This be ye new pirate vessel. But before we can transfer the deed to ye we gonna be needin' some information from ye. Fer starters, wat ye be called? ")
ship_name=input("Welcome aboard "+user_name+"! This be yer new vessel. But first she be needin' a name. Wat ye be callin' yer vessel? ")

#   we are congratumalating the user on their name?
print("That be a nice name "  + user_name + " We be callin' ye vessel the " + ship_name)
import turtle as turtl
painter = turtl.Turtle()

# moveto function makes it easier to move the turtle
def moveto(x,y):
  painter.penup()
  painter.goto(x,y)
  painter.pendown()

#Draws the hull of the ship  
painter.turtlesize(3)
painter.pensize(3)
painter.speed(100)
painter.pencolor("#6b3813")
painter.fillcolor("#a16032")
painter.begin_fill()
moveto(-50,-50)
painter.right(90)
painter.circle(100,180,90)
painter.setheading(180)
painter.forward(200)

#Paints the one part of the hull
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

# asks users what color and how many sails
sail_color = input("What color would ye like the sails to be? ")
sail_num = int(input("Would ye like 1 sail or 2? "))

# draws the first sail
painter.fillcolor(sail_color)
painter.backward(100)
painter.pencolor('#3d1d06')
painter.pensize(8)
painter.right(90)
painter.pendown()
painter.begin_fill()
painter.forward(150)
painter.right(135)
painter.pencolor("yellow")
painter.forward(150)
painter.right(135)
painter.forward(100)
painter.end_fill()
moveto(-30,5)

# draws the second sail
if sail_num == 2:
    painter.right(90)
    painter.pencolor('#3d1d06')
    painter.pendown()
    painter.begin_fill()
    painter.forward(150)
    painter.right(135)
    painter.pencolor("yellow")
    painter.forward(150)
    painter.right(135)
    painter.forward(100)
    painter.end_fill()
print("Good job " + user_name + "! Your ship " + ship_name +" is finished and those are some pretty good sails ya go")
painter.hideturtle()
wn = turtl.Screen()
wn.mainloop()
