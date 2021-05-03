import turtle as trtl

wn = trtl.Screen()
wn.colormode(255)

painter = trtl.Turtle()
painter.shape("square")
painter.setheading(0)
painter.turtlesize(1)
painter.penup()

# cordinates list helps manage the placement of the turtle
cordinates = [15,15]
painter.goto(cordinates[0],cordinates[1])

# put the rgb color codes in here for what you want your color to be
# the colors will match the values in art
colors = [(0,0,0),(255,255,255)]

# this is the bitmap of the created image
# the numbers in here will refer to the index's in the colors list
art = [
    '000001000000',
    '000010100000',
    '000100010000',
    '001000001000',
    '010000000100',
    '110001000110',
    '010000000100',
    '001000001000',
    '000100010000',
    '000010100000',
    '000001000000', 
]

# for the different rows in art,
for pixels in art:
    # check the individual value of the pixels
    for color in pixels:
        # set the fill color to the one pixel
        painter.fillcolor(colors[int(color)])
        # change the location of the turtle
        cordinates[0] += 15
        painter.goto(cordinates[0], cordinates[1])
        # stamp a square
        painter.stamp()
    # when that row is done, go down a level and back to the starting x pos
    cordinates[1] -= 15
    cordinates[0] = 15
    painter.goto(cordinates[0],cordinates[1])
        
wn.mainloop()