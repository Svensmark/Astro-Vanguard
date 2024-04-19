import pygame
from scenes.scene import Scene
from utils.background import Background


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event):
        super().__init__(pygame_module, screen, events)
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        
        self.background = Background(self.pygame_module, self.screen)
        
    def update(self):
        self.background.draw_static()

    
        