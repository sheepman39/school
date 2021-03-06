# CS Midterm: The Duel
# Final project by
# Tyler Stadt
# Thomas Armstrong
# John Salata


# imports
import turtle as trtl
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

# projectile handling
player1_projectiles = 0
player2_projectiles = 0
max_projectiles = 6

# Center line
test1 = trtl.Turtle()
test1.ht()
test1.goto(0,100)
test1.goto(0,-100)

# player set up

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

# player 2
player2 = trtl.Turtle()
player2.shape("square")
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
player2_health.goto(150,-150)

# update health updates the health and ammo turtles at the bottom
def update_health():

  player1_health.clear()
  player2_health.clear()

  player1_health.write("Health: " + str(player1.health) + "\nRounds left: " + str(max_projectiles - player1_projectiles),font=font_setup)
  player2_health.write("Health: " + str(player2.health) + "\nRounds left: " + str(max_projectiles - player2_projectiles),font=font_setup)

  trtl.update()

# projectiles
'''
Credit to HaimingXu679 for posting some of their own
code to GitHub and including a tutorial on how to make
projectiles 
 We used them as a starting point for this chunk of code
https://github.com/HaimingXu679/Asteroids/blob/master/bullet.py 
https://pythonturtle.academy/asteroids-tutorial-bullets/
'''
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
    self.life = 30

  # move function to calculate which coordinates the projectile goes to
  # Only moves on the x-axis
  def move(self,t):
    global player2_projectiles
    global player1_projectiles

    self.life, dist = self.life - t, speed * t 
    self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)
    
    # this is all collision checking for player2
    if(abs(self.turtle.xcor()-player2.xcor()) <= 30 and abs(self.turtle.ycor() - player2.ycor()) <= 30 and self.turtle.fillcolor() == player1.fillcolor()):

      # if there is a collection, hide and clear the turtle
      self.turtle.ht()
      self.turtle.clear()

      # try block removes errors for removing
      try:

        circles.remove(self)

        # removes an active projectile from the opposing player
        player1_projectiles -= 1
        
        # removes health from player 2
        player2.health -= damage

        # updates the health bar
        update_health()
        return 

      except:

        return

    # collision checking for player1
    elif(abs(self.turtle.xcor()-player1.xcor()) <= 30 and abs(self.turtle.ycor() - player1.ycor()) <= 30 and self.turtle.fillcolor() == player2.fillcolor()):

      # this is pretty much the same code
      # as above
      self.turtle.ht()
      self.turtle.clear()

      try:

        circles.remove(self)
        player2_projectiles -= 1
        player1.health -= damage
        update_health()
        return 

      except:

        return

    else:
      # if there is no collision, move as normal
      self.turtle.goto(self.x,self.turtle.ycor())      

# functions

# just a bunch of if statements to control movement
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

    if(key == "j"):
      player2.forward(speed)
    elif(key == "l"):
      player2.forward(-speed)
    elif(key == "k"):
      player2.goto(player2.xcor(),player2.ycor()-speed)
    elif(key == "i"):
      player2.goto(player2.xcor(),player2.ycor()+speed)

# life check function check if either player
# has no health and ends the game
def life_check():
      
  if(player1.health <= 0):
    
    # hides the turtles and shows a popup
    player1.ht()
    player2.ht()
    wn.textinput("Game Over","Congrats Player 2 Wins!\nPress cancel to stop playing!")
    
    try:
      
      # if a button is hit, close the game
      #This causes an error. safe to ignore
      wn.bye()
    
    except:
    
      pass

  elif(player2.health <= 0):

    player1.ht()
    player2.ht()
    wn.textinput("Game Over!","Congrats Player 1 Wins!\nPress cancel to stop playing!")
    
    try:
    
      wn.bye()
    
    except:
    
      pass

# this function animates all projectiles at once
def animate():

  global player1_projectiles
  global player2_projectiles

  # circles list stores the projectiles
  for b in circles:
    
    # they move a certain bit
    Projectile.move(b,1/20 * len(circles))

    if b in circles:

      if len(circles) > 0:

        # if the life is less than 0, remove it
        if b.life < 0:
          
          b.turtle.ht()
          
          try:
          
            circles.remove(b)
          
          except:
          
            pass
          
          # if the turtle is from a player and is 
          # removed, remove one current projectile
          if b.turtle.fillcolor() == player1.fillcolor():

            player1_projectiles -= 1
            update_health()
          
          elif b.turtle.fillcolor() == player2.fillcolor():

            player2_projectiles -= 1
            update_health
    
  # trtl.update() moves everything at once
  # may produce error on vs code. ignore
  trtl.update()

  # if the player health is low, check it
  if(player1.health < 10 or player2.health < 10):
    
    life_check()
  
  # on timer repeats this function for smoothness
  wn.ontimer(animate, 5)


# creates new projectile tied to a player
def new_projectile(player):
  global circles
  global player1_projectiles
  global player2_projectiles
  
  # checks if the plyaer is allowed to spawn
  # another Projectile
  if(player.fillcolor() == player1.fillcolor() and player1_projectiles < max_projectiles):
    
    player1_projectiles += 1
    update_health()
    circles.append(Projectile(player))
  
  elif(player.fillcolor() == player2.fillcolor() and player2_projectiles < max_projectiles):

    player2_projectiles += 1
    update_health()
    circles.append(Projectile(player))


update_health()

# primary loop that listens for key presses
# and controls which direction players move in
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