# import tkinter and everything with it
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
label1 = Label(root, text = "hello world")

label2 = Label(root, text = "My name is <name>")

# the other way to place it is in the grid system
# the grid system is relative to eachother

label1.grid(row=0,column=0)
label2.grid(row=1, column=0)

# since python is OOP, you can save some time by doing this
# note the .grid on the end
label3 = Label(root, text = "Look ma, no extra line").grid(row=2, column = 1)

# the loop here listens for any events, such as mouse movement
# must be exactly 'mainloop()'
root.mainloop()
