import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    shot_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shot_group)
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0

    # Infinite game loop
    while True:
        # Quits game if (x) button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit() # Quit/close game

        screen.fill("black")

        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()

        # Limit to 60 fps
        dt = game_clock.tick(60) / 1000
        # Infinite game loop end

    

if __name__ == "__main__":
    main()