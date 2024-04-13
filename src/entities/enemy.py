from pygame import Rect
from utils.json_reader import File_reader
from pygame import mixer


# create an enemy class extending pygame.Rect
class Enemy(Rect):
    def __init__(self, pygame, screen, x, y, asset):
        file_reader_game = File_reader()
        enemy_data = file_reader_game.read_json("enemy.json")
        
        super().__init__(x, y, enemy_data['width'], enemy_data['height'])
        self.pygame = pygame
        self.screen = screen
        self.collision_sound = mixer.Sound('assets/Enemy_explosion.ogg')
        self.sprite = self.pygame.image.load(asset).convert_alpha()

    def move(self):
        self.x -= 5
        if self.x < 0:
            self.x = 800

    def draw(self):
        self.screen.blit(self.sprite, self)

    def update(self):
        self.move()
        self.draw()

        
