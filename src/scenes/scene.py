"""
Scene class
"""
import pygame

from utils.data import Data

class Scene:

    name: str

    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data
        
    def on_load(self):
        pass
    
    def on_leave(self):
        pass
    
    def update(self, events):
        pass
    
    def render(self):
        pass
    
    def handle_events(self):
        pass
    
    