import pygame
from scenes.scene import Scene
from ui.button_module import Button
from utils.asset_loader import sound_loader, sprite_loader
from utils.background import Background
from utils.data import Data


class SettingsScene(Scene):
    def __init__(self, pygame_module: pygame, screen: pygame.Surface, data: Data):
        super().__init__(pygame_module, screen, data)
        self.name = "SettingsMenu"
        self.pygame_module = pygame_module
        self.screen = screen
        self.data = data

        self.back_btn = Button(screen, sprite_loader(pygame_module, data.asset_data.images.menu_btn), 50, 50, "Back", back_btn, data)
        self.buttons = [self.back_btn]

        self.background = Background(self.pygame_module, self.screen)
        
        self.music = sound_loader('assets/sounds/music/galactic_odyssey.ogg')
    
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
    

    def render(self):
        self.background.draw_static()
        for btn in self.buttons:
            self.screen.blit(btn.btn_img, (btn.x, btn.y))
            btn.draw_text()

    def on_load(self):
        self.music.play(loops=10, fade_ms=4000)

    def on_leave(self):
        self.music.fadeout(2000)


def back_btn():
    return 'MainMenu'