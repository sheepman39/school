# 1.2.4_Project with the mazes
import turtle as trtl 

# Screen setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# config variables
num_walls = 25
distance = 20
wall_color = "#4a1a9c"

# maze drawer setup
maze_painter = trtl.Turtle()
maze_painter.pensize(5)
maze_painter.color(wall_color)

# maze creator
for i in range(num_walls):

  maze_painter.left(90)
  maze_painter.forward(20+i*distance)

wn.mainloop()