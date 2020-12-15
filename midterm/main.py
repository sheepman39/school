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
wn.bgpic("midterm/background.gif")

# variables
speed = 30
damage = 10
circles = list()
font_setup = ("Arial", 20, "bold")

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
player1.health = 100

# player 1 health
player1_health = trtl.Turtle()
player1_health.ht()
player1_health.penup()
player1_health.color("blue")
player1_health.goto(-200,-150)
player1_health.write("Health: " + str(player1.health),font=font_setup)

# player 2
player2 = trtl.Turtle()
player2.shape("arrow")
player2.turtlesize(3)
player2.color("green")
player2.penup()
player2.setheading(180)
player2.goto(200,0)
player2.health = 100

# player 2 health
player2_health = trtl.Turtle()
player2_health.ht()
player2_health.penup()
player2_health.color("green")
player2_health.goto(200,-150)
player2_health.write("Health: " + str(player2.health),font=font_setup)

# projectiles
class Projectile():
  global speed
  global circles

  # __init__ function starts the creation of a new Projectile object
  # it sets the needed attributes of the projectiles
  def __init__(self, player):
    
    self.x = player.xcor()
    self.y = player.ycor()
    self.turtle = trtl.Turtle()
    self.turtle.speed(-1)
    self.turtle.penup()
    self.turtle.goto(self.x,self.y)
    self.turtle.shape("circle")
    self.turtle.color(player.fillcolor())
    self.direction = player.heading()
    self.turtle.setheading(player.heading())
    self.life = 20


  # move function to calculate which coordinates
  # the projectile goes to
  # Only moves on the x-axis
  def move(self,t):

    self.life, dist = self.life - t, speed * t 
    self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)
    
    if(abs(self.turtle.xcor()-player2.xcor()) < 20 and abs(self.turtle.ycor() - player2.ycor()) < 20 and self.turtle.fillcolor() == player1.fillcolor()):

      self.turtle.ht()
      self.turtle.clear()

      #try:
      circles.remove(self)
      player2_health.clear()
      player2.health -= damage
      player2_health.write("Health: " + str(player2.health),font=font_setup)
      print("Hit player 2")
      return 
      #except:
      #  print("error 119")
      #  return 

    elif(abs(self.turtle.xcor()-player1.xcor()) < 20 and abs(self.turtle.ycor() - player1.ycor()) < 20 and self.turtle.fillcolor() == player2.fillcolor()):

      self.turtle.ht()
      self.turtle.clear()

      #try:
      circles.remove(self)
      player1_health.clear()
      player1.health -= damage
      player1_health.write("Health: " + str(player1.health),font=font_setup)
      print("hit player 1")
      return 
      #except:
      #  print("error 136")
      #  return 

    else:
      self.turtle.goto(self.x,self.turtle.ycor())      


# functions

# just a bunch of if statements to control movement
def move_player(key):
  if(key == "w" or key == "a" or key == "s" or key == "d"):

    if(key == "d" and abs(player1.xcor()) < 300):
      player1.forward(speed)
    elif(key == "a" and abs(player1.xcor()) < 300):
      player1.forward(-speed)
    elif(key == "w" and abs(player1.ycor()) < 200):
        player1.goto(player1.xcor(),player1.ycor()+speed)
    elif(key == "s" and abs(player1.ycor()) < 200):
      player1.goto(player1.xcor(),player1.ycor()-speed)

  elif(key == "i" or key == "k" or key == "l" or key == "j"):

    if(key == "j" and abs(player2.xcor()) < 300):
      player2.forward(speed)
    elif(key == "l" and abs(player2.xcor()) < 300):
      player2.forward(-speed)
    elif(key == "k" and abs(player2.ycor()) < 200):
      player2.goto(player2.xcor(),player2.ycor()-speed)
    elif(key == "i" and abs(player2.ycor()) < 200):
      player2.goto(player2.xcor(),player2.ycor()+speed)

# this function animates all projectiles at once
def animate():

  # circles list stores the projectiles
  for b in circles:
    
    # they move a certain bit
    Projectile.move(b,1/20)
    
    if b in circles:
      if len(circles) > 0:

        # if the life is less than 0, remove it
        if b.life < 0:
          b.turtle.ht()
          circles.remove(b)
    
  # trtl.update() moves everything at once
  # may produce error on vs code. ignore
  #trtl.update()
  wn.ontimer(animate, 60)


# creates new projectile tied to a player
def new_projectile(player):
  global circles

  c = Projectile(player)
  circles.append(c)

animate()

for k in "wasdilkj":
  
  # controls movement of both players
  wn.onkeypress(functools.partial(move_player, k),key = k)
  
  # Listens for a projectile for player 1 and 2
  wn.onkeypress(functools.partial(new_projectile,player1),key = 'q')
  wn.onkeypress(functools.partial(new_projectile,player2),key = "o")
  
  # animate function moves projectiles
  # circles list stores the projectiles


  # needed to listen for keypresses
  wn.listen()
  
wn.mainloop()