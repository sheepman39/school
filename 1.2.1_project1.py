# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
dot_color = "#460a8f"
dot_size = 2
dot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
dot = trtl.Turtle()
dot.fillcolor(dot_color)
#dot.size(2)
dot.shape(dot_shape)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(50,-150)

#-----game functions--------
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write("score: " + str(score), font = font_setup)
  
def spot_clicked(x, y):
  dot.goto(x,y)
  change_position()
  update_score()

def change_position():
  new_xcor = rand.randint(-200,200)
  new_ycor = rand.randint(-150,150)
  print(new_xcor)
  print(new_ycor)
  dot.goto(new_xcor,new_ycor)


#-----events----------------
dot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()
