import pygame
from game import tile


class Grid():
    def __init__(self, pygame: pygame, screen: pygame.Surface, grid_matrix: list[list], tile: tile):
        # Initialize
        self.pygame = pygame
        self.screen = screen
        #self.tile = pygame.image.load('graphics/tile.png').convert_alpha()
        self.grid_matrix = grid_matrix
        self.tiles = []
        
        for height_i in range(len(self.grid_matrix)):
            for width_j in range(len(self.grid_matrix[height_i])):
                tile_tba = tile
                self.tiles.append(tile_tba)
                #self.tiles.append(pygame.image.load('graphics/tile.png').convert_alpha())
        
        #TODO Implement tile as class and parameter in grid init
        #self.tile = pygame.image.load('graphics/tile.png').convert_alpha()
        
    def blit_grid(self, mouse: tuple[int, int]):
        self.screen.fill('Black')
        
        hovered_tiles = []  # Store tiles that are hovered over
        tile_positions = []  # Store positions of tiles that are hovered over for later comparison
        
        # Adjusted to work with a flat list of tiles
        count = 0
        for x in range(len(self.grid_matrix)):
            for y in range(len(self.grid_matrix[x])):
                if self.grid_matrix[x][y] == 0:
                    continue
                    
                current_tile = self.tiles[count]
                is_hovered = current_tile.hover(mouse, [x, y], len(self.grid_matrix[x]))
                
                # Always blit the tile, but record it if it's being hovered over
                current_tile.blit(self.screen, x, y, len(self.grid_matrix[x]), False)
                
                if is_hovered:
                    hovered_tiles.append((current_tile, count))  # Store the tile and its index
                    tile_positions.append((x, y))
                
                count += 1  # Increment count to access the next tile in the flat list
        
        # Determine the topmost hovered tile
        if hovered_tiles:
            topmost_tile_position = max(tile_positions, key=lambda position: (position[1], position[0]))
            topmost_tile_index = tile_positions.index(topmost_tile_position)
            topmost_tile, _ = hovered_tiles[topmost_tile_index]
            
            # Now, re-blit only the topmost hovered tile with the hover effect
            x, y = topmost_tile_position
            topmost_tile.blit(self.screen, x, y, len(self.grid_matrix[x]), True)


        
        return 'play'