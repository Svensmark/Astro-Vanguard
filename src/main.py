"""
Main game file
"""
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, MOUSEBUTTONDOWN
# from pygame.constants import QUIT
# pylint: enable=no-name-in-module

from utils.data import Data
from utils.background import Background
from ui.interface import Interface
from controller.entity_controller import Spawner
from entities.player import Player
from menus.menu import get_main_menu


# Game data init
data = Data()
game_data = data.game_data
player_data = data.player_data
enemy_data = data.enemy_data
spawner_data = data.spawner_data
asset_data = data.asset_data

# Core game initialization
# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member
pygame.display.set_caption('Space Invaders')
screen = pygame.display.set_mode((game_data.screen_width, game_data.screen_height))
clock = pygame.time.Clock()
GAME_RUNNING = True
CLICK = False

# Helper classes init
player = Player(pygame, screen, player_data, asset_data)
spawner = Spawner(pygame, screen)
background = Background(pygame, screen)
interface = Interface(pygame, screen, player_data)


# Scenes
main_menu = get_main_menu(pygame, screen, background, asset_data)
## TODO - Add scene for playing
# Scene selector
SCENE_SELECTOR = "Main"

# Main game loop
while True:

    mouse = pygame.mouse.get_pos()

    # Check for exiting game
    for event in pygame.event.get():
        if event.type == QUIT:
            # pylint: disable=no-member
            pygame.quit()
            # pylint: enable=no-member
            exit()
        if event.type == MOUSEBUTTONDOWN:
            CLICK = True

    match SCENE_SELECTOR:
        case "Main":
            SCENE_SELECTOR = main_menu.update(mouse, CLICK)
        case "Start":
            if GAME_RUNNING:
                # Draw the background
                background.draw()

                # Updates
                player.update(player_data, pygame.key.get_pressed(), game_data)
                spawner.update(game_data, player_data, enemy_data, spawner_data, asset_data)
                interface.update(player_data, game_data)

                # Handle data to be removed
                for lazer in game_data.lazers:
                    lazer.update(game_data)

                # Check if game is over
                ## TODO - Add menu for death screen
                if player_data.current_hp == 0:
                    player.death.play()
                    GAME_RUNNING = False

            # If game is not running
            else:
                screen.fill("Red")
                font = pygame.font.Font(None, 36)
                hp_surface = font.render("Game Over!", True, "Black")
                text_rect = hp_surface.get_rect()
                text_rect.center = (
                    game_data.screen_width / 2,
                    game_data.screen_height / 2,
                )
                screen.blit(hp_surface, text_rect)

    # Update the game windows
    pygame.display.update()
    clock.tick(game_data.fps)
