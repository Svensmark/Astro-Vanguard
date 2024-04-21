"""
Module for Lazer class
"""
import pygame
from utils.json_reader import FileReader
from utils.asset_loader import sprite_loader
from utils.data import GameData


# create a lazer class extending pygame.Rect
class Lazer(pygame.Rect):
    """
    Class for spawning and updating lazer
    """
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, x: int, y: int):
        self.pygame_module = pygame_module
        self.screen = screen
        self.x = x

        file_reader_game = FileReader()
        lazer_data = file_reader_game.read_json("lazer.json")
        self.sprite = sprite_loader(self.pygame_module, 'assets/lazer_bolt.png')

        super().__init__(x, y, lazer_data['width'], lazer_data['height'])


    def move(self, game_data: GameData):
        """
        Method for moving the lazer
        """
        self.x += 5

        if self.x > self.screen.get_width()+100:
            game_data.lazers.remove(self)

    def draw(self):
        """
        Method for drawing the lazer
        """
        self.screen.blit(self.sprite, self)

    def handle_collision(self, game_data: GameData):
        """
        Method for handling collision
        """
        for enemy in game_data.enemies:
            if self.colliderect(enemy):
                game_data.lazers.remove(self)
                game_data.enemies.remove(enemy)
                enemy.collision_sound.play()
                game_data.score += 10

    def update(self, game_data: GameData):
        """
        Method for updating lazer
        """
        self.move(game_data)
        self.draw()
        self.handle_collision(game_data)
        
