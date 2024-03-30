import pygame
from utils.json_reader import File_reader


class Tile():
    def __init__(self, pygame: pygame, screen: pygame.Surface, img_path: str, img_hover_path: str, distortion_factor: float):
        # Initialize
        self.pygame = pygame
        self.screen = screen

        
        self.image = self.pygame.image.load(img_path).convert_alpha()
        self.image_hover = self.pygame.image.load(img_hover_path).convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_hover = pygame.mask.from_surface(self.image_hover)
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.distortion_factor = distortion_factor
        
    
    # Calculating isometric coordinates
    def calculate_isometric_x(self, x: int, y: int, grid_length: int):
        return x * 0.5 * self.width + y * (- 0.5) * self.width - self.width/2 + (grid_length / 2) * self.width
    
    def calculate_isometric_y(self, x: int, y: int):
        return x * 0.25 * self.height * self.distortion_factor + y * 0.25 * self.height * self.distortion_factor
          
    
    def blit(self, screen: pygame.Surface, x: int, y: int, grid_length: int, hover: bool):
        if hover:
            screen.blit(self.image_hover, (self.calculate_isometric_x(x, y, grid_length), self.calculate_isometric_y(x, y)))
        else:
            screen.blit(self.image, (self.calculate_isometric_x(x, y, grid_length), self.calculate_isometric_y(x, y)))


    def hover(self, mouse_pos: tuple[int, int], tile_pos: tuple[int, int], grid_length: int) -> bool:
            # Calculate the absolute screen position of the tile based on its grid position
            # `tile_pos` is a tuple of the form (x, y) representing the tile's position in the grid
            tile_screen_x, tile_screen_y = self.calculate_isometric_x(*tile_pos, grid_length), self.calculate_isometric_y(*tile_pos)

            # Create a mask for the mouse pointer. Since the mouse is effectively a single point,
            # we create a 1x1 mask.
            mouse_mask = pygame.mask.Mask((1, 1), fill=True)
            
            # Calculate the offset between the mouse mask and the tile mask.
            # This is the difference between the mouse position and the top-left corner of the tile.
            offset_x = int(mouse_pos[0] - tile_screen_x)
            offset_y = int(mouse_pos[1] - tile_screen_y)
            
            # Check if there is a collision between the mouse mask and the tile's mask at the calculated offset.
            # This indicates the mouse is over a solid part of the tile.
            return self.mask.overlap(mouse_mask, (offset_x, offset_y)) is not None

        # Your existing methods for calculating isometric positions...