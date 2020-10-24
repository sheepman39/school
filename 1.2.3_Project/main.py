#   a123_apple_1.py
import turtle as trtl
import random as rand

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
alphabet_list = ["a","s","d","f","g","h","j","k","l"]

# turtle list is where turtle objects are stored and kept with corresponding letters
turtle_list = []

# height where the apples/pears will fall
ground_height = -120

# initial definition of pear
pear = trtl.Turtle()

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
  
  # the index tells where in the list the correct turtle is
  # makes sure the pen is up and the writing is cleared
  turtle_list[index].turtle.penup()
  turtle_list[index].writer.clear()
  
  # updates the screen properly
  wn.update()

  # this makes the pear fall
  turtle_list[index].turtle.goto(turtle_list[index].turtle.xcor(),ground_height)

# NOTE this is a terrible way of doing this!
# I was not able to find a way (yet) to pass an argument for .onkeypress()
# hencefourth, I had to make a different function for each
# individual
# letter
# This is inefficient but i had to >:(

def a_fall():
  
  #for loop repeats the if statement for as long as the list is
  for i in range(len(turtle_list)):

    # if statement checks if the letter value of the object is equal to the correct letter
    if(turtle_list[i].letter == "a"):
      
      # calls the pear_fall function with the proper arguments
      pear_fall("a", i)
      
      # break ends the for loop and prevents the need for it to continue
      break

def s_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "s"):
      pear_fall("s", i)
      break

def d_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "d"):
      pear_fall("d", i)
      break

def f_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "f"):
      pear_fall("f", i)
      break

def g_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "g"):
      pear_fall("g", i)
      break

def h_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "h"):
      pear_fall("h", i)
      break

def j_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "j"):
      pear_fall("j", i)
      break

def k_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "k"):
      pear_fall("k", i)
      break

def l_fall():
  for i in range(len(turtle_list)):
    if(turtle_list[i].letter == "l"):
      pear_fall("l", i)
      break

# game_start() places the 5 turtles with the random letters
def game_start():
  
  #repeats the loop 5 times
  for i in range(5):
    
    # creates the writer turtle for the letter
    writer = trtl.Turtle()
    writer.penup()
    writer.hideturtle()
    
    # creates the pear turtle and sets its location
    temp_turtle = trtl.Turtle()
    temp_turtle.shape(pear_image)
    temp_turtle.penup()
    temp_turtle.goto(-150+i*75,0)
    
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
    
    


#-----function calls-----

# starts the game by drawing the apples
game_start()

# NOTE This is also a terrible way of doing this
# I am probably just really stupid
# But I have yet to figure out how to actually pass
# an argument with on key press to include which key
# is being pressed
# so i have to do this manually ¯\_(ツ)_/¯
wn.onkeypress(a_fall,"a")
wn.onkeypress(s_fall,"s")
wn.onkeypress(d_fall,"d")
wn.onkeypress(f_fall,"f")
wn.onkeypress(g_fall,"g")
wn.onkeypress(h_fall,"h")
wn.onkeypress(j_fall,"j")
wn.onkeypress(k_fall,"k")
wn.onkeypress(l_fall,"l")

wn.listen()
wn.mainloop()