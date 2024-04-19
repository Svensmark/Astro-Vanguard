import pygame
from entities.player import Player
from managers.entity_manager import Spawner
from scenes.scene import Scene
from ui.interface import Interface
from utils.background import Background
from utils.data import Data


class DeathScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event, data: Data):
        super().__init__(pygame_module, screen, events, data)
        self.name = 'DeathScene'
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        self.data = data

        self.background = Background(self.pygame_module, self.screen)
        self.player = Player(pygame, screen, data.player_data, data.asset_data)
        self.spawner = Spawner(pygame, screen)
        self.interface = Interface(pygame, screen, data.player_data)
        
    def update(self):
        self.screen.fill("Red")
        font = pygame.font.Font(None, 36)
        hp_surface = font.render("Game Over!", True, "Black")
        text_rect = hp_surface.get_rect()
        text_rect.center = (
        self.data.game_data.screen_width / 2,
        self.data.game_data.screen_height / 2,
        )
        self.screen.blit(hp_surface, text_rect)
        
        return self.name
    
    
        