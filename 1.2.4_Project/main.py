# 1.2.4_Project with the mazes
import turtle as trtl 

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

# maze creator
for i in range(num_walls):

  # Controls doors and walls
  # ignores the first 6 walls drawn
  if(i>=6):
    
    #draws the windows
    maze_painter.left(90)
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(distance)
    maze_painter.pendown()
    
    #Draws the barriers
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(distance*2)
    maze_painter.back(distance*2)
    maze_painter.right(90)
    maze_painter.forward(-40+i*distance)

  else:
    
    # draws the first 6 walls
    maze_painter.left(90)
    maze_painter.forward(20+i*distance)
  

wn.mainloop()