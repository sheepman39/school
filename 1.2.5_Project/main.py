#    a.113---main.py---Shall we play a game?

#import statements
import turtle as trtl 
import random as rand
import functools
import leaderboard as lb

# === variables ===
point = 0
rounds = 0
lives = 3
player_speed = 14

trash = []
trash_img = ["./1.2.5_Project/bad_apple.gif","./1.2.5_Project/banana.gif","./1.2.5_Project/garbage-bag.gif","./1.2.5_Project/paper_ball.gif"]
trashcan = "./1.2.5_Project/trashcan.gif"
tipped_trash = "./1.2.5_Project/tippedovercan.gif"
font_setup = ("Arial", 20, "bold")
a_surprise_for_later = "./1.2.5_Project/angry_raccoon.gif"

# screen setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("./1.2.5_Project/garbage-truck.gif")

# adds each of the trash images into the program
for i in trash_img:
  wn.addshape(i)

wn.addshape(trashcan) 
wn.addshape(tipped_trash)
wn.addshape(a_surprise_for_later)

# === leaderboard variables ===
leaderboard_file_name = "./1.2.5_Project/1.2.5_Leaderboard.txt"
leader_names_list = []
leader_scores_list = []


# === bucket turtle ===
bucket = trtl.Turtle()
bucket.turtlesize(1)
bucket.color("#1bb300")
bucket.penup()
bucket.shape(trashcan)
bucket.goto(0,-250)

# === anouncer turtle ===
scoreboard = trtl.Turtle()
scoreboard.penup()
scoreboard.color("#1bb300")
scoreboard.goto(-350,-250)
scoreboard.ht()

# easter egg number 1
#           {Hi Mr. Joyce}
#        o /
#       /|\
#       / \
# === inital setup ===
try:
  player_name = wn.textinput("Greetings Player...","I'm gonna need your name player. Player isn' exactly a name...:")
except:
  player_name = "Unknown"

# === functions ===

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global leader_scores_list
  global leader_names_list
  global point
  global bucket

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list,leader_scores_list)

  # controls writing to the leaderboard
  if (len(leader_scores_list) < 5 or point > leader_scores_list[4]):
      lb.update_leaderboard(leaderboard_file_name,leader_names_list,leader_scores_list, player_name, point)
      lb.draw_leaderboard(leader_names_list, leader_scores_list, True, bucket,point)

  else:
      lb.draw_leaderboard(leader_names_list,leader_scores_list, False, bucket,point)

# creates the items of trash
def trash_creator(x):
  global trash

  # creates x amount of turtles
  for i in range(x):
    tmp_turtle = trtl.Turtle()
    
    print(rounds)
    # every 6th round the trash is an angry racoon. Why? Raccoons. No other reason besides raccoons
    if(rounds % 5 == 0 and rounds >= 5):
      
        tmp_turtle.shape(a_surprise_for_later)
    
    else:
    
      # sets the shape to a random image
      tmp_turtle.shape(trash_img[rand.randint(0,len(trash_img)-1)])

    tmp_turtle.penup()
    tmp_turtle.turtlesize(rand.uniform(0.5,3))
    tmp_turtle.speed(-1+i*0)
    tmp_turtle.goto(rand.randint(-200,200),300)
    tmp_turtle.speed(rand.uniform(0.5+rounds*0.1,3+rounds*0.2))
    trash.append(tmp_turtle)
    

# moves the trash can
def move(direction):
  if(str(direction) == "left"):
    bucket.goto(bucket.xcor()-player_speed,bucket.ycor())
  elif(str(direction) == 'right'):
    bucket.goto(bucket.xcor()+player_speed,bucket.ycor())

# tells the turtles to fall and control mosts of the game
def game_start():
  global point
  global lives 
  global rounds
  global lives

  # repeats this for each peice of trash
  for i in range(len(trash)):

    # if lives are 0, game is over and break out of loop
    if(lives <= 0):
      break

    # updates the scoreboard on the left
    scoreboard.clear()
    scoreboard.write("Score: " + str(point) + "\nRound: " + str(rounds) + "\nLives: "  + str(lives),font=font_setup)

    # repeats this for trash reamining
    while(trash[i].isvisible()):

      # Listnes for the arrow or a and d keys to move
      wn.onkeypress(functools.partial(move,"left"),"a")
      wn.onkeypress(functools.partial(move,"left"), "Left")
      wn.onkeypress(functools.partial(move,"right"),"d")
      wn.onkeypress(functools.partial(move,"right"),"Right")
      wn.listen()

      # collision checker
      if(abs(trash[i].xcor()-bucket.xcor()) < 25 and trash[i].ycor() <= -200):
        
        trash[i].ht()
        point += 1

      # if the trash is below this point, lose a life
      elif(trash[i].ycor() <= -320):
      
        trash[i].ht()
        lives -= 1

      # moves the trash down
      trash[i].goto(trash[i].xcor(),trash[i].ycor()- float(trash[i].speed()))

#easter egg number 2
#          -
#        /   \
#       |     |
#        \   /
#          - 
#         ---
#        /~~~\
#        |===|
#        \~~~/
#         ---

# While you still have lives,
# run the game
while(lives>0):
  
  # summons more trash per round
  trash_creator(10 + rounds*2)
  rounds += 1

  # bonus life if you live for 5 rounds
  if(rounds % 5 == 0):
    lives += 1

  # starts the game
  game_start()

# if the lives are less than zero
if(lives <= 0):
  
  # hide any extra trash
  for i in trash:
    i.ht()

  # manage the leaderboard
  manage_leaderboard()

  # displays fallen trash bin
  bucket.goto(0,-180)
  bucket.st()
  bucket.shape(tipped_trash)

# TODO: add easter eggs 
#easter egg number 3
#/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/[}--<
wn.listen()
wn.mainloop()