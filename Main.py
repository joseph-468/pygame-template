# Essential
import pygame
import os

# Very useful
import math
import random

# Setup
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption("ExampleName")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
LIME = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
SILVER = 192, 192, 192
GREY = 128, 128, 128
DARKGREY = 64, 64, 64
MAROON = 128, 0, 0
OLIVE = 128, 128, 0
GREEN = 0, 128, 0
PURPLE = 128, 0, 128
TEAL = 0, 128, 128
NAVY = 0, 0, 128

# CONSTANTS
WIDTH, HEIGHT = 800, 800  # Resolution of screen
FPS = 60  # How many times the game should update per second

# Variables

# Loads assets (remove triple apostrophes to use)

# Functions


# Main loop
def main():
    # Variables used in game
    run = True
    clock = pygame.time.Clock()

    # Game loop
    while run:
        # Gets input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Game logic

        # Updates screen
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit() 


main()
