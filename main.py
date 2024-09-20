import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()    
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #create the screen and draw and update all objects
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()
            if asteroid.collision_check(player):
                sys.exit("Game over!")

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        #limit framerate to 60
        dt = gameClock.tick(60)/1000
        
        

if __name__ == "__main__":
    main()

