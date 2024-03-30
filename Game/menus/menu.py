import pygame
from pygame import mixer
from menus import button_module


class Menu():
    def __init__(self, pygame: pygame, screen: pygame.Surface, buttons: list[button_module.Button], menu_name: str):
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
        
        self.background = pygame.image.load('graphics/background.png').convert_alpha()
        self.hover_sound = mixer.Sound('sounds/menu_selection_hover.mp3')
        self.click_sound = mixer.Sound('sounds/menu_selection_click.mp3')

    
    def draw_menu(self,screen, mouse: tuple[int,int], click: bool): 
        # Draw background
        pygame.transform.scale(self.background, (150,2))
        screen.blit(self.background,(525,0))
        #mouse = self.pygame.mouse.get_pos()
        
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
    return "start"
def get_main_menu(pygame: pygame, screen: pygame.surface):
    main_menu_btns = [
                button_module.Button(screen, pygame, 750, 250, "Start", start),
                button_module.Button(screen, pygame, 750, 350, "Quit", quit)]
    return Menu(pygame, screen, main_menu_btns, "main_menu")


# Start Menu
def choose_char():
    print("Pressed CHOOSE CHARACTER")
    return "play"
def new_char():
    print("Pressed NEW CHARACTER")
    return "start"
def back_to_mm():
    return "main_menu"
def get_start_menu(pygame: pygame, screen: pygame.surface):
    main_menu_btns = [
                button_module.Button(screen, pygame, 750, 250, "Play", choose_char),
                button_module.Button(screen, pygame, 750, 350, "New", new_char),
                button_module.Button(screen, pygame, 750, 450, "Back", back_to_mm)]
    return Menu(pygame, screen, main_menu_btns, "start")