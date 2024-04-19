import pygame
from scenes.game_scene import GameScene
from scenes.main_menu_scene import MainMenu
from scenes.scene import Scene

class SceneManager:
    """
    Class for handling scenes
    """
    
    current_scene: Scene
    scenes: dict[Scene]
    
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, events: pygame.event):
        self.pygame_module = pygame_module
        self.screen = screen
        self.events = events
        
        
    def init_scenes(self):
        self.scenes = {
            "MainMenu": MainMenu(self.pygame_module, self.screen, self.events),
            "GameScene": GameScene(self.pygame_module, self.screen, self.events)
        }
        self.set_scene('MainMenu')
        
                
    def set_scene(self, scene: str):
        self.current_scene = self.scenes[scene]
        
        
    def update_current_scene(self):
        if self.current_scene:
            self.current_scene.update()
            
