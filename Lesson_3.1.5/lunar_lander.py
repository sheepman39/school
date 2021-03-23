################################################################
#   lunar_lander.py
#   The Pygame piece of this program is based on the source code
#   lunarlanderbasic.py shared on GitHub.
#   It was written for CoderDojo Leiden (http://coderdojo.nl) by 2BoysAndHats.
#   The code has been modified and extended to include the other pieces (such as TKinter, Turtle)
#################################################################
import tkinter as tk
import tkinter.messagebox as mb
import time
import pygame
import sys
import random
import gdx
import turtle as trtl
from PIL import Image, ImageTk

# define global variables
user_height_inches = 0
user_hand_inches = 0
user_injuries = 0
user_age = 0
user_handedness = ""
user_sleep_hours = 0
user_active_hours = 0
user_milk_glasses = 0
font = None
gravity = 8  # used as the sprite's original Y-axis speed
game_over = False
grips = []
average_grip = 0


##############################
# define GUI functions
##############################
def next():
  
  global user_height_inches
  global user_hand_inches
  global user_injuries
  global user_age
  global user_handedness
  
  # read the values from the textboxes
  feet = ent_feet.get()
  inches = ent_inches.get()
  hand = ent_hand_length.get()
  injuries = ent_injuries.get()
  age = ent_age.get()
  handedness = lst_handedness.curselection()
  
  # data validation
  if (feet=="" or inches==""):
    mb.showerror("Validation Error!", "Please enter a value for both feet and inches.")
  elif (hand=="" or injuries=="" or age=="" or len(handedness)==0):
    mb.showerror("Validation Error!", "Please enter a response for each question.")
  else:
    user_height_inches = int(feet) * 12 + float(inches)
    user_hand_inches = float(hand)
    user_injuries = int(injuries)
    user_age = float(age)
    if (handedness[0] == 0):  # index of the first option in the list
      user_handedness = "Right-handed"
    else:
      user_handedness = "Left-handed"
    # display the next GUI form
    frame_habits.tkraise()


def back():
  # display the previous GUI form
  frame_physiology.tkraise()


def submit_data():
  
  global user_sleep_hours
  global user_active_hours
  global user_milk_glasses
  
  # read the values from the textboxes
  sleep = ent_hours_sleep.get()
  activity = ent_hours_active.get()
  milk = ent_glasses_milk.get()

  # data validation
  if (sleep=="" or activity=="" or milk==""):
    mb.showerror("Validation Error!", "Please enter all three values.")
  else:
    user_sleep_hours = float(sleep)
    user_active_hours = float(activity)
    user_milk_glasses = float(milk)
    # display the confirmation GUI screen, then start the pygame
    frame_confirmation.tkraise()
    

# start the game when the user clicks the btn_play button
def play_game():
  btn_play.state = tk.DISABLED  # to avoid cliking this button twice, which will crash the program
  time.sleep(1)
  start_game()
  

##############################
# define sprite classes
##############################

# Lander class (extends Sprite class)
class Lander(pygame.sprite.Sprite):
    global gravity
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spacecraft.png')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = [0, gravity]
    def move(self):
        self.rect = self.rect.move(self.speed)

# Moon class (extends Sprite class)
class Moon(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('moon.png')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

# Sensor class (extends Sprite class)
class Sensor(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sensor.png')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = [random.randint(-20,20), random.randint(-20,20)]
        self.collected = False
    def move(self):
        self.rect = self.rect.move(self.speed)


##############################
# save all the data collected from the forms and the game to a comma-delimited text file
##############################
def save_user_data():

  global user_height_inches
  global user_hand_inches
  global user_injuries
  global user_age
  global user_handedness
  global user_sleep_hours
  global user_active_hours
  global user_milk_glasses
  global average_grip
  global grips
  
  # open the file for appending, i.e. mode = "a"
  user_data_file = open("user_data.csv", "a") 

  # create the data_row from the global variables collected from the GUI forms
  data_row = str(user_height_inches) + "," + str(user_hand_inches)  + ","
  data_row = data_row + str(user_injuries) + "," + str(user_age) + "," + user_handedness + "," 
  data_row = data_row + str(user_sleep_hours)  + "," + str(user_active_hours) + ","
  data_row = data_row + str(user_milk_glasses) + ","
  
  # loop through all the grip values captured in the game, calcualte their sum, and add them to a temporary string
  # use a temp variable for the grip values because we want to insert the average_grip (which still needs to be calcualted) 
  # into data_row BEFORE the rest of the grip values
  grips_sum = 0
  temp = "" 
  for grip in grips:
    temp = temp + "," + str(grip)
    grips_sum = grips_sum + grip
    print(grip)
  
  # calculate the average grip, and append it with the grip values (temp) to data_row
  average_grip = grips_sum/len(grips)
  data_row = data_row + str(average_grip) + temp + "\n"
  
  # add the data_row to the text file, then close it
  user_data_file.write(data_row)
  user_data_file.close()


def add_sensor(sensor_collection):

  # create a random sensor and place it randomly on the screen, subtracting the moon's section (bottom 150 pixels)
  sensor = Sensor([random.randint(25,640-25), random.randint(25,680-150)])
  
  # add the sensor to the collection, and return the sensor
  sensor_collection.add(sensor)
  return sensor

def move_sensors(sensor_collection):

  for obj in sensor_collection:
    if not obj.collected:
      # call the move() method
      obj.move()
 
      # if sensor is close to the left or right edges of the screen, make it switch direction
      if obj.rect.left > 630 or obj.rect.left < 10:
        obj.speed[0] = -1 * obj.speed[0]
 
      # if sensor is close to the top or bottom edges of the sky (subtract the moon height), make it switch direction
      if obj.rect.top < 10 or obj.rect.top > 550:
        obj.speed[1] = -1 * obj.speed[1]


##############################
# define turtle graphing functions
##############################
def draw_axes(turtle_object, x_offset, y_offset):
  turtle_object.hideturtle()
  turtle_object.penup()
  turtle_object.goto(x_offset,y_offset)
  turtle_object.pendown()
  turtle_object.forward(400)
  turtle_object.stamp()
  turtle_object.backward(400)
  turtle_object.left(90)
  turtle_object.forward(400)
  turtle_object.stamp()
  turtle_object.backward(400)
  turtle_object.right(90)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 50)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 100)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 150)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 200)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 250)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 300)
  turtle_object.dot(5)
  turtle_object.goto(x_offset, y_offset + 350)
  turtle_object.dot(5)
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 50)
  turtle_object.pendown()
  turtle_object.write("25")   # this is half the pixel offset (50) because the graph is plotted with y values * 2 for a larger scale graph
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 100)
  turtle_object.pendown()
  turtle_object.write("50")
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 150)
  turtle_object.pendown()
  turtle_object.write("75")
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 200)
  turtle_object.pendown()
  turtle_object.write("100")
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 250)
  turtle_object.pendown()
  turtle_object.write("125")
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 300)
  turtle_object.pendown()
  turtle_object.write("150")
  turtle_object.penup()
  turtle_object.goto(x_offset - 20, y_offset + 350)
  turtle_object.pendown()
  turtle_object.write("175")
  turtle_object.penup()
  turtle_object.goto(x_offset - 160, y_offset + 100)
  turtle_object.pendown()
  turtle_object.write("Grip Strength (N)", font=('Arial', 10, 'bold'))
  turtle_object.penup()
  turtle_object.goto(x_offset + 100, y_offset - 50)
  turtle_object.pendown()
  turtle_object.write("Sensor Periodic Collection", font=('Arial', 10, 'bold'))
  turtle_object.penup()
  turtle_object.goto(x_offset, y_offset)
  turtle_object.pendown()

# draw the graph from the grip sensor data 
def graph_grip():
  
  global grips
  global average_grip
  
  wn = trtl.Screen()
  
  # turtle used to draw the axes and the graph of the grip sensor data
  graph = trtl.Turtle()
  xoffset = -200
  yoffset = -100
  draw_axes(graph, xoffset, yoffset) # draw the x-y axes
  
  # turtle used to write results on Turtle screen
  messenger = trtl.Turtle()
  messenger.hideturtle()
  messenger.penup()
  messenger.goto(-300, -200)
  messenger.pendown()
  messenger.write("Here is a visual representation of your grip strength captured in the game.", font=('Arial', 12, 'bold'))

  # graph the points
  for i in range(0, len(grips)):
    graph.setposition(xoffset + (i+1)*10, yoffset + grips[i]*2)
    print(grips[i])
  
  # display the average grip in (N)
  messenger.penup()
  messenger.goto(-300, -250)
  messenger.pendown()
  messenger.write("On average, your grip strength is:" + str(round(average_grip, 4)) + " N", font=('Arial', 12, 'bold'))
  
  wn.mainloop()


##############################
# define the pygame function
##############################
def start_game():
  
  global game_over
  global font

  # start initializing objects
  pygame.init()
  screen = pygame.display.set_mode([640,680])
  font = pygame.font.SysFont("comicsansms", 30)
  pygame.display.set_caption('Lunar Lander')
  pygame.key.set_repeat(50,50) # Set key repeat (delay,interval)
  background = pygame.image.load('background.png')
  lander = Lander([random.randint(0,640-25),0]) # creates a lander object at random x, y=0
  moon = Moon([0,530]) # creates a moon at [x 0, y 530]
  score_label = font.render("Score: 0", 1, (255,255,255)) # Make a surface out of the base font
  
  # create a group to add any objects that need to be detected for collision to end the game
  # this only contains the moon object for now, but more objects can be added to it to end the game
  collision_group = pygame.sprite.Group()
  collision_group.add(moon)

  # create a group to add sensors that the lander can collect during the game 
  collection_group = pygame.sprite.Group()
  sensor_1 = add_sensor(collection_group)
  sensor_2 = add_sensor(collection_group)
  sensor_3 = add_sensor(collection_group)
  sensor_4 = add_sensor(collection_group)
  sensor_5 = add_sensor(collection_group)

  # add / display objects on the screen
  screen.blit(background,[0,0]) # In pygame, blit means copy so copy the background surface to [x 0 ,y 0]
  screen.blit(lander.image,lander.rect) # Copy the lander image to coords defined in its rect
  screen.blit(moon.image,moon.rect) # Blit the moon
  screen.blit(score_label, [480,600])
  screen.blit(sensor_1.image,sensor_1.rect) # Blit the random Sensor
  screen.blit(sensor_2.image,sensor_2.rect)
  screen.blit(sensor_3.image,sensor_3.rect)
  screen.blit(sensor_4.image,sensor_4.rect)
  screen.blit(sensor_5.image,sensor_5.rect)
  pygame.display.flip() # In pygame we draw (blit) onto the screen then we 'flip' to the screen we drew on, so it all appears at once

  # set up gdx sensor
  my_gdx = gdx.gdx()  # object to be used with the Vernier sensor
  my_gdx.open_usb()
  my_gdx.select_sensors([1,3]) # hand dynamometer ch1 = force, and ch3 = y axis accel
  my_gdx.start(period=200)   # set the frequency of sensor data retrieval to every half 200 ms
  print("enabled_sensor_info:", my_gdx.enabled_sensor_info())

  # calibrate/baseline the force sensor
  measurements = my_gdx.read()
  f0 = measurements[0]
  f1 = measurements[0]

  #Main game loop
  while not game_over:
    screen.fill([255,255,255]) # Fill the screen, (to wipe out everything else)
    for event in pygame.event.get(): # Get all events
      if event.type == pygame.QUIT: # if x button clicked on the window
        my_gdx.stop()
        my_gdx.close()
        sys.exit() # then quit the program

    # if no pygame events are detected, then use gdx to get the sensor values
    measurements = my_gdx.read()
    print(measurements)

    if (measurements != None):
      # read the Y-axis tilt that affects the xspeed of the sprite (left/right movement)
      xspeed = measurements[1] * 5
      
      # calculate the change in force, if any. this will determine the yspeed of the sprite
      f0 = f1
      f1 = measurements[0]
      print("Change in force: ", f1-f0)
      
      # only change the vertical speed if the change in > 1, i.e. only when pressing, not releasing the grip!
      # compare the change to 1, rather than 0, allowing for small margin of sensor error (simply holding it can cause a small change)
      if (f1-f0) > 1:
        yspeed = gravity - ((f1-f0)/3)   # slow down the yspeed based on the rate of change in force
        grips.append(measurements[0])
      else:
        yspeed = gravity    # reset it back to normal gravity
      
      # set the new speeds
      lander.speed = [xspeed, yspeed]
      print("new X speed is:", xspeed)
      print("new Y speed is:", yspeed)

    # Checks for collisions with moon sprite, to end the game
    if pygame.sprite.spritecollide(lander, collision_group, False):
      game_over = True
    
    # get all Sensors that have been collected
    sensors_collected = pygame.sprite.spritecollide(lander, collection_group, False)
    for obj in sensors_collected:
      obj.collected = True
    
    # move the objects on the screen only if game is not over yet
    if not game_over:
      lander.move()
      move_sensors(collection_group)
    
    # update display
    screen.blit(background,[0,0])  # Blit the screen every time through the loop
    screen.blit(lander.image,lander.rect)  # And the lander
    screen.blit(moon.image,moon.rect)  # And the moon
    
    # blit the sensors that have not been collected yet, and add to the score for those that have been collected
    score = 0
    for obj in collection_group:
      if obj.collected:
        score = score + 10
      else:
        screen.blit(obj.image,obj.rect) # Blit the Sensor
    
    # blit the score label
    score_label = font.render("Score: " + str(score), 1, (255,255,255)) # Make a surface out of the base font
    screen.blit(score_label,[480,600]) # Blit the label
    
    # Flip to the new screen
    pygame.display.flip()
    pygame.time.delay(30)
  # end of the game loop

  # game is over... finalize the rest
  # stop and close the gdx sensor
  my_gdx.stop()
  my_gdx.close()

  # display message
  label = font.render("Game over! Click anywhere to continue...", 1, (255,255,255)) # Make a surface out of the base font
  screen.blit(label,[50,50]) # Blit the label
  pygame.display.flip() # Flip to the new screen
  pygame.time.delay(30) # 

  # wait for the mouse click to continue to the graph
  while True:
    for event in pygame.event.get(): # Get all event
      if event.type == pygame.QUIT: # if x clicked...
        sys.exit() # then quit the program
      elif event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        save_user_data()
        graph_grip()
        
##############################
# main program
##############################

# start the GUI forms
root = tk.Tk()
root.wm_geometry("550x550")
root.title("Data Collection")

##############################
# create frame for physiology
##############################
frame_physiology = tk.Frame(root, height=550, width=550)
frame_physiology.grid_propagate(0)
frame_physiology.grid(row=0, column=0)

# create the text boxes
# height label
lbl_height = tk.Label(frame_physiology, text='Enter your height:')
lbl_height.grid(row=0, column=0, padx=20, pady=20)

# text box for feet measurement
ent_feet = tk.Entry(frame_physiology, width=5, bd=3)
ent_feet.grid(row=0, column=1)

# label for feet '
lbl_feet = tk.Label(frame_physiology, text="'")  # feet
lbl_feet.grid(row=0, column=2)

# text box for inches measurement
ent_inches = tk.Entry(frame_physiology, width=5, bd=3)
ent_inches.grid(row=0, column=3)

# label for inches "
lbl_inches = tk.Label(frame_physiology, text='"')  # inches
lbl_inches.grid(row=0, column=4)

# hand length label
lbl_hand_length = tk.Label(frame_physiology, text='Enter the length of your hand:' )
lbl_hand_length.grid(row=1, column=0, padx=20, pady=10)

# text box for inches measurement
ent_hand_length = tk.Entry(frame_physiology, width=5, bd=3)
ent_hand_length.grid(row=1, column=1)

# label for inches "
lbl_hand_inches = tk.Label(frame_physiology, text='"')  # inches
lbl_hand_inches.grid(row=1, column=2)

# hand injuries label
lbl_injuries = tk.Label(frame_physiology, text='How many times have you injured your dominant hand?')
lbl_injuries.grid(row=2, column=0, padx=20, pady=10)

# text box for injuries
ent_injuries = tk.Entry(frame_physiology, width=5, bd=3)
ent_injuries.grid(row=2, column=1)

# age label
lbl_age = tk.Label(frame_physiology, text='How old are you?' )
lbl_age.grid(row=3, column=0, padx=20, pady=10)

# text box for age
ent_age = tk.Entry(frame_physiology, width=5, bd=3)
ent_age.grid(row=3, column=1)

# handedness label
lbl_handedness = tk.Label(frame_physiology, text='Are you right or left handed?')
lbl_handedness.grid(row=4, column=0, padx=20, pady=10)

# list box for handedness
lst_handedness = tk.Listbox(frame_physiology, width=5, height=2, bd=3)
lst_handedness.insert(0, "Right")
lst_handedness.insert(1, "Left")
lst_handedness.selectmode = tk.SINGLE
lst_handedness.grid(row=4, column=1)

# create Next button
btn_next = tk.Button(frame_physiology, text='Next >>', command=next, padx=10, pady=10, bd=3)
btn_next.grid(row=5, column=5)

##############################
# create frame for habits data 
##############################
frame_habits = tk.Frame(root, height=550, width=550)
frame_habits.grid_propagate(0)
frame_habits.grid(row=0, column=0)

# hours of sleep label
lbl_sleep = tk.Label(frame_habits, text='How many hours of sleep do you get per night?' )
lbl_sleep.grid(row=0, column=0, padx=20, pady=20)

# text box for sleep
ent_hours_sleep = tk.Entry(frame_habits, width=5, bd=3)
ent_hours_sleep.grid(row=0, column=1)

# hours of activity label
lbl_active = tk.Label(frame_habits, text='How many hours of exercise do you do per day?' )
lbl_active.grid(row=1, column=0, padx=20, pady=20)

# text box for activity
ent_hours_active = tk.Entry(frame_habits, width=5, bd=3)
ent_hours_active.grid(row=1, column=1)

# glasses of milk label
lbl_milk = tk.Label(frame_habits, text='How many glasses of milk do you drink per day?')
lbl_milk.grid(row=2, column=0, padx=20, pady=20)

# text box for milk
ent_glasses_milk = tk.Entry(frame_habits, width=5, bd=3)
ent_glasses_milk.grid(row=2, column=1)

# create the buttons
btn_back = tk.Button(frame_habits, text='<< Back', command=back,  padx=10, pady=10, bd=3)
btn_back.grid(row=3, column=0, pady=20)
btn_submit = tk.Button(frame_habits, text='Submit', command=submit_data, padx=10, pady=10, bd=3)
btn_submit.grid(row=3, column=1)

##############################
# create frame for confirmation message and launch of the turtle/sensor screen
##############################
frame_confirmation = tk.Frame(root, height=550, width=550)
frame_confirmation.grid_propagate(0)
frame_confirmation.grid(row=0, column=0)
msg_confirmation = tk.Message(frame_confirmation, 
                              text="Excellent! \n\n" +
                                "It's time to test your grip strength by playing a game! \n\n" +
                                "Hold the Hand Dynamometer in your dominant hand with its power button facing left. In the game, you must: \n" +
                                "  a) Tilt the Dynamometer left and right to move the lander and collect the sensors that fell out of the spacecraft! \n" +
                                "  b) Squeeze the sensor to slow down the lander's vertical speed. The stronger the squeeze, the slower the lander will fall. \n\n" +
                                "Are you ready to play?", 
                              foreground="green",
                              width=450)
msg_confirmation.grid(row=0, column=0, padx=20, pady=20)
btn_play = tk.Button(frame_confirmation, text='Play the Game!', command=play_game, padx=10, pady=10, bd=3)
btn_play.grid(row=1, column=0)

load = Image.open("csp315_sensor_hold.png")
render = ImageTk.PhotoImage(load)
canvas = tk.Canvas(frame_confirmation, width = 195, height = 260)
canvas.grid(row=2, column=0)
canvas.create_image(0,0,image=render,anchor=tk.NW)

# make the physiology frame visible (top layer)
frame_physiology.tkraise()
root.mainloop()
