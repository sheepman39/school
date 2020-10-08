# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
dot_color = "#460a8f"
dot_size = 5
dot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
dot = trtl.Turtle()
dot.fillcolor(dot_color)
dot.turtlesize(dot_size)
dot.shape(dot_shape)
dot.penup()

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(50,-150)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,-150)

#-----game functions--------
def spot_clicked(x, y):
  global timer_up
  if(timer_up):
    dot.goto(0,0)
    dot.hideturtle()
    #game_setup()
  else:
    dot.goto(x,y)
    change_position()
    update_score()

def game_setup(x,y):
  global dot_color
  global dot_size
  global dot_shape
  global score
  global font_setup
  global timer
  global counter_interval
  global timer_up
  if(timer_up == True):
    dot_color = "#460a8f"
    dot_size = 5
    dot_shape = "circle"
    score = 0
    font_setup = ("Arial", 20, "normal")
    timer = 30
    counter_interval = 1000  
    timer_up = False
    counter.write("Timer: " + str(timer), font=font_setup)
    counter.getscreen().ontimer(countdown, counter_interval) 
  else:
    spot_clicked(x,y)

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write("score: " + str(score), font = font_setup)
  
def change_position():
  global score
  global dot_size
  if(score % 2 == 0 and dot_size >= 1):
    dot_size -= 0.25
    dot.turtlesize(dot_size)
  new_xcor = rand.randint(-200,200)
  new_ycor = rand.randint(-150,150)
  dot.goto(new_xcor,new_ycor)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    #print("Click on the turtle to play again!")
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
dot.onclick(game_setup)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("#5ca5ff") 
wn.mainloop()
