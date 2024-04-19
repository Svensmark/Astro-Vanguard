"""
Module for Menu class and related functions
"""
import sys
import pygame
from ui import button_module
from utils.asset_loader import sprite_loader, sound_loader
from utils.background import Background
from utils.data import AssetData

class Menu:
    """
    Class for Menu
    """
    
    hover_sound: pygame.mixer.Sound

    def __init__(self, pygame_module: pygame, screen: pygame.Surface, buttons: list[button_module.Button], menu_name: str, background: Background, asset_data: AssetData):
        self.pygame = pygame_module
        self.screen = screen
        self.buttons = buttons
        self.button_sprites = [self.pygame.sprite.GroupSingle(button) for button in self.buttons]
        self.menu_name = menu_name
        self.background = background

    def update(self, mouse: tuple[int, int], click: bool) -> str:
        """
        Update the menu
        """
        self.background.draw_static()
        for i, btn in enumerate(self.buttons):
            sprite = self.button_sprites[i]
            if btn.hover(mouse):
                btn.set_hover(self.hover_sound)
            else:
                btn.set_not_hover()
            sprite.draw(self.screen, mouse)
            btn.draw_text()
            if click and btn.hover(mouse):
                self.click_sound.play()
                return btn.function()
        return self.menu_name

def quit_game():
    """
    Quit the game
    """
    # pylint: disable=no-member
    pygame.quit()
    # pylint: enable=no-member
    sys.exit(0)

def start_game() -> str:
    """
    Start the game
    """
    return "Start"

def get_main_menu(pygame_module: pygame, screen: pygame.Surface, background: Background, asset_data: AssetData) -> Menu:
    """
    Get the main menu
    """
    main_menu_btns = [
        button_module.Button(screen, sprite_loader(pygame_module, asset_data.images.menu_btn), 235, 100, "Start", start_game),
        button_module.Button(screen, sprite_loader(pygame_module, asset_data.images.menu_btn), 235, 250, "Quit", quit_game)
    ]
    return Menu(pygame_module, screen, main_menu_btns, "Main", background, asset_data)
