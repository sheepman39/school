#   a123_apple_1.py
import turtle as trtl
import random as rand
import functools 

#-----setup-----
# NOTE: since this is in a folder and the code is (probably) not running in the same folder, you must give a file path for it to go to.  
#This will vary slightly depending on your setup.  
#If it is running in the same folder and you are not funky like I am, you can leave it 'pear.gif'

pear_image = "./1.2.3_Project/pear.gif" # Store the file name of your shape

# Screen setup for the background and size
wn = trtl.Screen()
wn.bgpic("./1.2.3_Project/background.gif")
wn.setup(width=1.0, height=1.0)

# Make the screen aware of the new file
wn.addshape(pear_image) 

# Random variables for stuff
# font_setup is for fonts.  
font_setup = ("Arial", 55, "normal")

# alphabet_list contains the characters needed on the home row
alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# turtle list is where turtle objects are stored and kept with corresponding letters
turtle_list = []

# height where the apples/pears will fall
ground_height = -120

# number of pears setting
num_letters = 5
current_letters = 0

# notification turtle
notification = trtl.Turtle()
notification.ht()

# NOTE this is a bit farther along than what we've gone through
# A class stores multiple properties in one variable
# this makes it easier to store and manipulate values
# This will store the pear, the writer, and the random letter
# Makes life easier

class game_turtle():
  def __init__ (self, turtle, writer, letter):
    self.turtle = turtle
    self.writer = writer
    self.letter = letter

#-----functions-----

def random_letter():
  # return will send *the letter* that was in the index that was randomly selected with the rand.randint() function
  return alphabet_list.pop(rand.randint(0,len(alphabet_list)-1))

# This function actually makes the pear fall
def pear_fall(letter, index):
  
  global current_letters
  # the index tells where in the list the correct turtle is
  # makes sure the pen is up and the writing is cleared
  turtle_list[index].turtle.penup()
  turtle_list[index].writer.clear()
  turtle_list[index].writer.hideturtle()

  # updates the screen properly
  wn.update()

  # this makes the pear fall
  turtle_list[index].turtle.goto(turtle_list[index].turtle.xcor(),ground_height)
  
  # increases current letters
  current_letters += 1

  # if the number of letters your clicked is 
  # greater than or equal to the number of letters you should have,
  # do stuff
  if(current_letters >= num_letters):
    
    # Text box asks if you want to restart the game
    play_again = wn.textinput("Woohoo!","Would you like to play again? \nHit enter to keep playing or press y/n")
    
    # if you hit yes or y, restarts the game
    if(play_again == "" or play_again.lower() == "y" or play_again.lower() == "yes"):
      
      current_letters = 0
      game_start()
    
    # else, close the game
    else:
      
      wn.bye()

# Originally, I had to do each one of these individually,
# but i found a way to pass a letter as an argument
# more info how down below
def fall(letter):
  
  #for loop repeats the if statement for as long as the list is
  for i in range(len(turtle_list)):

    # if statement checks if the letter value of the object is equal to the correct letter
    if(turtle_list[i].letter == letter):
      
      # calls the pear_fall function with the proper arguments
      pear_fall(letter, i)
      
      # break ends the for loop and prevents the need for it to continue
      break

# game_start() places the 5 turtles with the random letters
def game_start():
  
  global turtle_list
  global alphabet_list
  if(len(turtle_list) > 0):
    
    #hides the turtles when a game is started
    for i in turtle_list:
      i.turtle.ht()
  
    # resets major variables
    turtle_list = []
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

  
  #repeats the loop 5 times
  for i in range(num_letters):
    
    # creates the writer turtle for the letter
    writer = trtl.Turtle()
    writer.penup()
    writer.speed(-1)
    writer.hideturtle()
    
    # creates the pear turtle and sets its location
    temp_turtle = trtl.Turtle()
    temp_turtle.shape(pear_image)
    temp_turtle.speed(-1)
    temp_turtle.penup()
    temp_turtle.goto(-150+i*75,0)
    temp_turtle.speed(3)

    # sets the location of the writer
    writer.goto(temp_turtle.xcor()-25,temp_turtle.ycor()-60)
    
    # creates a new object with the pear, writer, and the random letter
    # NOTE this is a bit ahead of what we worked with already
    # Objects are kind of hard to explain. 
    # Pretty much an object can store multiple values and properties in a single variable,
    # making it easier to group different values together

    obj_turtle = game_turtle(temp_turtle, writer, random_letter())
    
    # adds the new object into the turtle_list array
    turtle_list.append(obj_turtle)
    
    # writes the random letter on top of the pear
    writer.write(turtle_list[i].letter,font=font_setup)

    # This will loop through the entire alphabet
    # NOTE YOU MUST 'import functools' in order for this to work
  for k in 'abcdefghijklmnopqrstuvwxyz':
    
    # functools.partial allows the fall function to pass
    # an argument, allowing the keys to work better
    # also, it sets the key it listens for as 'k'
    # this is a much better way of doing this!
    wn.onkeypress(functools.partial(fall, k),key = k)
    wn.listen()

# starts the game by drawing the apples
game_start()

wn.listen()
wn.mainloop()