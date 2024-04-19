"""
Main game file
"""
import sys
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, MOUSEBUTTONDOWN
# pylint: enable=no-name-in-module
from managers.scene_manager import SceneManager
from utils.data import Data


# Core game initialization
data = Data()
# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member
pygame.display.set_caption('Astro Vanguard')
screen = pygame.display.set_mode((data.game_data.screen_width, data.game_data.screen_height))
clock = pygame.time.Clock()
scene_manager = SceneManager(pygame, screen, pygame.event.get(), data)


# Main game loop
while True:

    # Check for events
    events = []
    for event in pygame.event.get():
        if event.type == QUIT:
            # pylint: disable=no-member
            pygame.quit()
            # pylint: enable=no-member
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            events.append('MOUSEBUTTONDOWN')

    # Handle scenes
    scene_manager.update_current_scene(events)

    pygame.display.update()
    clock.tick(data.game_data.fps)
