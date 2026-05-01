import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    #Draw Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        for item in drawable:
            item.draw(screen)

        #Update the display
        pygame.display.flip()

        #Delta time calculation for 60 FPS
        dt = clock.tick(60) / 1000

            
if __name__ == "__main__":
    main()
