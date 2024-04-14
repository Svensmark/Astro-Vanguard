"""
Module for Interface class
"""
import pygame

class Interface:
    """
    Class for Interface
    """
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, player_data):
        self.pygame = pygame_module
        self.screen = screen
        self.hp_bar = self.pygame.Rect(20, 20, player_data.current_hp, 20)
        self.hp_bar_background = self.pygame.Rect(18, 18, player_data.current_hp + 4, 24)

    def update_hp(self, player_data):
        """
        Update the HP bar
        """
        self.hp_bar.update(
            self.hp_bar.left,
            self.hp_bar.top,
            player_data.current_hp,
            self.hp_bar.height,
        )

    def draw_ui(self, game_data):
        """
        Draw the UI
        """
        font = self.pygame.font.Font(None, 36)
        point_surface = font.render(f"Points: {game_data.score}", True, (255, 255, 255))
        self.pygame.draw.rect(self.screen, (255, 255, 255), self.hp_bar_background)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hp_bar)
        self.screen.blit(point_surface, (20, 45))

    def update(self, player_data, game_data):
        """
        Update the interface
        """
        self.update_hp(player_data)
        self.draw_ui(game_data)
