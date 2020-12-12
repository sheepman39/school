# Final project by
# Tyler Stadt
# Thomas Armstrong
# John Salata

# we are making a dueling game
# done: 
# make two turtles that can move using wasd and ijkl
# make the turtles able to fire projectiles
# TODO:
# make the opposite player able to be hit
# make a scoreboard for when a player gets hit
# insert player names
# change turtle colors
# fix bugs
# possible upgrades?
# make some obstacles to hide behind
# different blaster models

# imports
import turtle as trtl
import random as rand
import functools 
import math

# screen setup
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# variables
speed = 10
circles = list()

# test turtle
test1 = trtl.Turtle()
test1.goto(0,100)
test1.goto(0,-100)

# player 1
player1 = trtl.Turtle()
player1.shape("square")
player1.turtlesize(3)
player1.color("blue")
player1.penup()
player1.goto(-200,0)
player1.health = 20

# player 2
player2 = trtl.Turtle()
player2.shape("arrow")
player2.turtlesize(3)
player2.color("green")
player2.penup()
player2.setheading(180)
player2.goto(200,0)
player2.health = 20

# projectiles
class Projectile():
  speed = 20

  # __init__ function starts the creation of a new Projectile object
  # it sets the needed attributes of the projectiles
  def __init__(self, player):
    
    self.x = player.xcor()
    self.y = player.ycor()
    self.turtle = trtl.Turtle()
    self.turtle.penup()
    self.turtle.goto(self.x,self.y)
    self.turtle.shape("circle")
    self.turtle.color(player.fillcolor())
    self.direction = player.heading()
    self.turtle.setheading(player.heading())
    self.life = 50

  # move function to calculate which coordinates
  # the projectile goes to
  # Only moves on the x-axis
  def move(self,t):

    self.life, dist = self.life - t, Projectile.speed * t 
    self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)
    self.turtle.goto(self.x,self.turtle.ycor())


# functions

# just a bunch of if statements to control movement
def move_player(key):
  if(key == "w" or key == "a" or key == "s" or key == "d"):

    if(key == "d" and player1.xcor() < 300):
      player1.forward(speed)
    elif(key == "a" and player1.xcor() > -300):
      player1.forward(-speed)
    elif(key == "w" and player1.ycor() < 200):
        player1.goto(player1.xcor(),player1.ycor()+speed)
    elif(key == "s" and player1.ycor() > -200):
      player1.goto(player1.xcor(),player1.ycor()-speed)

  elif(key == "i" or key == "k" or key == "l" or key == "j"):

    if(key == "l" and player2.xcor() < 300):
      player2.forward(speed)
    elif(key == "j" and player2.xcor() > -300):
      player2.forward(-speed)
    elif(key == "i" and player2.ycor() < 200):
      player2.goto(player2.xcor(),player2.ycor()-speed)
    elif(key == "k" and player2.ycor() > -200):
      player2.goto(player2.xcor(),player2.ycor()+speed)

# this function animates all projectiles at once
def animate():

  # circles list stores the projectiles
  for b in circles:
    
    # they move a certain bit
    Projectile.move(b,1/20)
    if len(circles) > 0:
      # if the life is less than 0, remove it
      if b.life < 0:
        circles.pop(0)
  # trtl.update() moves everything at once
  # may produce error on vs code. ignore
  trtl.update()
  wn.ontimer(animate, 5)

# creates new projectile tied to a player
def new_projectile(player):
  c = Projectile(player)
  circles.append(c)

for k in "wasdilkj":
    
  # controls movement of both players
  wn.onkeypress(functools.partial(move_player, k),key = k)
  
  # Listens for a projectile for player 1 and 2
  wn.onkeypress(functools.partial(new_projectile,player1),key = 'q')
  wn.onkeypress(functools.partial(new_projectile,player2),key = "o")
  
  # animate function moves projectiles
  animate()

  # needed to listen for keypresses
  wn.listen()

wn.mainloop()