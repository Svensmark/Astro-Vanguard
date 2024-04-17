import pygame
from scenes.scene import Scene

class SceneController:
    """
    Class for handling scenes
    """
    
    current_scene: Scene
    
    def __init__(self):
        pass
                
    def set_scene(self, scene: Scene):
        self.current_scene = scene
        
    def update_current_scene(self):
        if self.current_scene:
            self.current_scene.update()