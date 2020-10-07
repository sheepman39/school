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

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
dot = trtl.Turtle()
dot.fillcolor(dot_color)
#dot.size(2)
dot.shape(dot_shape)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(50,-150)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,-150)

#-----game functions--------
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write("score: " + str(score), font = font_setup)
  
def spot_clicked(x, y):
  global timer_up
  if(timer_up):
    dot.hideturtle()
  else:
    dot.goto(x,y)
    change_position()
    update_score()

def change_position():
  new_xcor = rand.randint(-200,200)
  new_ycor = rand.randint(-150,150)
  print(new_xcor)
  print(new_ycor)
  dot.goto(new_xcor,new_ycor)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
dot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
