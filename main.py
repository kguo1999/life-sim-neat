import pygame
import neat
import time
import os
import random

from classes import * 

# Define constants
WIN_WIDTH = 1280
WIN_HEIGHT = 720

MAP_IMG = pygame.image.load('img/map.png')
HUMAN_IMG = pygame.image.load('img/agent.png')

def draw_window(win, human, map):
    win.blit(map, (0,0))
    human.draw(win)

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

human = Human(100, 100, HUMAN_IMG)

### TESTING ###
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    human.handle_keys()
    # human.move_left()

    draw_window(win, human, MAP_IMG)
    
    pygame.display.update()

    clock.tick(30)
