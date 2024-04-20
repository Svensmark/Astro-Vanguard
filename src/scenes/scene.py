"""
Scene class
"""
import pygame

from utils.data import Data

class Scene:

    name: str
    fading: bool

    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data
        
    def on_load(self):
        pass
    
    def on_leave(self):
        pass
    
    def update(self):
        pass
    
    def render(self):
        pass
    
    def handle_events(self):
        pass
    
    def fadein(self, events):
        veil = self.pygame_module.Surface((self.screen.get_width(), self.screen.get_height()))
        for i in range(255):
            self.render()
            veil.fill((0, 0, 0))  
            veil.set_alpha(255 - i)
            self.screen.blit(veil, (0, 0))
            self.pygame_module.display.flip()  # Update the display
            self.pygame_module.time.delay(5)  # Delay for smoother effect

    def fadeout(self):
        veil = self.pygame_module.Surface((self.screen.get_width(), self.screen.get_height()))
        for i in range(100):
            veil.fill((0, 0, 0))  
            veil.set_alpha(i)
            self.screen.blit(veil, (0, 0))
            self.pygame_module.display.flip()  # Update the display
            self.pygame_module.time.delay(5)  # Delay for smoother effect
