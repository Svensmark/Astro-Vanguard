import pygame
from scenes.scene import Scene


class GameScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface):
        super().__init__(pygame_module, screen)
        
    def update(self):
        return super().update()
    
    
        