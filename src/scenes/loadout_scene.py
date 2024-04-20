from ui.button_module import Button
import pygame
from scenes.scene import Scene
from utils import asset_loader
from utils.asset_loader import sprite_loader
from utils.background import Background
from utils.data import Data


class LoadoutScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        super().__init__(pygame_module, screen, data)
        self.name = 'LoadoutScene'
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data
        
        self.start_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), 150, 350, "Enter World", start_btn, data)
        self.main_menu_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), 150, 450, "Back", main_menu_btn, data)
        self.background = Background(self.pygame_module, self.screen)
        
        # TODO - Fix music between menu scenes
        self.music = asset_loader.sound_loader('assets/sounds/music/galactic_odyssey.ogg')
        
    def update(self, events):
        mouse_position = self.pygame_module.mouse.get_pos()
        
        self.background.draw_static()
        self.screen.blit(self.start_btn.btn_img, (self.start_btn.x, self.start_btn.y))
        self.screen.blit(self.main_menu_btn.btn_img, (self.main_menu_btn.x, self.main_menu_btn.y))
        
        self.start_btn.update(mouse_position, events)
        self.main_menu_btn.update(mouse_position, events)
        
        self.draw_player()
        self.draw_inventory()
        
        if self.start_btn.clicked:
            return self.start_btn.function()
        elif self.main_menu_btn.clicked:
            return self.main_menu_btn.function()
        else:
            return self.name
    
    # TODO - Move into own class
    def draw_player(self):
        veil = self.pygame_module.Surface((350, 225))
        veil.fill((128, 128, 128))
        veil.set_alpha(128)
        self.screen.blit(veil, (150,100))
    
    # TODO - Move into own class
    def draw_inventory(self):
        veil = self.pygame_module.Surface((400, 450))
        veil.fill((128, 128, 128))
        veil.set_alpha(128)
        self.screen.blit(veil, (550,100))
    
    def render(self):
        self.background.draw_static()
        self.draw_player()
        self.draw_inventory()
        self.screen.blit(self.start_btn.btn_img, (self.start_btn.x, self.start_btn.y))
        self.screen.blit(self.main_menu_btn.btn_img, (self.main_menu_btn.x, self.main_menu_btn.y))
        self.start_btn.draw_text()
        self.main_menu_btn.draw_text()        
    
    def on_load(self):
        self.music.play(loops=10, fade_ms=4000)
    
    def on_leave(self):
        self.music.fadeout(2000)
    


def start_btn():
    return 'GameScene'

def main_menu_btn():
    return 'MainMenu'