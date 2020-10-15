# a121_catch_a_turtle.py
#NOTE: copy and pasted code from 1.2.1 and im going
#to continue working on this to keep the two separate
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

# leaderboard variables
leaderboard_file_name = "1.2.2_Project/a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name:")

#-----game configuration----
dot_color = "#460a8f"
dot_size = 5
dot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000
timer_up = False

#-----initialize turtle-----
#Purple turtle
dot = trtl.Turtle()
dot.fillcolor(dot_color)
dot.turtlesize(dot_size)
dot.shape(dot_shape)
dot.penup()

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

#Score turtle
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(50,-150)

#Timer turtle
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,-150)

#-----game functions--------
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global dot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, dot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, dot, score)

#Controls the initial click
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

#Resets the game to make it playable
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
    counter.clear()
    counter.write("Timer: " + str(timer), font=font_setup)
    counter.getscreen().ontimer(countdown, counter_interval) 
    dot_color = "#460a8f"
    dot_size = 5
    dot_shape = "circle"
    score = 0
    timer = 20
    font_setup = ("Arial", 20, "normal")
    counter_interval = 1000  
    timer_up = False
    
  else:
    spot_clicked(x,y)

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

#Updates the score
def update_score():
  
  global score
  score += 1
  score_writer.clear()
  score_writer.write("score: " + str(score), font = font_setup)

#Moves turtle to a random position  
def change_position():
  
  global score
  global dot_size
  if(score % 2 == 0 and dot_size >= 1):
  
    dot_size -= 0.25
    dot.turtlesize(dot_size)
  
  new_xcor = rand.randint(-200,200)
  new_ycor = rand.randint(-100,150)
  dot.goto(new_xcor,new_ycor)

#Timer code
def countdown():
  
  global timer, timer_up
  counter.clear()
  if (timer <= 0):
  
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    dot.goto(0,0)
    dot.turtlesize(5)
    print("Click on the turtle to play again!")

#This Program was created/edited by sheepman39
#In case of plagarism, please go to https://github.com/sheepman39/school
#And submit an issue

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