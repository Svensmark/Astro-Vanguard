import pygame
from pygame import mixer

def sprite_loader(pygame: pygame, asset: str):
    return pygame.image.load(asset).convert_alpha()

def sound_loader(asset):
    print(asset)
    return mixer.Sound(asset)