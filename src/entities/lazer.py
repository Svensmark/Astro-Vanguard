from pygame import Rect
from utils.json_reader import File_reader


# create a lazer class extending pygame.Rect
class Lazer(Rect):
    def __init__(self, pygame, screen, x, y):
        self.pygame = pygame
        self.screen = screen

        file_reader_game = File_reader()
        lazer_data = file_reader_game.read_json("lazer.json")
        self.sprite = self.pygame.image.load('assets/lazer_bolt.png').convert_alpha()
        
        super().__init__(x, y, lazer_data['width'], lazer_data['height'])

        

    def move(self, game_data):
        self.x += 5

        if self.x > self.screen.get_width():
            game_data.lazers.remove(self)

    def draw(self):
        self.screen.blit(self.sprite, self)
        
    
    def handle_collision(self, game_data):
        for enemy in game_data.enemies:
            if self.colliderect(enemy):
                game_data.lazers.remove(self)
                game_data.enemies.remove(enemy)
                enemy.collision_sound.play()
                game_data.score += 10

    def update(self, game_data):
        self.move(game_data)
        self.draw()
        self.handle_collision(game_data)

        
        