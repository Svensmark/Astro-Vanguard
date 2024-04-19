import pygame
from scenes.scene import Scene


class GameScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event):
        super().__init__(pygame_module, screen, events)
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        
    def update(self):
        return super().update()
    
    
        