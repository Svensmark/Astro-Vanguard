import pygame
from utils.json_reader import File_reader


# create a lazer class extending pygame.Rect
class Lazer(pygame.Rect):
    def __init__(self, screen, x, y):
        file_reader_game = File_reader()
        lazer_data = file_reader_game.read_json("lazer.json")
        
        super().__init__(x, y, lazer_data['width'], lazer_data['height'])

        self.screen = screen

    def move(self, game_data):
        self.x += 5

        if self.x > self.screen.get_width():
            game_data.lazers.remove(self)

    def draw(self):
        pygame.draw.rect(self.screen, 'Red', self)
    
    def handle_collision(self, game_data):
        for enemy in game_data.enemies:
            if self.colliderect(enemy):
                game_data.lazers.remove(self)
                game_data.enemies.remove(enemy)
                game_data.score += 10

    def update(self, game_data):
        self.move(game_data)
        self.draw()
        self.handle_collision(game_data)

        
        