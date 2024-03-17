import pygame
from sys import exit
import json
from pathlib import Path


# Game
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# Game variables
script_location = Path(__file__).absolute().parent
file_location = script_location / 'global.json'
f = open(file_location, 'r')
global_variables = json.load(f)

# Player variables
player_variables = global_variables['player']
player_width = player_variables['player_width']
player_height = player_variables['player_height']
player_x = player_variables['player_x']
player_y = player_variables['player_y']
player_background = pygame.Surface((player_width+10,player_height+10))
player_background.fill('black')

# Player draw
player = pygame.Surface((player_width,player_height))
player.fill('Red')


# Main loop
while True:
    # Exit game
    for event in pygame.event.get():
        # If player closes the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Player input movement
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x = player_x - 5

    if keys[pygame.K_RIGHT]:
        player_x = player_x + 5

    

    screen.blit(player_background, (player_x-5,player_y))
    screen.blit(player,(player_x,player_y))

    pygame.display.update()
    clock.tick(60)