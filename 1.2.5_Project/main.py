#    a.113---main.py---Shall we play a game?

#import statements
import turtle as trtl 
import random as rand
import functools
import leaderboard as lb
# idea: falling trashtrash that click
# you get a score
# steal code from 1.2.2 with the leaderboard
# I have some javascript code we can convert for this
# timer?
# Idea: add different color trash that you don't click on
#https://wwwkhanacademy.org/computer-programming/snow-fall/6097804743835648

# === variables ===
trash = []
trashcan = "./1.2.5_Project/trashcan.gif"
font_setup = ("Arial", 20, "normal")
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(trashcan) 
point = 0
rounds = 0
lives = 3

# === leaderboard variables ===
leaderboard_file_name = "./1.2.5_Project/1.2.5_Leaderboard.txt"
leader_names_list = []
leader_scores_list = []
try:
  player_name = wn.textinput("Greetings Player...","Identify yourself:")
  print(player_name)
except:
  player_name = "Unknown"

# === bucket turtle ===
bucket = trtl.Turtle()
bucket.turtlesize(1)
bucket.color("black")
bucket.penup()
bucket.shape(trashcan)
bucket.goto(0,-250)

# === functions ===
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global leader_scores_list
  global leader_names_list
  global point
  global bucket

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list,leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or point > leader_scores_list[4]):
      lb.update_leaderboard(leaderboard_file_name,leader_names_list,leader_scores_list, player_name, point)
      lb.draw_leaderboard(leader_names_list, leader_scores_list, True, bucket,point)

  else:
      lb.draw_leaderboard(leader_names_list,leader_scores_list, False, bucket,point)

# creates the items of trash
def trash_creator(x):
  global trash
  for i in range(x):
    tmp_turtle = trtl.Turtle()
    tmp_turtle.penup()
    tmp_turtle.turtlesize(rand.uniform(0.5,3))
    tmp_turtle.speed(-1+i*0)
    tmp_turtle.goto(rand.randint(-200,200),rand.randint(50,300))
    tmp_turtle.speed(rand.uniform(0.5,5))
    trash.append(tmp_turtle)
    

# moves the trash can
def move(direction):
  if(str(direction) == "left"):
    bucket.goto(bucket.xcor()-7,bucket.ycor())
  elif(str(direction) == 'right'):
    bucket.goto(bucket.xcor()+7,bucket.ycor())



# tells the turtles to fall
def game_start():
  global point
  global lives 
  global rounds

  for i in range(len(trash)):

    if(lives <= 0):
      print("Game Over")
      break

    while(trash[i].isvisible()):

      # adds functionality to move trash can
      wn.onkeypress(functools.partial(move,"left"),"a")
      wn.onkeypress(functools.partial(move,"left"), "Left")
      wn.onkeypress(functools.partial(move,"right"),"d")
      wn.onkeypress(functools.partial(move,"right"),"Right")
      wn.listen()


      if(abs(trash[i].xcor()-bucket.xcor()) < 25 and trash[i].ycor() <= -200):
        
        trash[i].ht()
        point += 1
        print(point)
      
      elif(trash[i].ycor() <= -320):
      
        trash[i].ht()
        lives -= 1
        print("Lost a life")
        print(str(lives) + " lives remaining")

      trash[i].goto(trash[i].xcor(),trash[i].ycor()-1)
  
  #manage_leaderboard()
  

# summons 10 test dummies
while(lives>0):
  trash_creator(10+lives*5)
  game_start()

if(lives <= 0):
  manage_leaderboard()

# TODO: make multiple fall + random location
# TODO: implement leaderboard code from previous projects
# TODO: Add different colored trashtrash
# TODO: add easter eggs 
#/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/[}--<
wn.listen()
wn.mainloop()