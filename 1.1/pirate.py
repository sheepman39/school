import turtle as turtl
painter = turtl.Turtle()

# the program starts by asking the user their name and what the name of their pirate ship will be
'''
fun fact: to make it easier to put variables in strings, type 'f' in front of a string and when you need a variable, put the variable name in brackets {}
ex. apples = 20 print(f"I have {apples} apples!") and it will print out "I have 20 apples!"
This type of syntax is used throughout this program
'''
user_name=input("Avast me harty! This be ye new pirate vessel. But before we can transfer the deed to ye we gonna be needin' some information from ye. Fer starters, wat ye be called? ")
ship_name=input(f"Welcome aboard {user_name}! This be yer new vessel. But first she be needin' a name. Wat ye be callin' yer vessel? ")
print(f"That’s a fine choice {user_name}! We be callin' ye vessel the {ship_name}")

 
# moveto function makes it easier to move the turtle
def moveto(x,y):
 painter.penup()
 painter.goto(x,y)
 painter.pendown()
 
#Draws the hull of the ship 
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
sail_color = input("Oh, almsot forgot about the sails.\nWhat color would ye like the sails to be? ")
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

print(f"Good job {user_name}! Your ship {ship_name} is finished and those are some pretty good sails ya got")
painter.hideturtle()
wn = turtl.Screen()
wn.mainloop()
