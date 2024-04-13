from pygame import Rect
from utils.json_reader import File_reader


# create an enemy class extending pygame.Rect
class Enemy(Rect):
    def __init__(self, pygame, screen, x, y):
        file_reader_game = File_reader()
        enemy_data = file_reader_game.read_json("enemy.json")
        
        super().__init__(x, y, enemy_data['width'], enemy_data['height'])
        self.pygame = pygame
        self.screen = screen
        self.sprite = self.pygame.image.load("assets/enemy_ship_1.png").convert_alpha()

    def move(self):
        self.x -= 5

    def draw(self):
        self.screen.blit(self.sprite, self)

    def update(self, player_data, enemies_to_be_removed):
        self.move()
        self.draw()

        if self.x < 0:
            enemies_to_be_removed.append(self)
