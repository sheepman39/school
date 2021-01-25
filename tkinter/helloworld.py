from tkinter import *

# in tkinter, everything is a widget
# buttons, frames, text boxes ect. are treated as widgets
# and the main widget is referred as the 'root' widget
# this line creates that root widget
root = Tk()

# to create anything, you have to take 2 steps
# step 1: define the thing
# step 2: put it on the screen

# we defined what our label is
# it is going to go in the root widget with text saying 'hello world'
my_label = Label(root, text = "hello world")

# 2 ways to display stuff
# for now, only do one
my_label.pack()


# the loop here listens for any events, such as mouse movement
# must be exactly 'mainloop()'
root.mainloop()
