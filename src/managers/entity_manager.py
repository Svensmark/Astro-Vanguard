"""
Module for Spawner class
"""
import random
from entities.enemy import Enemy

## TODO - Rename to SpawnerController
class Spawner:
    """
    Class for spawning and updating enemies
    """
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    ## TODO - Change functionality cleanup
    def spawn_enemy(self, game_data, player_data, enemy_data, spawner_data, asset_data):
        """
        Method for spawning enemy
        """
        if enemy_data.spawn_rate == 0:
            enemy_y = random.randint(30, game_data.screen_height-player_data.height-30)
            random_ship_img = spawner_data.enemy_ships[random.randint(0, len(spawner_data.enemy_ships))-1]
            enemy = Enemy(self.pygame, self.screen, game_data.screen_width, enemy_y, asset_data.sounds.enemy_death)
            game_data.enemies.append(enemy)
            enemy_data.spawn_rate = 60
        elif enemy_data.spawn_rate != 0:
            enemy_data.spawn_rate -= 1

    @staticmethod
    def handle_update_enemy(game_data):
        """
        Method for updating enemy
        """
        for enemy in game_data.enemies:
            enemy.update()

    def update(self, game_data, player_data, enemy_data, spawner_data, asset_data):
        """
        Method for updating game data
        """
        self.handle_update_enemy(game_data)
        self.spawn_enemy(game_data, player_data, enemy_data, spawner_data, asset_data)
