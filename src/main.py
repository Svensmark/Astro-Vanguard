import pygame
from sys import exit
import random

from controller.spawner import Spawner
from entities.enemy import Enemy
from entities.player import Player
from utils.background import Background
from utils.data import Data

# Game data init
data = Data()
game_data = data.get_game_data()
player_data = data.get_player_data()
enemy_data = data.get_enemy_data()
spawner_data = data.get_spawner_data()

# Core game initialization
pygame.init()
screen = pygame.display.set_mode((game_data.screen_width, game_data.screen_height))
clock = pygame.time.Clock()

game_running = True

player = Player(pygame, screen, player_data)
spawner = Spawner(pygame, screen)
background = Background(pygame, screen)

# Main game loop
while True:

    # Check for exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_running:
        # Draw the background
        background.draw()

        # Data to be removed
        enemies_to_be_removed = []
        lazers_to_be_removed = []


        # Updates
        player.update(player_data, pygame.key.get_pressed(), game_data, enemies_to_be_removed)
        spawner.update(game_data, player_data, enemy_data)


        # Draw the interface
        font = pygame.font.Font(None, 36) 
        hp_surface = font.render('HP: ' + str(player_data.current_hp), True, 'White')
        point_surface = font.render('Points: ' + str(game_data.score), True, 'White')
        screen.blit(hp_surface, (20, 20))
        screen.blit(point_surface, (20, 45))


        # Handle data to be removed
        for lazer in game_data.lazers:
            lazer.update(lazers_to_be_removed, game_data)

        new_lazers = [lazer for lazer in game_data.lazers if lazer not in lazers_to_be_removed]
        game_data.lazers = new_lazers


        # Handle enemies to be removed
        for enemy in game_data.enemies:
            enemy.update(enemies_to_be_removed)
        
        for enemy in enemies_to_be_removed:
            game_data.enemies.remove(enemy)

        if player_data.current_hp == 0:
            game_running = False


    # If game is not running
    else:
        screen.fill("Red")
        font = pygame.font.Font(None, 36)
        hp_surface = font.render("Game Over!", True, "Black")
        text_rect = hp_surface.get_rect()
        text_rect.center = (game_data.screen_width/2, game_data.screen_height/2)
        screen.blit(hp_surface, text_rect)


    # Update the game window
    pygame.display.update()
    clock.tick(game_data.fps)


