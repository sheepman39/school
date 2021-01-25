from tkinter import *

root = Tk()
# in order for a button to do something, you must have a function
clicks = 0
def numClicks(clicks):
  if(clicks == 0):
    return "Look I clicked!"
  elif(clicks == 1):
    pass

def onClick():
  myLabel = Label(root, text="Look, I clicked")
  myLabel.pack()

# like everything else, a button is a widget
# you can do 'state=DISABLED' to disable the button
# padx/y can change size of the button
# call the function with 'command=<name of function>'
button = Button(root, text="Click me", padx=50, pady=20,command=onClick)

button.pack()

root.mainloop()