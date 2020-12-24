# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
# specifies the width and height of the window to create
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # first parameter is the window to draw on
    # second is the RGB value
    # third is the center coordinates
    # fourth is the radius
    pygame.draw.circle(screen, (0, 0, 255), (0, 0), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()