"""
Scene class
"""
import pygame

class Scene:
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event):
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
    
    def update(self):
        pass
    
    def render(self):
        pass
    
    def handle_events(self):
        pass
    
    