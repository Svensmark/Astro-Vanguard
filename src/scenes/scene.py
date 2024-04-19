"""
Scene class
"""
import pygame

from utils.data import Data

class Scene:

    name: str

    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event, data: Data):
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        self.data = data
    
    def update(self):
        pass
    
    def render(self):
        pass
    
    def handle_events(self):
        pass
    
    