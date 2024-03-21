import pygame
import json
from pathlib import Path
from json_helper import File_reader
import math

# Read variables json
script_location = Path(__file__).absolute().parent
file_location = script_location / 'player.json'
f = open(file_location, 'r')
player_json = json.load(f)

file_reader = File_reader('player.json') 


variables = player_json['variables']
graphics = player_json['graphics']

attack_right_anim_ar = file_reader.read_animation_array('graphics','attack_right')
attack_left_anim_ar = file_reader.read_animation_array('graphics','attack_left')

##
# Player class
##
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        # Init images
        self.stand_right = pygame.image.load(graphics['stand_right']).convert_alpha()
        self.stand_left = pygame.image.load(graphics['stand_left']).convert_alpha()
        
        self.image = self.stand_right
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0
        self.animation_frames = 0
        self.animation_tick = 0
        
        self.looking_right = True
        self.looking_left = False
        self.attacking_bool = False

        
    def player_input(self):
        keys=pygame.key.get_pressed()                    
        if keys[pygame.K_RIGHT]:
            self.image = self.stand_right
            self.rect.x += variables['walk_speed']
            self.looking_right = True
            self.looking_left = False

        if keys[pygame.K_LEFT]:
            self.image =  self.stand_left
            self.rect.x -= variables['walk_speed']
            self.looking_left = True
            self.looking_right = False
            
        if keys[pygame.K_UP] and self.rect.bottom >= 400:
            self.gravity = -15
        
        if keys[pygame.K_SPACE]:            
            if (not self.attacking_bool):
                self.attacking_bool = True
                if (self.looking_right):
                    self.animation_frames = len(attack_right_anim_ar)
                if (self.looking_left):
                    self.animation_frames = len(attack_left_anim_ar)
            
    def attacking(self):
        if (self.attacking_bool):
            if (self.attacking_bool):
                if (self.animation_tick >= self.animation_frames-0.1):
                    self.animation_frames = 0
                    self.animation_tick = 0
                    self.attacking_bool = False
                    if (self.looking_right):
                        self.image = self.stand_right
                    elif(self.looking_left):
                        self.image =  self.stand_left
                else:                    
                    self.animation_tick += 0.1
                    temp = math.floor(self.animation_tick)
                    if (self.looking_right):                        
                        self.image = pygame.image.load(attack_right_anim_ar[temp])
                    elif(self.looking_left):
                        self.image = pygame.image.load(attack_left_anim_ar[temp])
                
            
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
    
    def check_walls(self):
        if self.rect.midright[0] >= 800:
            self.rect.x = 685
        if self.rect.midleft[0] <= 0:
            self.rect.x = 0
    
    def update(self):
        self.player_input()
        self.check_walls()
        self.attacking()
        self.apply_gravity()
