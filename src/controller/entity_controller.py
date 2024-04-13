import random
from entities.enemy import Enemy


## TODO - Rename to controller
class Spawner():
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    ## TODO - Change functionality cleanup
    def spawn_enemy(self, game_data, player_data, enemy_data, spawner_data):
        if enemy_data.spawn_rate == 0:
            enemy_y = random.randint(30, game_data.screen_height-player_data.height-30)
            
            random_ship_img = spawner_data.enemy_ships[random.randint(0, len(spawner_data.enemy_ships))-1]
            enemy = Enemy(self.pygame, self.screen, game_data.screen_width, enemy_y, random_ship_img)
            game_data.add_enemy(enemy)
            enemy_data.spawn_rate = 60

        elif enemy_data.spawn_rate != 0:
            enemy_data.spawn_rate -= 1   
    
    def handle_update_enemy(self, game_data):
        for enemy in game_data.enemies:
            enemy.update()

    def update(self, game_data, player_data, enemy_data, spawner_data):
        self.handle_update_enemy(game_data)
        self.spawn_enemy(game_data, player_data, enemy_data, spawner_data)