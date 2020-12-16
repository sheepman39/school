# Final project by
# Tyler Stadt
# Thomas Armstrong
# John Salata

# ITS TIME TO D-D-D-DUEL

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

player1_projectiles = 0
player2_projectiles = 0
max_projectiles = 5

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


def update_health():

  player1_health.clear()
  player2_health.clear()

  player1_health.write("Health: " + str(player1.health) + "\nRounds left: " + str(max_projectiles - player1_projectiles),font=font_setup)
  player2_health.write("Health: " + str(player2.health) + "\nRounds left: " + str(max_projectiles - player2_projectiles),font=font_setup)

  trtl.update()

def game_restart():

  player1_health.clear()
  player2_health.clear()

  for c in circles:
    c.turtle.ht()
    try:
      circles.remove(c)
    except:
      pass
  
  player1.goto(-150, 0)
  player2.goto(150, 0)
  
  player1.st()
  player2.st()
  
  player1.health = 100
  player2.health = 100
  
  update_health()

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
    self.life = 30


  # move function to calculate which coordinates
  # the projectile goes to
  # Only moves on the x-axis
  def move(self,t):
    global player2_projectiles
    global player1_projectiles

    self.life, dist = self.life - t, speed * t 
    self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)
    
    if(abs(self.turtle.xcor()-player2.xcor()) <= 25 and abs(self.turtle.ycor() - player2.ycor()) <= 25 and self.turtle.fillcolor() == player1.fillcolor()):

      self.turtle.ht()
      self.turtle.clear()

      try:
        circles.remove(self)
        player1_projectiles -= 1
        player2.health -= damage
        update_health()
        return 
      except:
        return

    elif(abs(self.turtle.xcor()-player1.xcor()) <= 25 and abs(self.turtle.ycor() - player1.ycor()) <= 25 and self.turtle.fillcolor() == player2.fillcolor()):

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

def life_check():
      
  if(player1.health <= 0):

    player1.ht()
    player2.ht()
    continueScript = wn.textinput("Game Over","Congrats Player 2 Wins!\nPress Ok to play again or cancel to stop playing!")
    print(continueScript)
    
    if(continueScript is not None):
      
      game_restart()
    
    else:
      try:
        wn.bye()
      except:
        print("Thanks for playing!")


  elif(player2.health <= 0):

    player1.ht()
    player2.ht()
    continueScript = wn.textinput("Game Over!","Congrats Player 1 Wins!\nPress Ok to play again or cancel to stop playing!")
    print(continueScript)
    
    if(continueScript is not None):
      
      game_restart()
    
    else:
      try:
        wn.bye()
      except:
        print("Thanks for playing!")

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
          circles.remove(b)
          
          if b.turtle.fillcolor() == player1.fillcolor():

            player1_projectiles -= 1
            update_health()
          
          elif b.turtle.fillcolor() == player2.fillcolor():

            player2_projectiles -= 1
            update_health
    
  
    
  # trtl.update() moves everything at once
  # may produce error on vs code. ignore
  trtl.update()
  life_check()
  wn.ontimer(animate, 60)


# creates new projectile tied to a player
def new_projectile(player):
  global circles
  global player1_projectiles
  global player2_projectiles
  
  if(player.fillcolor() == player1.fillcolor() and player1_projectiles < max_projectiles):
    
    player1_projectiles += 1
    update_health()
    circles.append(Projectile(player))
  
  elif(player.fillcolor() == player2.fillcolor() and player2_projectiles < max_projectiles):

    player2_projectiles += 1
    update_health()
    circles.append(Projectile(player))


update_health()

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