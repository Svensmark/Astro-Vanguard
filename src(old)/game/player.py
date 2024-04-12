import pygame
from game.tile import Tile
import random
from utils.json_reader import File_reader

fr = File_reader()
tiles = fr.read_json('json/tiles.json')

class Player():
    def __init__(self, pygame: pygame, screen: pygame.Surface):
        # Initialize
        self.pygame = pygame
        self.screen = screen

         
    # TODO - lav det bedre
    def blit_player(self,x,y):
        color = (255,0,0)
        rect = pygame.Rect(x,y,20,60)
        rect.centerx = x+30
        rect.centery = y-10
        
        pygame.draw.rect(self.screen, color, rect)