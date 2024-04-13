import pygame
from sys import exit
import random

from controller.entity_controller import Spawner
from entities.enemy import Enemy
from entities.player import Player
from utils.background import Background
from ui.interface import Interface
from utils.data import Data
from menus.menu import get_main_menu


# Game data init
data = Data()
game_data = data.get_game_data()
player_data = data.get_player_data()
enemy_data = data.get_enemy_data()
spawner_data = data.get_spawner_data()


# Core game initialization
pygame.init()
game_running = True
screen = pygame.display.set_mode((game_data.screen_width, game_data.screen_height))
clock = pygame.time.Clock()
click = False


# Helper classes init
player = Player(pygame, screen, player_data)
spawner = Spawner(pygame, screen)
background = Background(pygame, screen)
interface = Interface(pygame, screen, player_data)


# Scenes
main_menu = get_main_menu(pygame, screen, background)
## TODO - Add scene for playing
# Scene selecter
scene_selecter = "Main"


# Main game loop
while True:

    mouse = pygame.mouse.get_pos()

    # Check for exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    match scene_selecter:
        case "Main":
            scene_selecter = main_menu.update(screen, mouse, click)
        case "Start":
            if game_running:
                # Draw the background
                background.draw()

                # Updates
                player.update(player_data, pygame.key.get_pressed(), game_data)
                spawner.update(game_data, player_data, enemy_data, spawner_data)
                interface.update(player_data, game_data)

                # Handle data to be removed
                for lazer in game_data.lazers:
                    lazer.update(game_data)

                # Check if game is over
                ## TODO - Add menu for death screen
                if player_data.current_hp == 0:
                    player.death.play()
                    game_running = False

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
