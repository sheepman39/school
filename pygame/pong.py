import pygame, random, sys

# starts pygame
pygame.init()
clock = pygame.time.Clock()

# main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# gives the display its title
pygame.display.set_caption("Pong")

# game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# color variable
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

def ball_animation():
  
  global ball_speed_x, ball_speed_y
  
  # changes ball speed
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  # this changes the direction upon collision
  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1
  
  if ball.left <= 0 or ball.right >= screen_width:
    ball_restart()

  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1

def player_animation():

  # moving of the players
  player.y += player_speed

  # checks for boundaries
  if player.top <= 0:
    
    player.top = 0
  
  if player.bottom >= screen_height:
  
    player.bottom = screen_height

def opponent_animation():
  
 
  if opponent.top < ball.y:
  
    opponent.top += opponent_speed
  
  if opponent.bottom > ball.y:
  
    opponent.bottom -= opponent_speed

  # checks for boundaries
  if opponent.top <= 0:
    
    opponent.top = 0
  
  if opponent.bottom >= screen_height:
  
    opponent.bottom = screen_height

def ball_restart():
  global ball_speed_x, ball_speed_y
  ball.center = (screen_width/2, screen_height/2)
  ball_speed_y *= random.choice((1,-1))
  ball_speed_x *= random.choice((1,-1))

while True:
  
  # handles input
  for event in pygame.event.get():

    # checks if the event is quit
    if event.type == pygame.QUIT:

      # using both of these ensures that it is closed reliably
      pygame.quit()
      # sys exit closes the entire program
      sys.exit()
    
    if event.type == pygame.KEYDOWN:
    
      if event.key == pygame.K_DOWN:
        player_speed += 7
    
      if event.key == pygame.K_UP:
        player_speed -= 7
    
    if event.type == pygame.KEYUP:
    
      if event.key == pygame.K_DOWN:
        player_speed -= 7
    
      if event.key == pygame.K_UP:
        player_speed += 7


  ball_animation()
  player_animation()
  opponent_animation()

  # background color
  screen.fill((0,0,0))

  # draws the players and the ball
  pygame.draw.rect(screen,light_grey,player)
  pygame.draw.rect(screen,light_grey,opponent)
  pygame.draw.ellipse(screen, light_grey, ball)

  # to draw a line <screen>, <color> <x1,y1> <x2,y2>
  pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2,screen_height))

  # .flip draws the picture from everything in the loop
  pygame.display.flip()

  # this limits how fast the loop runs, 60 hz
  clock.tick(60)
