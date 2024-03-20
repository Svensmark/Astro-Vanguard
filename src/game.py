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


# Game init
pygame.init()
screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()


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
player_jumping = False
player_jump_flag = False
player_jump_maxed = False
player_max_jump = player_variables['player_max_jump']
player_looking_right = True
player_looking_left = False

# Player attack animation
player_attack = False
player_attacking = False
player_attack_frames = 20
player_attack_count = 0

# Player draw
 #player = pygame.Surface((player_width,player_height)) 
 #player.fill(player_color)
player_right = pygame.image.load('graphics/player_right.png').convert_alpha()
player_left = pygame.image.load('graphics/player_left.png').convert_alpha()

player_right_attack1 = pygame.image.load('graphics/player_right_attack1.png').convert_alpha()
player_right_attack2 = pygame.image.load('graphics/player_right_attack2.png').convert_alpha()

# Map
map_variables = global_variables["map"]
# Map background
 #background_variables = map_variables['background']
 #map_background_color = background_variables['background_color']


# Floor variables
floor_variables = map_variables["floor"]
floor_width = floor_variables["floor_width"]
floor_height = floor_variables["floor_height"]
floor_x = floor_variables["floor_x"]
floor_y = floor_variables["floor_y"]
floor_color = floor_variables['color']
# Map draw
map_background = pygame.image.load('graphics/background.png').convert_alpha()
# Floor draw
floor_background = pygame.Surface((floor_width,floor_height))
floor_background.fill(pygame.Color(7, 20, 7))




# Main loop
while True:
    screen.blit(map_background,(0,0))
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
        player_looking_left = True
        player_looking_right = False

    if keys[pygame.K_RIGHT]:
        player_x = player_x + player_speed_x
        player_looking_right = True
        player_looking_left = False

    if keys[pygame.K_UP]:
        player_jump_flag = True

    if keys[pygame.K_SPACE]:
        if (not player_attacking):
            player_attack = True

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
    if (player_looking_right):
        if (player_attack):
            if (not player_attacking):
                
                player_attacking = True
            else:
                player_attack_count += 1
                if (player_attack_count > player_attack_frames):
                    player_attack = False
                    player_attacking = False
                    player_attack_count = 0
                    player_height = player_variables['player_height']
                    player_width = player_variables['player_width']
                elif (player_attack_count < player_attack_frames/2):
                    player_height = 122
                    player_width = 76
                    screen.blit(player_right_attack1,(player_x,player_y))
                else:
                    player_height = 122
                    player_width = 63
                    screen.blit(player_right_attack2,(player_x,player_y))
        else:
            screen.blit(player_right,(player_x,player_y))
            
    elif (player_looking_left):
        screen.blit(player_left,(player_x,player_y))
    
    
    
    pygame.display.update()
    clock.tick(fps)
    
