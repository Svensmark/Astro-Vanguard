"""
Module for Button class
"""
from typing import Callable
import pygame
from pygame.mixer import Sound

from utils.asset_loader import sound_loader
from utils.data import AssetData, Data

COLOR = (255, 255, 255)  # white
COLOR_LIGHT = (170, 170, 170)
COLOR_DARK = (100, 100, 100)  # dark shade of the button

class Button(pygame.sprite.Sprite):
    """
    Class for Button extending pygame.sprite.Sprite
    """
    def __init__(self, screen: pygame.Surface, btn_image: pygame.Surface,
                x: int, y: int, text: str, function: Callable, data: Data):
        super().__init__()

        self.hover_sound = sound_loader(data.asset_data.sounds.menu_hover)
        self.click_sound = sound_loader(data.asset_data.sounds.menu_select)

        self.screen = screen
        self.x = x
        self.y = y
        self.btn_img = btn_image
        self.color = "Black"
        self.text = text
        self.hovering = False
        self.image = self.btn_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.function = function

    def hover(self, mouse: tuple[int, int]) -> bool:
        """
        Method to check if mouse is hovering over the button
        """
        return (self.x
                <= mouse[0]
                <= self.x + self.rect.width and self.y
                <= mouse[1]
                <= self.y + self.rect.height)

    def set_hover(self, sound: Sound):
        """
        Method to set hover state
        """
        if not self.hovering:
            self.color = "Red"
            self.hovering = True
            # put this out in own method
            if self.hovering:
                sound.play()

    def play_click_sound(self):
        self.click_sound.play()

    def set_not_hover(self):
        """
        Method to unset hover state
        """
        self.color = "Black"
        self.hovering = False

    def draw_text(self):
        """
        Method to draw text on the button
        """
        font_size = 45
        if len(self.text) >= 8:
            font_size = 35
        font = pygame.font.Font(None, font_size)
        img = font.render(self.text, True, self.color)
        self.screen.blit(img,
                        (self.rect.centerx - (img.get_width() / 2),
                        self.rect.centery - (img.get_height() / 2)))
