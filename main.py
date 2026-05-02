import pygame
from constants import *
from logger import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    # Sets available display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create game clock
    clock = pygame.time.Clock()
    dt = 0

    # Create update and draw groups for main loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Set objects to specific container groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #Draw Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        #Check if user closes game window and exit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for event in pygame.event.get():
            pass
        
        #Fill screen black
        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        #Update the display
        pygame.display.flip()

        #Delta time calculation for 60 FPS
        dt = clock.tick(60) / 1000

            
if __name__ == "__main__":
    main()
