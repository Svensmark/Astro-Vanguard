import pygame
from game.tile import Tile
from game.player import Player
import random
from utils.json_reader import File_reader

fr = File_reader()
tiles = fr.read_json('json/tiles.json')

class Grid():
    def __init__(self, pygame: pygame, screen: pygame.Surface, grid_matrix: list[list], tile_type: str, ):
        # Initialize
        self.pygame = pygame
        self.screen = screen
        self.grid_matrix = grid_matrix
        
        # Initiate player
        self.player = Player(pygame, screen)
        self.player_x = 0
        self.player_y = 0
        self.player_destination_x = 0
        self.player_destination_y = 0
        

        # Initiate each tile in the grid
        self.tiles = []
        self.hovered_tile = None
        for x in range(len(self.grid_matrix)):
            for y in range(len(self.grid_matrix[x])):
                tile = Tile(pygame, screen, 'graphics/'+random.choice(tiles[tile_type]), 'graphics/tile_hover.png', 1.45, x, y)
                self.tiles.append(tile)

        
    def blit_grid(self, screen: pygame.Surface, mouse: tuple[int, int], click: bool):
        self.screen.fill('Black')        
        
        hovered_tiles = []
        tile_positions = []
        
        count = 0
        for tile in self.tiles:            
            tile.blit(self.screen, tile.x, tile.y, len(self.grid_matrix[tile.x]), False) 
            is_hovered = tile.hover(mouse, [tile.x, tile.y], len(self.grid_matrix[tile.x]))  
            
            if click and is_hovered:
                hovered_tiles.append((tile, count))
                tile_positions.append((tile.x, tile.y))
        
        if hovered_tiles:
            topmost_tile_position = max(tile_positions, key=lambda position: (position[1], position[0]))
            topmost_tile_index = tile_positions.index(topmost_tile_position)
            topmost_tile, _ = hovered_tiles[topmost_tile_index]
            
            x, y = topmost_tile_position
            self.player_destination_x = topmost_tile.calculate_isometric_x(x,y,len(self.grid_matrix[x]))
            self.player_destination_y = topmost_tile.calculate_isometric_y(x,y)
            
            topmost_tile.blit(self.screen, x, y, len(self.grid_matrix[x]), True)
    
    # FIX
    def handle_player_movement(self):
        if self.player_x < self.player_destination_x:
            self.player_x += 3
        else:
            self.player_x -= 3
            
        if self.player_y < self.player_destination_y:
            self.player_y += 3
        else:
            self.player_y -= 3
    
    
    def blit_player(self):
        self.player.blit_player(self.player_x, self.player_y)
