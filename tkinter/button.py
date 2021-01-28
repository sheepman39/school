from tkinter import *

root = Tk()
# in order for a button to do something, you must have a function
clicks = 0
def numClicks(clicks):
  if(clicks == 0):
    return "Look I clicked!"
  elif(clicks == 1):
    return "Why did you click me again?"
  elif(clicks == 2):
    return "That tickles!"
  elif(clicks == 3):
    return "Oh please don't make me disable myself"
  elif(clicks == 4):
    return "I swear stop clicking me!"
  elif(clicks == 5):
    button.config(state=DISABLED)
    return "Ha now you can't click me"
  else:
    return "this shouldn't be possible"

def onClick():
  global clicks
  myLabel = Label(root, text=numClicks(clicks))
  clicks += 1
  myLabel.pack()

# like everything else, a button is a widget
# you can do 'state=DISABLED' to disable the button
# padx/y can change size of the button
# call the function with 'command=<name of function>'
button = Button(root, text="Click me", padx=50, pady=20,command=onClick)

button.pack()

root.mainloop()