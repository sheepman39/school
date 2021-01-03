import pygame, random, sys

# this is based off of a tutorial from https://www.youtube.com/watch?v=Qf3-aDXG8q4

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

ball_speed = [7 * random.choice((1,-1)), 7 * random.choice((1,-1))]
player_speed = 0
opponent_speed = 7

def ball_animation():
  
  global ball_speed, player_score, opponent_score, score_time
  
  # changes ball speed
  ball.x += ball_speed[0]
  ball.y += ball_speed[1]

  ball_speed = list(ball_speed)
  # this changes the direction upon collision
  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed[1] = ball_speed[1] * -1
  
  if ball.left <= 0:
    player_score += 1
    score_time = pygame.time.get_ticks()

  elif ball.right >= screen_width:
    opponent_score += 1
    score_time = pygame.time.get_ticks()


  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed[0] = ball_speed[0] * -1

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
  global ball_speed, score_time

  ball.center = (screen_width/2, screen_height/2)

  current_time = pygame.time.get_ticks()

  if current_time - score_time < 700:
  
    number_three = game_font.render("3", True, light_grey)
    screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
  
  elif 700 < current_time - score_time < 1400:
  
    number_two = game_font.render("2", True, light_grey)
    screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
  
  elif 1400 < current_time - score_time < 2100:
  
    number_one = game_font.render("1", True, light_grey)
    screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

  if current_time - score_time < 2100:
  
    ball_speed = [0, 0]
  
  else:
  
    ball_speed = (7 * random.choice((1,-1)), 7 * random.choice((1,-1)))
    score_time = None

# score variables
player_score = 0
opponent_score = 0

# text variables
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Score timer
score_time = True

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

  if score_time:
    ball_restart()

  # draws the score
  player_text = game_font.render(f"{player_score}", True, light_grey)
  screen.blit(player_text, (660, 470))
  
  opponent_text = game_font.render(f"{opponent_score}", True, light_grey)
  screen.blit(opponent_text, (600, 470))

  # .flip draws the picture from everything in the loop
  pygame.display.flip()

  # this limits how fast the loop runs, 60 hz
  clock.tick(60)
