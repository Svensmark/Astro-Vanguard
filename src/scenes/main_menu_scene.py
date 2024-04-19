from ui.button_module import Button
import pygame
from scenes.scene import Scene
from utils.asset_loader import sprite_loader
from utils.background import Background
from utils.data import Data


class MainMenu(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        super().__init__(pygame_module, screen, data)
        self.name = 'MainMenu'
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data
        
        self.start_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), 235, 100, "Start", start_btn, data)
        self.background = Background(self.pygame_module, self.screen)
        
    def update(self, events):
        self.background.draw_static()
        self.screen.blit(self.start_btn.btn_img, (self.start_btn.x, self.start_btn.y))

        #TODO Handle clicks in button class
        if self.start_btn.hover(self.pygame_module.mouse.get_pos()):
            self.start_btn.set_hover(self.start_btn.hover_sound)
            if 'MOUSEBUTTONDOWN' in events:                    
                self.start_btn.play_click_sound()
                return self.start_btn.function()
        else:
            self.start_btn.set_not_hover()
            self.screen.blit(self.start_btn.btn_img, (self.start_btn.x, self.start_btn.y))

        # This is fine
        self.start_btn.draw_text()
        return self.name
    


def start_btn():
    return 'GameScene'