import pygame
from sys import exit
import random

from entities.enemy import Enemy
from entities.player import Player
from utils.background import Background
from utils.json_reader import File_reader

# Game variables
file_reader_game = File_reader()

# Game data init
game_data = file_reader_game.read_json("game.json")
screen_width = game_data["screen_width"]
screen_height = game_data["screen_height"]
score = 0
lazers = []
enemies = []

# Player data init
player_data = file_reader_game.read_json("player.json")
player_width = player_data["width"]
player_height = player_data["height"]
player_shoot_cooldown = player_data["shoot_cooldown"]
current_shoot_cooldown = 0
player_x = player_data["start_x"]
player_y = player_data["start_y"]
max_hp = player_data["max_hp"]
current_hp = max_hp

# Enemy data init
enemy_spawn_rate = 0

# Lazer data init
lazer_width = 35
lazer_height = 5


game_running = True

# Core game initialization
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(pygame, screen, player_x, player_y, player_width, player_height)
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

        # Handle enemies
        enemies_to_be_removed = []

        # Draw the player
        current_hp = player.update(
            pygame.key.get_pressed(), lazers, enemies, enemies_to_be_removed, current_hp
        )

        # Draw the interface
        font = pygame.font.Font(None, 36)
        hp_surface = font.render("HP: " + str(current_hp), True, "White")
        point_surface = font.render("Points: " + str(score), True, "White")
        screen.blit(hp_surface, (20, 20))
        screen.blit(point_surface, (20, 45))

        # Handle the enemies
        if enemy_spawn_rate == 0:
            enemy_y = random.randint(30, screen_height - player_height - 30)
            enemy = Enemy(
                pygame, screen, screen_width, enemy_y, player_width, player_height
            )
            enemies.append(enemy)
            enemy_spawn_rate = 60

        elif enemy_spawn_rate != 0:
            enemy_spawn_rate -= 1

        # Handle the lazers
        lazers_to_be_removed = []

        for lazer in lazers:
            score = lazer.update(lazers_to_be_removed, enemies, score)

        # Handle lazers to be removed
        new_lazers = [lazer for lazer in lazers if lazer not in lazers_to_be_removed]
        lazers = new_lazers

        for enemy in enemies:
            current_hp = enemy.update(current_hp, enemies_to_be_removed)

        for enemy in enemies_to_be_removed:
            enemies.remove(enemy)

        if current_hp == 0:
            game_running = False

    else:
        screen.fill("Red")
        font = pygame.font.Font(None, 36)
        hp_surface = font.render("Game Over!", True, "Black")
        text_rect = hp_surface.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)
        screen.blit(hp_surface, text_rect)

    # Update the game window
    pygame.display.update()
    clock.tick(60)
