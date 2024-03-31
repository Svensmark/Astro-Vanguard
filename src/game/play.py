import pygame
from game.grid import Grid
from game.tile import Tile
from utils.json_reader import File_reader


class Play():
    def __init__(self, pygame: pygame, screen: pygame.Surface):
        self.pygame = pygame
        self.screen = screen

        fr = File_reader()
        self.levels = fr.read_json('json/maps.json')

        self.grid = Grid(pygame, screen, self.levels['level1'], 'stone_tiles')


    def update(self, screen: pygame.surface, mouse: tuple[int,int], click: bool):
        self.grid.blit_grid(screen,mouse,click)
        self.grid.handle_player_movement()
        self.grid.blit_player()
        return 'play'