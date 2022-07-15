# Essential
import pygame
import os  # Only essential if assets are used

# Very useful
import math
import random

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
player = pygame.Rect((0, 0), (32, 32))  # Example

# Loads assets (remove triple apostrophes to use)
'''SPRITE_NAME = pygame.image.load(os.path.join("assets_folder", "filename"))  # Loads image from a folder
SPRITE_NAME = pygame.transform.scale(sprite_name, (32, 32))  # Makes image size in pixels as desired (32, 32)
MOVEMENT_SOUND = pygame.mixer.Sound(os.path.join("assets_folder", "filename"))  # Loads sound from a folder
'''

# Setup
pygame.init()  # Initializes pygame
pygame.mixer.init()  # Initializes pygame's sound system
pygame.font.init()  # Initializes pygame's fonts
pygame.display.set_caption("ExampleName")  # The title of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Makes game window
FONT = pygame.font.SysFont("Comic Sans MS", 32)  # Font name, font size. Taken from pygame

# Example Functions
def move_player():
    player.x += 1
    player.y += 1


def draw_player():
    pygame.draw.rect(screen, RED, player)


# Main loop
def main():
    # Variables used in game
    run = True
    clock = pygame.time.Clock()

    # Game loop
    while run:
        # Gets input
        for event in pygame.event.get():
            # Closes game when told to
            if event.type == pygame.QUIT:
                run = False

        # Game logic
        move_player()  # Example

        # Clear screen
        screen.fill(WHITE)  # Replace WHITE with desired background color

        # Draw things to screen
        draw_player()  # Example

        # Updates screen and runs at set FPS
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()  # Quits game when loop is stopped


main()  # Starts game
