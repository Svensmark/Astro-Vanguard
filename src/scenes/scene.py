"""
Scene class
"""
import pygame

class Scene:
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, object):
        self.pygame_module = pygame_module
        self.screen = screen
    
    def update(self):
        pass