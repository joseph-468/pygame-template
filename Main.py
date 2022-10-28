import pygame

# CONSTANTS
WIDTH, HEIGHT = 800, 800
FPS = 60


# Main
def main():
    # Setup
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.display.set_caption("WindowName")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Variables

    # Load assets

    # Game loop
    while True:
        # Gets input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Updates screen
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
