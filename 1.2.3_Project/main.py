#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
# NOTE: since this is in a folder and the code is (probably) not running in the same folder, you must give a file path for it to go to.  
#This will vary slightly depending on your setup.  
#If it is running in the same folder and you are not funky like I am, you can leave it 'pear.gif'

pear_image = "./1.2.3_Project/pear.gif" # Store the file name of your shape

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
  
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.


wn = trtl.Screen()
wn.bgpic("./1.2.3_Project/background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file

font_setup = ("Arial", 55, "normal")
alphabet_list = ["a","s","d","f","g","h","j","k","l"]
ground_height = -120

turtle_list = []

pear = trtl.Turtle()
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
# This is what I did for number 15.  List is at the top of code
def random_letter():
  
  # return will send the letter that was in the index that was randomly selected with the rand.randint() function
  return alphabet_list.pop(rand.randint(0,len(alphabet_list)))

def draw_apple(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def pear_fall():
  pear.penup()
  apple.clear()
  wn.update()
  pear.goto(pear.xcor(),ground_height)

def letter_draw(turtle,letter):
  turtle.penup()
  apple.hideturtle()
  turtle.goto(pear.xcor()-18,pear.ycor()-40)
  turtle.write(letter, font = font_setup)

def game_start():
  current_letter = random_letter()
  letter_draw(apple,current_letter)
  wn.onkeypress(pear_fall, current_letter)

#-----function calls-----

draw_apple(pear)

for i in range(5):
  temp_turtle = trtl.Turtle()
  temp_turtle.shape(pear_image)
  turtle_list.append(temp_turtle)
  turtle_list[i].penup()
  turtle_list[i].goto(-150+i*75,0)

game_start()
wn.listen()
wn.mainloop()