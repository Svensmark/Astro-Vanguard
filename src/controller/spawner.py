

import random

from entities.enemy import Enemy


class Spawner():
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    def spawn_enemy(self, game_data, player_data, enemy_data):
        if enemy_data.spawn_rate == 0:
            enemy_y = random.randint(30, game_data.screen_height-player_data.height-30)
            enemy = Enemy(self.pygame, self.screen, game_data.screen_width, enemy_y)
            game_data.add_enemy(enemy)
            enemy_data.spawn_rate = 60

        elif enemy_data.spawn_rate != 0:
            enemy_data.spawn_rate -= 1   

    def update(self, game_data, player_data, enemy_data):
        self.spawn_enemy(game_data, player_data, enemy_data)