import pygame
from scenes.scene import Scene
from utils.background import Background
from utils.data import Data


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event, data: Data):
        super().__init__(pygame_module, screen, events, data)
        self.name = 'MainMenu'
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        self.data = data
        
        self.background = Background(self.pygame_module, self.screen)
        
    def update(self):
        self.background.draw_static()
        return self.name

    
        