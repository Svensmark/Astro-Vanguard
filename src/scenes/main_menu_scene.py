from ui.button_module import Button
import pygame
from scenes.scene import Scene
from utils import asset_loader
from utils.asset_loader import sprite_loader
from utils.background import Background
from utils.data import Data
import sys


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        super().__init__(pygame_module, screen, data)
        self.name = 'MainMenu'
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data
        
        self.start_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), screen.get_width()/2-175, 100, "Start", start_btn, data)
        self.settings_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), screen.get_width()/2-175, 200, "Settings", settings_btn, data)
        self.quit_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), screen.get_width()/2-175, 300, "Quit", quit_btn, data)
        self.buttons = [self.start_btn, self.settings_btn, self.quit_btn]
        
        self.background = Background(self.pygame_module, self.screen)
        
        self.music = asset_loader.sound_loader('assets/sounds/music/galactic_odyssey.ogg')
        
    def update(self, events):
        mouse_position = self.pygame_module.mouse.get_pos()
        self.background.draw_static()
        
        # Button updates
        for btn in self.buttons:
            btn.update(mouse_position, events)
        
        # Check for button clicks
        for btn in self.buttons:
            if btn.clicked:
                return btn.function()
            
        return self.name
    
    def on_load(self):
        self.music.play(loops=10, fade_ms=4000)
    
    def on_leave(self):
        self.music.fadeout(2000)
    
    def render(self):
        self.background.draw_static()
        for btn in self.buttons:
            self.screen.blit(btn.btn_img, (btn.x, btn.y))
            btn.draw_text()

def start_btn():
    return 'LoadoutScene'

def settings_btn():
    return 'SettingsMenu'

def quit_btn():
    # pylint: disable=no-member
    pygame.quit()
    # pylint: enable=no-member
    sys.exit()