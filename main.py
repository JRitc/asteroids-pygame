import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite game loop
    while True:
        screen.fill("black")

        # Quits game if (x) button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        pygame.display.flip()
        # Infinite game loop end

    

if __name__ == "__main__":
    main()