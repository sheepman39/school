# Final project by
# Tyler Stadt
# Thomas Armstrong
# John Salata

# we are making a dueling game
# done: 
# make two turtles that can move using wasd and ijkl
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
import math

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

# variables
speed = 10
circles = list()


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
player2.shape("square")
player2.turtlesize(3)
player2.color("green")
player2.penup()
player2.goto(200,0)
player2.health = 20

# projectiles
class Projectile():
  speed = 10

  def __init__(self, player):
    self.x = player.xcor()
    self.y = player.ycor()
    self.turtle = trtl.Turtle()
    self.turtle.penup()
    self.turtle.shape("circle")
    self.turtle.color(player.fillcolor())
    self.direction = player.heading()
    self.life = 20000
    circles.append(self)
  def move(self,t):
    self.life, dist = self.life - t, Projectile.speed * t
    self.x, self.y = self.x + dist * math.cos(self.direction), self.y + dist * math.sin(self.direction)


  pass
# functions
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
      player2.goto(player2.xcor(),player2.ycor()+speed)
    elif(key == "k" and player2.ycor() > -200):
      player2.goto(player2.xcor(),player2.ycor()-speed)

def animate():
  for b in circles:
    
    b.move(1/5)
    b.draw()
    if len(circles) > 0:
        if circles[0].life < 0:
            circles.pop(0)
  wn.ontimer(animate, 50)
    
for k in "wasdilkj":
    
  wn.onkeypress(functools.partial(move_player, k),key = k)
  
  wn.onkeypress(functools.partial(Projectile,player1),key = 'q')
  #circles.append(c)
  animate()
  wn.listen()



wn.mainloop()