#skeleton for a pygame project
import pygame
import random
from settings import *

#initilize pygame and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# Game loop

running = True
while running:
    #Keep loop running at the right speed
    clock.tick(FPS)

    #Process input
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False

    #update


    #render/draw
    screen.fill(BLACK)
    # *after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()