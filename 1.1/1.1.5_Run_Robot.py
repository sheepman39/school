#   a114_robot_maze.py
import turtle as trtl

#------ robot algorithms
def move():
  robot.dot(10)
  robot.forward(50)

def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)
  
#----- robot starting location
startx = -100
starty = -100

#----- init screen
wn = trtl.Screen()
wn.setup(width=400, height=420)

#----- init robot
# TODO: Find robot.gif
# this will add the robot shape to the images 
# NOTE: Since this program is in a folder, we need to tell python to look in that folder.  This should not be necessary on standalone projects
robot_image = "./1.1/robot.gif"
wn.addshape(robot_image)

# creates the details and setup of the robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO 1: change maze here
wn.bgpic("./1.1/maze2.png") # other file names should be maze2.png, maze3.png

#---- TODO 2: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
# maze3
move()
i = 0
while (i<3):
  turn_left()
  i += 1
i = 0
while (i < 2): # forward 3
  i += 1
  move()
turn_left()
i = 0
while (i < 2): # forward 3
  i += 1
  move()
i = 0
while (i<3):
  turn_left()
  i += 1
i = 0
while (i < 2):
  move()
  i += 1
turn_left()
move()
'''
'''
#maze 2
i = 0
while (i < 3): # forward 3
  i += 1
  move()
#turn_left()
i = 0
while (i<3):
  turn_left()
  i += 1
i = 0
while (i < 2): # forward 3
  i += 1
  move()
'''
#---- end robot movement 

wn.mainloop()
