#   a123_apple_1.py
import turtle as trtl

#-----setup-----
# NOTE: since this is in a folder and the code is (probably) not running in the same folder, you must give a file path for it to go to.  
#This will vary slightly depending on your setup.  
#If it is running in the same folder and you are not funky like I am, you can leave it 'pear.gif'
pear_image = "./1.2.3_Project/pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("./1.2.3_Project/background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file

pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def fall(turtle):
  turtle.penup()
  turtle.goto(turtle.xcor(),-120)

#-----function calls-----
draw_apple(pear)
fall(pear)

wn.mainloop()