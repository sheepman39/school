#    a.113---main.py---Shall we play a game?

#import statements
import turtle as trtl 
import random as rand
import functools
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
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(trashcan) 

# === bucket turtle ===
bucket = trtl.Turtle()
bucket.turtlesize(1)
bucket.color("white")
bucket.penup()
bucket.shape(trashcan)
bucket.goto(0,-250)

# creates the items of trash
def trash_creator(x):
  for i in range(x):
    tmp_turtle = trtl.Turtle()
    tmp_turtle.penup()
    tmp_turtle.turtlesize(rand.uniform(0.5,3))
    tmp_turtle.speed(-1)
    tmp_turtle.goto(rand.randint(-200,200),rand.randint(50,300))
    tmp_turtle.speed(rand.uniform(0.5,5))
    trash.append(tmp_turtle)
    

# moves the trash can
def move(direction):
  if(str(direction) == "left"):
    bucket.goto(bucket.xcor()-5,bucket.ycor())
  elif(str(direction) == 'right'):
    bucket.goto(bucket.xcor()+5,bucket.ycor())
  pass

# summons 10 test dummies
trash_creator(10)
# tells the turtles to fall
for i in range(len(trash)):
  
  while(int(trash[i].ycor()) > -200):

    # adds functionality to move trash can
    wn.onkeypress(functools.partial(move,"left"),"a")
    wn.onkeypress(functools.partial(move,"left"), "Left")
    wn.onkeypress(functools.partial(move,"right"),"d")
    wn.onkeypress(functools.partial(move,"right"),"Right")
    wn.listen()
    
    # moves the trash down
    trash[i].goto(trash[i].xcor(),trash[i].ycor()-1)

# TODO: make trash fall
''''
var xPositions = [200];
var yPositions = [0];
var diameter = [10];
var speed = [1];
for(var g=0;g<200;g++){
    diameter.push(random(2,15));
    xPositions.push(random(0,width-10));
    yPositions.push(random(0, height+25));
    speed.push(random(0.5,1));
}
mouseClicked = function(){
    diameter.push(random(2,20));
    xPositions.push(random(0,width-10));
    yPositions.push(random(0, height+25));
    speed.push(random(0.5,1));
    playSound(getSound("rpg/hit-clop"));
};
draw = function() {
    frameRate(90);
  background(87, 160, 211);
   
    for (var i = 0; i < xPositions.length; i++) {
    
        noStroke();
        ellipse(xPositions[i],yPositions[i],diameter[i],diameter[i]);
        yPositions[i] += speed[i];
            if(yPositions[i]>height+25){
                yPositions[i] =-25;
        }
    }
'''
# TODO: make multiple fall + random location
# TODO: make them clickable
# TODO: make them disappear and count when clicked
# TODO: add timer

#Timer turtle
'''
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,-150)

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
'''

# TODO: implement leaderboard code from previous projects
'''
# manages the leaderboard for top 5 scorers
def manage_leaderboard():

    global leader_scores_list
    global leader_names_list
    global score
    global dot

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list,
                        leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list,
                              leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, dot,
                            score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, dot,
                            score)
'''

# TODO: Add different colored trashtrash


# TODO: add easter eggs 
#/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/[}--<
wn.listen()
wn.mainloop()

