import pygame
from typing import Callable
from pygame.mixer import Sound

color = (255,255,255)  # white
color_light = (170,170,170)
color_dark = (100,100,100)  # dark shade of the button

class Button(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, btn_image: pygame.Surface, x: int, y: int, text: str, function: Callable):
        super().__init__()
        self.screen = screen

        self.x = x
        self.y = y
        self.btn_img = btn_image
        self.color = "Black"
        self.text = text

        self.hovering = False

        self.image = self.btn_img
        self.rect = self.image.get_rect(topleft = (x,y))
        self.function = function


    def hover(self, mouse: tuple[int,int]):
        return self.x <= mouse[0] <= self.x + self.rect.width and self.y <= mouse[1] <= self.y + self.rect.height

    def set_hover(self, sound: Sound):
        if (not self.hovering):
            self.color = "Red"
            self.hovering = True
            if (self.hovering):
                sound.play()

    def set_not_hover(self):
        self.color = "Black"
        self.hovering = False

    def draw_text(self):
        font_size = 45
        if (len(self.text) >= 8):
            font_size = 35
        font = pygame.font.Font(None, font_size)
        img = font.render(self.text, True, self.color)
        self.screen.blit(img, (self.rect.centerx-(img.get_width()/2), self.rect.centery-(img.get_height()/2)))