# Завдання №3 Смайл

# Потребує pygame

from re import X
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()


# Defie the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
yellow = (255, 255, 0) 

# Set the height and width of the screen
size = [300, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Вітаю!")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:

    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
        
    pygame.draw.circle(screen, yellow, [150, 150], 80)
    pygame.draw.ellipse(screen, BLACK, [165, 110, 20, 50]) 
    pygame.draw.ellipse(screen, BLACK, [115, 110, 20, 50]) 

   
    pygame.draw.circle(screen, BLACK, [150, 168], 46, 5, draw_bottom_left=True)
    pygame.draw.circle(screen, BLACK, [150, 168], 46, 5, draw_bottom_right=True)

    pygame.draw.circle(screen, BLACK, [108, 168], 10, 0, draw_top_left=True)
    pygame.draw.circle(screen, BLACK, [191, 168], 10, 0, draw_top_right=True)

    pygame.display.flip()