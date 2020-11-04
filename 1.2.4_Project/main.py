# 1.2.4_Project with the mazes
import turtle as trtl 
import random as rand
import functools 

# Screen setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# config variables
num_walls = 35
distance = 20
wall_color = "#007502"

# maze drawer setup
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.color(wall_color)
maze_painter.ht()
maze_painter.speed(-1)

# maze runner
maze_runner = trtl.Turtle()
maze_runner.shape("arrow")
maze_runner.color("#1FF1E5")
maze_runner.penup()
maze_runner.goto(-15,0)
maze_runner.pendown()

# door and barrier creator
def door_creator(door):
  
  
  maze_painter.forward(door)
  maze_painter.penup()
  maze_painter.forward(distance*2)
  maze_painter.pendown()

def bar(barrier):
  maze_painter.forward(barrier)
  maze_painter.left(90)
  maze_painter.forward(distance*2)
  maze_painter.back(distance*2)
  maze_painter.right(90)

def go_up():
  maze_runner.setheading(90)

def go_right():
  maze_runner.setheading(0)

def go_left():
  maze_runner.setheading(180)

def go_down():
  maze_runner.setheading(270)

def move_runner(amount):
  maze_runner.forward(amount)

# maze creator
for i in range(num_walls):

  # Controls doors and walls
  # ignores the first 6 walls drawn
  wall_len = 30+i*distance

  if(i>4):
    
    door = rand.randint(distance*2, (wall_len - distance*2))
    barrier = rand.randint(distance*2, (wall_len - distance*2))
    while abs(door - barrier) < distance:
      door = rand.randint(distance*2, (wall_len - distance*2))
    
    if(door < barrier):

      # draws the door first
      maze_painter.left(90)
      door_creator(door)

      # draws the barriers
      bar(barrier - (distance*2+door))

      # draws the rest of the wall
      maze_painter.forward(wall_len-barrier)

    else:

      # draws the barrier first
      maze_painter.left(90)
      bar(barrier)

      # draws the doors
      door_creator(door-barrier)
      
      # finishes up the rest of the wall
      maze_painter.forward(wall_len - door - distance*2)

  else:
    
    # draws the first 6 walls
    maze_painter.left(90)
    maze_painter.forward(20+i*distance)

wn.onkeypress(go_down,"Down")
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(functools.partial(move_runner,10)," ")
wn.listen()
wn.mainloop()




# snek easter egg
# hello there
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/[}=>