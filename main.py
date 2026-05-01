import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        #Check for user closing game window and exit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for event in pygame.event.get():
            pass
        
        #Fill screen black and update display
        screen.fill("black")
        pygame.display.flip()

        
        #Delta time calculation for 60 FPS
        dt = clock.tick(60) / 1000
            
if __name__ == "__main__":
    main()
