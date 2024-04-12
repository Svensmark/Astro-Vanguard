import pygame
from sys import exit
import random

from enemy import Enemy
from player import Player
from background import Background

# Game variables
screen_width = 800
screen_height = 450

player_width = 50
player_height = 35

player_shoot_cooldown = 0
enemy_spawn_rate = 0

lazer_width = 35
lazer_height = 5

player_x = 100
player_y = 100

max_hp = 100
current_hp = max_hp

score = 0

lazers = []
enemies = []

game_running = True

# Core game initialization
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
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

        # Draw the player
        player.update(pygame.key.get_pressed(), lazers)

        # Draw the interface
        font = pygame.font.Font(None, 36) 
        hp_surface = font.render('HP: ' + str(current_hp), True, 'White')
        point_surface = font.render('Points: ' + str(score), True, 'White')
        screen.blit(hp_surface, (20, 20))
        screen.blit(point_surface, (20, 45))


        # Handle the enemies
        if enemy_spawn_rate == 0:
            enemy_y = random.randint(30, screen_height-player_height-30)
            enemy = Enemy(pygame, screen, screen_width, enemy_y, player_width, player_height)
            enemies.append(enemy)
            enemy_spawn_rate = 60

        elif enemy_spawn_rate != 0:
            enemy_spawn_rate -= 1   

        # Handle the lazers
        enemies_to_be_removed = []
        lazers_to_be_removed = []
        for lazer in lazers:
            score = lazer.update(lazers_to_be_removed, enemies, score)

        for lazer_tbr in lazers_to_be_removed:
            lazers.remove(lazer_tbr)

        for enemy in enemies:
            current_hp = enemy.update(current_hp, enemies_to_be_removed)
        
        for enemy in enemies_to_be_removed:
            enemies.remove(enemy)

        if current_hp == 0:
            game_running = False

    else:
        screen.fill('Red')
        font = pygame.font.Font(None, 36) 
        hp_surface = font.render('Game Over!', True, 'Black')
        text_rect = hp_surface.get_rect()
        text_rect.center = (screen_width/2, screen_height/2)
        screen.blit(hp_surface, text_rect)

    # Update the game window
    pygame.display.update()
    clock.tick(60)


