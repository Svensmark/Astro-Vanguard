import pygame
from sys import exit
from player import Player

# Read variables json


# Core game
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
def handle_exit():
     # Exit game
    for event in pygame.event.get():
        # If player closes the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Player
player = pygame.sprite.GroupSingle()
player.add(Player())


# Background
map_background = pygame.image.load('graphics/background.png').convert_alpha()


while True:
    # Handle exit of game
    handle_exit()
        
    # Handle background
    screen.blit(map_background,(0,0))    
    
    # Player
    player.update()
    player.draw(screen)
    
    # Update screen
    pygame.display.update()
    clock.tick(60)
    

