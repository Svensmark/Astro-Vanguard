import pygame
from sys import exit
import json
from pathlib import Path
from physics import *


# Read variables json
script_location = Path(__file__).absolute().parent
file_location = script_location / 'global.json'
f = open(file_location, 'r')
global_variables = json.load(f)


# Default settings
game_settings = global_variables['game_settings']
window_height = game_settings['window_height']
window_width = game_settings['window_width']
fps = game_settings['fps']


# World settings
world_settings = global_variables['world_settings']
gravity = world_settings['gravity']


# Player
player_variables = global_variables['player']
player_width = player_variables['player_width']
player_height = player_variables['player_height']
player_x = player_variables['player_x']
player_y = player_variables['player_y']
player_speed_x = player_variables['player_speed_x']
player_speed_y = player_variables['player_speed_y']
player_color = player_variables['color']
player_bg_color = player_variables['background_color']
player_jumping = False
player_jump_flag = False
player_jump_maxed = False
player_max_jump = player_variables['player_max_jump']

player_previous_x = 0
player_previous_y = 0

# Player draw
player = pygame.Surface((player_width,player_height))
player_shadow = pygame.Surface((player_width,player_height))
player.fill(player_color)
player_shadow.fill(player_bg_color)
player_background = pygame.Surface((player_width+10,player_height+10))
player_background.fill(player_bg_color)


# Map variables
map_variables = global_variables["map"]
# Floor variables
floor_variables = map_variables["floor"]
floor_width = floor_variables["floor_width"]
floor_height = floor_variables["floor_height"]
floor_x = floor_variables["floor_x"]
floor_y = floor_variables["floor_y"]
floor_color = floor_variables['color']


# Floor draw
floor_background = pygame.Surface((floor_width,floor_height))
floor_background.fill(floor_color)


# Game init
pygame.init()
screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()


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

    if keys[pygame.K_SPACE]:
        player_jump_flag = True

    if (player_jump_flag):
        if not player_jumping:
            player_jumping = True

        else:
            if not player_jump_maxed:
                player_y = handle_jumping(player_y)
            
            if player_y < player_max_jump:
                player_jump_maxed = True

            if (player_y == window_height-floor_y-player_height):
                player_jumping = False
                player_jump_flag = False
                player_jump_maxed = False

    player_y = handle_gravity(gravity, player_y, window_height-floor_y-player_height)

    # Draw world
    screen.blit(floor_background,(floor_x,window_height-floor_y))

    # Draw player
    screen.blit(player_shadow,(player_previous_x, player_previous_y))
    player_previous_x = player_x
    player_previous_y = player_y
    screen.blit(player,(player_x,player_y))
    
    
    pygame.display.update()
    clock.tick(fps)
    
