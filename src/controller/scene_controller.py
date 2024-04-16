import pygame

class SceneController:
    """
    Class for handling scenes
    """
    def __init__(self, pygame: pygame, screen: pygame.surface):
        self.pygame = pygame
        self.screen = screen