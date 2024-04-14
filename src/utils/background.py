"""
Module for Background class
"""
import pygame

class Background:
    """
    Class for Background
    """
    def __init__(self, pygame_module: pygame, screen: pygame.Surface):
        self.pygame = pygame_module
        self.screen = screen
        self.bg_1 = self.load_scaled_image('assets/background.png')
        self.bg_2 = self.load_scaled_image('assets/background.png')
        self.bg_1_x = 0
        self.bg_2_x = self.screen.get_width()

    def load_scaled_image(self, image_path: str) -> pygame.Surface:
        """
        Load an image and scale it to the screen size
        """
        image = self.pygame.image.load(image_path).convert_alpha()
        return self.pygame.transform.scale(image, (self.screen.get_width(), self.screen.get_height()))

    def draw_static(self):
        """
        Draw a static background
        """
        self.screen.fill('White')
        self.screen.blit(self.bg_1, (self.bg_1_x, 0))

    def draw(self):
        """
        Draw a moving background
        """
        self.screen.fill('White')
        self.screen.blit(self.bg_1, (self.bg_1_x, 0))
        self.screen.blit(self.bg_2, (self.bg_2_x, 0))
        self.bg_1_x -= 2
        self.bg_2_x -= 2

        if self.bg_1_x < -self.screen.get_width():
            self.bg_1_x = self.screen.get_width() - 2

        elif self.bg_2_x < -self.screen.get_width():
            self.bg_2_x = self.screen.get_width() - 2
