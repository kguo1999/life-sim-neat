import pygame
import neat
import time
import os
import random

# Define constants
WIN_WIDTH = 1280
WIN_HEIGHT = 720

MAP_IMG = pygame.image.load('img/map.png')
HUMAN_IMG = pygame.image.load('img/agent.png')


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

# Draw background - same resolution so 0,0
win.blit(MAP_IMG, (0,0))

### TESTING ###
running = True
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # win.blit(MAP_IMG, (0,0))
    pygame.display.update()