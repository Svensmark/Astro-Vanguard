from scene import Scene
import pygame

class Main_Menu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface):
        super().__init__(pygame_module, screen)
        