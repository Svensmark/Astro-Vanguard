import pygame
from scenes.scene import Scene
from utils import asset_loader


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface):
        super().__init__(pygame_module, screen)
        
    def update(self):
        self.screen.blit(asset_loader.sprite_loader(self.pygame_module, 'assets/background.png'), (100,100))
        return "MainMenu"

    
        