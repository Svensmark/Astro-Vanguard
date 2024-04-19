import pygame
from entities.player import Player
from managers.entity_manager import Spawner
from scenes.scene import Scene
from ui.interface import Interface
from utils import asset_loader
from utils.background import Background
from utils.data import Data


class GameScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        super().__init__(pygame_module, screen, data)
        self.name = 'GameScene'
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data

        self.background = Background(self.pygame_module, self.screen)
        self.player = Player(pygame, screen, data.player_data, data.asset_data)
        self.spawner = Spawner(pygame, screen)
        self.interface = Interface(pygame, screen, data.player_data)
        
        self.music = asset_loader.sound_loader('assets/sounds/music/galactic_skirmish.ogg')
        
    def update(self, events):
        self.background.draw()

        # Updates
        self.player.update(self.data.player_data, self.pygame_module.key.get_pressed(), self.data.game_data)
        self.spawner.update(self.data.game_data, self.data.player_data, self.data.enemy_data, self.data.spawner_data, self.data.asset_data)
        self.interface.update(self.data.player_data, self.data.game_data)

        # Handle data to be removed
        for lazer in self.data.game_data.lazers:
            lazer.update(self.data.game_data)

        # Check if game is over
        if self.data.player_data.current_hp == 0:
            self.player.death.play()
            return 'MainMenu'
        
        return self.name
    
    def on_load(self):
        self.music.play(loops=10, fade_ms=4000)
    
    def on_leave(self):
        self.music.fadeout(2000)
    
        