# Final project by
# Tyler Stadt
# Thomas Armstrong
# John Salata

# we are making a dueling game
# done: 
# make two turtles that can move using wasd and arrow keys
# TODO:
# make the turtles able to fire projectiles 
# make the opposite player able to be hit
# make a scoreboard for when a player gets hit
# insert player names
# change turtle colors
# fix bugs
# possible upgrades?
# make some obstacles to hide behind
# different blaster models
import turtle as trtl
import random as rand
import functools 

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# variables
speed = 10

# player 1
player1 = trtl.Turtle()
player1.shape("circle")
player1.turtlesize(3)
player1.color("blue")
player1.penup()
player1.goto(-200,0)
player1.health = 20

# player 2
player2 = trtl.Turtle()
player2.shape("circle")
player2.turtlesize(3)
player2.color("green")
player2.penup()
player2.goto(200,0)
player2.health = 20

# functions
def move_player(key):
  if(key == "w" or key == "a" or key == "s" or key == "d"):
    if(key == "d"):
      player1.forward(speed)
    elif(key == "a"):
      player1.forward(-speed)
    elif(key == "w"):
        player1.goto(player1.xcor(),player1.ycor()+speed)
    elif(key == "s"):
      player1.goto(player1.xcor(),player1.ycor()-speed)

  elif(key == "i" or key == "k" or key == "l" or key == "j"):
    if(key == "l"):
      player2.forward(speed)
    elif(key == "j"):
      player2.forward(-speed)
    elif(key == "i"):
      player2.goto(player2.xcor(),player2.ycor()+speed)
    elif(key == "k"):
      player2.goto(player2.xcor(),player2.ycor()-speed)

for k in "wasdilkj":
  
  wn.onkeypress(functools.partial(move_player, k),key = k)
  wn.listen()


wn.mainloop()