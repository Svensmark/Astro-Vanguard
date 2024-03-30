import pygame
from sys import exit
from menus import menu
from menus import button_module
from game.grid import Grid
from game.tile import Tile
from pathlib import Path
from utils.json_reader import File_reader
import json


# Core game initialization
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
click = False

# Read JSON
map_reader = File_reader('json/maps.json')
#Todo - lav om
levels = map_reader.read_json()

# Menus
main_menu = menu.get_main_menu(pygame, screen)
start_menu = menu.get_start_menu(pygame, screen)


#Todo - Fjern dette - ryk eventuelt over i en level klasse
test_tile = Tile(pygame, screen, 'graphics/tile_1.png', 'graphics/tile_hover.png', 1.45)
test_grid = Grid(pygame, screen, levels['level1'], test_tile)


# Scene selecter
scene_selecter = "main_menu"


# Main game loop
while True:
    mouse = pygame.mouse.get_pos()
    
    # Get input event - (Mouse/Keyboard input etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    
    # Scene selecter - Draws either a menu or game depending on gamestate/scene
    match scene_selecter:
        case "main_menu":
            scene_selecter = main_menu.draw_menu(screen, mouse, click)
        case "start":
            scene_selecter = start_menu.draw_menu(screen, mouse, click)
        case "play":
            #pygame.mouse.set_visible(0)
            scene_selecter = test_grid.blit_grid(mouse)
            
            
    click = False
    pygame.display.update()
    clock.tick(120)