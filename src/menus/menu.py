import pygame
from pygame import mixer
from menus import button_module


class Menu():
    def __init__(self, pygame: pygame, screen: pygame.Surface, buttons: list[button_module.Button], menu_name: str, background):
        # Initiliaze
        self.pygame = pygame
        self.screen = screen
        
        # Buttons
        self.buttons = buttons
        
        self.button_sprites = []
        for button in self.buttons:
            button_sprite = pygame.sprite.GroupSingle()
            button_sprite.add(button)
            self.button_sprites.append(button_sprite)
        
        self.menu_name = menu_name
        
        self.background = background
        self.hover_sound = mixer.Sound('assets/menu_selection_hover.mp3')
        self.click_sound = mixer.Sound('assets/menu_selection_click.mp3')

    
    def update(self,screen, mouse: tuple[int,int], click: bool): 
        # Draw background
        self.background.draw_static()
        
        # Draw buttons
        # Exit button
        for i in range(len(self.buttons)):
            btn = self.buttons[i]
            sprite = self.button_sprites[i]
            
            if (btn.hover(mouse)):
                btn.set_hover(self.hover_sound)
            else:
                btn.set_not_hover()
            sprite.draw(self.screen, mouse)
            btn.draw_text()
            
            
            if click:
                if btn.hover(mouse):                    
                    self.click_sound.play()
                    return btn.function()
        
        return self.menu_name
        
        
# Main Menu
def quit():
    pygame.quit()
    exit()   
def start():
    return "Start"
def get_main_menu(pygame: pygame, screen: pygame.surface, background):
    main_menu_btns = [
                button_module.Button(screen, pygame, 235, 100, "Start", start),
                button_module.Button(screen, pygame, 235, 250, "Quit", quit)]
    return Menu(pygame, screen, main_menu_btns, "Main", background)
