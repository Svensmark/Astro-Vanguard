import pygame
from scenes.scene import Scene
from utils import asset_loader


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event):
        super().__init__(pygame_module, screen, events)
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        
    def update(self):
        self.screen.blit(asset_loader.sprite_loader(self.pygame_module, 'assets/background.png'), (100,100))
        return "MainMenu"

    
        