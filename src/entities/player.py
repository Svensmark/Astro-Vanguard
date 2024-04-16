"""
Module for Player class
"""
import pygame
from entities.lazer import Lazer
from utils.asset_loader import sprite_loader, sound_loader
from utils.data import AssetData, GameData, PlayerData
import math

class Player(pygame.Rect):
    """
    Class for Player extending pygame.Rect
    """
    def __init__(self, pygame: pygame, screen: pygame.surface, player_data: PlayerData, asset_data: AssetData):
        super().__init__(player_data.start_x, player_data.start_y, player_data.width, player_data.height)
        print(type(asset_data.sounds))
        self.pygame = pygame
        self.screen = screen
        self.sprite = sprite_loader(self.pygame, 'assets/heroship/player2.png')
        self.velocity = player_data.velocity
        self.acceleration = player_data.acceleration
        self.max_speed = player_data.max_speed
        self.friction = player_data.friction
        self.shoot_cooldown = player_data.shoot_cooldown
        self.shooting_sound = sound_loader(asset_data.sounds.lazer)
        self.death = sound_loader(asset_data.sounds.player_death)
        self.x = player_data.start_x
        self.y = player_data.start_y

        self.animation_list = []
        self.frame_index = 0
        for i in range(4):
            self.animation_list.append(sprite_loader(self.pygame, f'assets/heroship/heroship_animated_{i+1}.png'))
            

    def move(self, keys: tuple[bool, ...]):
        """
        Method for moving player
        """
        if keys[self.pygame.K_w]:
            self.velocity[1] -= self.acceleration
        if keys[self.pygame.K_s]:
            self.velocity[1] += self.acceleration
        if keys[self.pygame.K_a]:
            self.velocity[0] -= self.acceleration
        if keys[self.pygame.K_d]:
            self.velocity[0] += self.acceleration

        # Apply friction
        self.velocity[0] *= 1 - self.friction
        self.velocity[1] *= 1 - self.friction

        # Limit speed
        self.velocity[0] = max(-self.max_speed, min(self.velocity[0], self.max_speed))
        self.velocity[1] = max(-self.max_speed, min(self.velocity[1], self.max_speed))

        # Update position based on velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Ensure player stays within screen boundaries
        self.x = max(0, min(self.x, self.screen.get_width() - self.width))
        self.y = max(0, min(self.y, self.screen.get_height() - self.height))
        

    def shoot(self, keys: tuple[bool, ...], game_data: GameData):
        """
        Method for player shooting
        """
        if keys[self.pygame.K_SPACE]:
            if self.shoot_cooldown == 0:
                self.shooting_sound.play()
                game_data.lazers.append(Lazer(self.pygame, self.screen, self.midright[0], self.midright[1]))
                self.shoot_cooldown = 15
                

    def cooldown(self):
        """
        Method for cooldown
        """
        if self.shoot_cooldown != 0:
            self.shoot_cooldown -= 1
            

    def draw(self):
        """
        Method for drawing player
        """
        
        if (self.frame_index >= len(self.animation_list)):
            self.frame_index = 0
        else:
            self.frame_index += 0.1
        self.sprite = self.animation_list[math.floor(self.frame_index-1)]
        self.screen.blit(self.sprite, self)
        

    def handle_collision(self, player_data: PlayerData, game_data: GameData):
        """
        Method for handling collision
        """
        for enemy in game_data.enemies:
            if self.colliderect(enemy):
                enemy.collision_sound.play()
                game_data.enemies.remove(enemy)
                player_data.current_hp -= 20


    def update(self, player_data: PlayerData, keys: tuple[bool, ...], game_data: GameData):
        """
        Method for updating player
        """
        self.draw()
        self.move(keys)
        self.shoot(keys, game_data)
        self.cooldown()
        self.handle_collision(player_data, game_data)
