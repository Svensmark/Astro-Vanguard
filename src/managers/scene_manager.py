import pygame
from scenes.death_scene import DeathScene
from scenes.game_scene import GameScene
from scenes.loadout_scene import LoadoutScene
from scenes.main_menu_scene import MainMenu
from scenes.scene import Scene
from utils.data import Data

class SceneManager:
    """
    Class for handling scenes
    """
    
    current_scene: Scene
    scenes: dict[Scene]
    
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event, data: Data):
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        self.data = data

        self.scenes = {
            "MainMenu": MainMenu(self.pygame_module, self.screen, self.data),
            "LoadoutScene": LoadoutScene(self.pygame_module, self.screen, self.data),
            "GameScene": GameScene(self.pygame_module, self.screen, self.data),
            "DeathScene": DeathScene(self.pygame_module, self.screen, self.data)
        }

        self.start_scene()
        
                
    def start_scene(self):
        self.set_scene('MainMenu')
        
                
    def set_scene(self, scene: str):        
        self.current_scene = self.scenes[scene]
        self.current_scene.on_load() 
        
        
    def update_current_scene(self, events: list[str]):
        next_scene_name = self.current_scene.update(events)
        if next_scene_name != self.current_scene.name:
            self.current_scene.fadeout() 
            self.current_scene.on_leave()
            self.set_scene(next_scene_name)   
            #self.current_scene.update(events)
            self.current_scene.fadein(events) 
            
