import pygame
from game.grid import Grid
from game.tile import Tile
from utils.json_reader import File_reader

#Todo - Fjern dette - ryk eventuelt over i en level klasse

# Read JSON
fr = File_reader()
levels = fr.read_json('json/maps.json')


class Play():
    def __init__(self, pygame: pygame, screen: pygame.Surface):
        self.pygame = pygame
        self.screen = screen

        self.grid = Grid(pygame, screen, levels['level1'], 'stone_tiles')


    def update(self, screen: pygame.surface, mouse: tuple[int,int], click: bool):
        self.grid.blit_grid(mouse)
        return 'play'