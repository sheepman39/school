# 1.1.9_final_project.py
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()
screen = trtl.Screen()
screen.setup(280, 190)
trtl.bgcolor("#72b964")
painter.color("white")

painter.circle(20)
painter.circle(100)

wn = trtl.Screen()
wn.mainloop()

