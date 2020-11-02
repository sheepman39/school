# 1.2.4_Project with the mazes
import turtle as trtl 
import random as rand

# Screen setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# config variables
num_walls = 25
distance = 15
wall_color = "#007502"

# maze drawer setup
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.color(wall_color)
maze_painter.ht()

# maze runner
maze_run = trtl.Turtle()

# door and barrier creator
def door_creator(door):
  
  maze_painter.left(90)
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

# maze creator
for i in range(num_walls):

  # Controls doors and walls
  # ignores the first 6 walls drawn
  wall_len = 30+i*distance

  if(i>=6):
    
    door = rand.randint(distance*2, (wall_len - distance*2))
    barrier = rand.randint(distance*2, (wall_len - distance*2))
    while abs(door - barrier) < distance:
      door = rand.randint(distance*2, (wall_len - distance*2))
    
    if(door < barrier):

      # draws the door first
      door_creator(door)

      # draws the barriers
      bar(barrier - (distance*2+door))

      # draws the rest of the wall
      maze_painter.forward(wall_len-barrier)

    else:

      # draws the barrier first
      bar(barrier)

      # draws the doors
      door_creator(door-barrier)
      
      # finishes up the rest of the wall
      maze_painter.forward(wall_len - door - distance*2)

  else:
    
    # draws the first 6 walls
    maze_painter.left(90)
    maze_painter.forward(20+i*distance)


wn.mainloop()




# snek easter egg
# hello there
# \/\/\/\/\/\/\/\/\/\/\/\/\/\/[}=>