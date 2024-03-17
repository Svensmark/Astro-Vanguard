import pygame
from sys import exit
import json
from pathlib import Path

# Game variables
script_location = Path(__file__).absolute().parent
file_location = script_location / 'global.json'
f = open(file_location, 'r')
global_variables = json.load(f)

# Default settings variables
default_settings = global_variables['default_settings']
window_height = default_settings['window_height']
window_width = default_settings['window_width']
game_clk = default_settings['game_clk']

# Game
pygame.init()
screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

# Player variables
player_variables = global_variables['player']
player_width = player_variables['player_width']
player_height = player_variables['player_height']
player_x = player_variables['player_x']
player_y = player_variables['player_y']
player_speed_x = player_variables['player_speed_x']
player_speed_y = player_variables['player_speed_y']

# Player draw
player = pygame.Surface((player_width,player_height))
player.fill('Red')

player_background = pygame.Surface((player_width+10,player_height))
player_background.fill('black')

# Map variables
map_variables = global_variables["map"]
floor_variables = map_variables["floor"]

floor_width = floor_variables["floor_width"]
floor_height = floor_variables["floor_height"]
floor_x = floor_variables["floor_x"]
floor_y = floor_variables["floor_y"]

# Map draw
map_background = pygame.Surface((player_width+10,player_height+10))

# Floor draw
floor_background = pygame.Surface((floor_width,floor_height))
floor_background.fill('Green')

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
        player_x = player_x - player_speed_x

    if keys[pygame.K_RIGHT]:
        player_x = player_x + player_speed_x

    # Draw world
    screen.blit(floor_background,(floor_x,window_height-floor_y))

    # Draw player
    screen.blit(player_background, (player_x-player_speed_x,window_height-player_y))
    screen.blit(player,(player_x,window_height-player_y))
    
    pygame.display.update()
    clock.tick(game_clk)