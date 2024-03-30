import pygame
from sys import exit
from menus import menu
from game.play import Play


# Core game initialization
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
click = False


# Scenes
main_menu = menu.get_main_menu(pygame, screen)
start_menu = menu.get_start_menu(pygame, screen)
play_scene = Play(pygame, screen)
# Scene selecter
scene_selecter = "main_menu"


# Main game loop
while True:
    mouse = pygame.mouse.get_pos()
    
    # Get input event - (Mouse/Keyboard input etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    
    # Scene selecter - Draws either a menu or game depending on gamestate/scene
    match scene_selecter:
        case "main_menu":
            scene_selecter = main_menu.update(screen, mouse, click)
        case "start":
            scene_selecter = start_menu.update(screen, mouse, click)
        case "play":
            scene_selecter = play_scene.update(screen, mouse, click)
            
    
    click = False
    pygame.display.update()
    clock.tick(120)