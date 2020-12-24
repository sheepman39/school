import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    
    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    # in order to place an object in the center, you must do some math
    # default place to the upper left corner
    surf_center = (
    (screen_width-surf.get_width())/2,
    (screen_height-surf.get_height())/2
    )

    # This line says "Draw surf onto the screen at the center"
    screen.blit(surf, surf_center)

    # tells the program to update the entire screen
    pygame.display.flip()