# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
dot_color = "#460a8f"
dot_size = 2
dot_shape = "circle"
score = 0

#-----initialize turtle-----
dot = trtl.Turtle()
dot.fillcolor(dot_color)

#dot.size(2)
dot.shape(dot_shape)

#-----game functions--------
def spot_clicked(x, y):
  dot.goto(x,y)
  print("here")

def change_position(x,y):
  print("here")
  new_xcor = rand.randint(-200,200)
  new_ycor = rand.randint(-150,150)
  print(new_xcor)
  print(new_ycor)
  dot.goto(new_xcor,new_ycor)

#-----events----------------
dot.onclick(change_position)
wn = trtl.Screen()
wn.mainloop()
