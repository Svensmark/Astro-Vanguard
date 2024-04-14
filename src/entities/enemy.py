"""
Module for Enemy class
"""
from pygame import Rect
from utils.json_reader import FileReader
from utils.asset_loader import sprite_loader, sound_loader

class Enemy(Rect):
    """
    Class for Enemy extending pygame.Rect
    """
    def __init__(self, pygame, screen, x, y, asset, collision_sound):
        file_reader_game = FileReader()
        enemy_data = file_reader_game.read_json("enemy.json")

        super().__init__(x, y, enemy_data['width'], enemy_data['height'])
        self.pygame = pygame
        self.screen = screen
        self.collision_sound = sound_loader(collision_sound)
        self.sprite = sprite_loader(self.pygame, asset)
        self.x = x

    def move(self):
        """
        Method for moving enemy
        """
        self.x -= 5
        if self.x < 0:
            self.x = 800

    def draw(self):
        """
        Method for drawing enemy
        """
        self.screen.blit(self.sprite, self)

    def update(self):
        """
        Method for updating enemy
        """
        self.move()
        self.draw()
