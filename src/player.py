import pygame
import json
from pathlib import Path

# Read variables json
script_location = Path(__file__).absolute().parent
file_location = script_location / 'player.json'
f = open(file_location, 'r')
player_json = json.load(f)

player_variables = player_json['variables']
player_graphics = player_json['graphics']

##
# Player class
##
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        # Init images
        self.walk_right = pygame.image.load(player_graphics['walk_right']).convert_alpha()
        self.walk_left = pygame.image.load(player_graphics['walk_left']).convert_alpha()
        
        self.image = self.walk_right
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0

        
    def player_input(self):
        keys=pygame.key.get_pressed()                    
        if keys[pygame.K_RIGHT]:
            self.image = self.walk_right
            self.rect.x += player_variables['walk_speed']

        if keys[pygame.K_LEFT]:
            self.image =  self.walk_left
            self.rect.x -= player_variables['walk_speed']
            
        if keys[pygame.K_UP] and self.rect.bottom >= 400:
            self.gravity = -15
            

            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
    
    
    def update(self):
        self.player_input()
        self.apply_gravity()
