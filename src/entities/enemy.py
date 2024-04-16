"""
Module for Enemy class
"""
import pygame
from utils.json_reader import FileReader
from utils.asset_loader import sprite_loader, sound_loader
import math

class Enemy(pygame.Rect):
    """
    Class for Enemy extending pygame.Rect
    """
    def __init__(self, pygame: pygame, screen: pygame.surface, x: int, y: int, collision_sound: pygame.mixer.Sound):
        file_reader_game = FileReader()
        enemy_data = file_reader_game.read_json("enemy.json")

        super().__init__(x, y, enemy_data['width'], enemy_data['height'])
        self.pygame = pygame
        self.screen = screen
        self.collision_sound = sound_loader(collision_sound)
        self.x = x
        
        self.animation_list = []
        self.frame_index = 0
        for i in range(4):
            self.animation_list.append(sprite_loader(self.pygame, f'assets/enemyship_1/enemy_ship_1_{i+1}.png'))


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
        if (self.frame_index >= len(self.animation_list)):
            self.frame_index = 0
        else:
            self.frame_index += 0.1
        self.sprite = self.animation_list[math.floor(self.frame_index-1)]
        self.screen.blit(self.sprite, self)


    def update(self):
        """
        Method for updating enemy
        """
        self.move()
        self.draw()
