import pygame
from utils.json_reader import File_reader

# create a lazer class extending pygame.Rect
class Lazer(pygame.Rect):
    def __init__(self, screen, x, y):
        file_reader_game = File_reader()
        lazer_data = file_reader_game.read_json("lazer.json")
        
        super().__init__(x, y, lazer_data['width'], lazer_data['height'])

        self.screen = screen

    def move(self):
        self.x += 5

    def draw(self):
        pygame.draw.rect(self.screen, 'Red', self)
    
    def handle_collision(self, game_data, lazers_to_be_removed):
        for enemy in game_data.enemies:
            if self.colliderect(enemy):
                lazers_to_be_removed.append(self)
                game_data.enemies.remove(enemy)
                game_data.score += 10

    def update(self, lazers_to_be_removed, game_data):
        self.move()
        self.draw()

        self.handle_collision(game_data, lazers_to_be_removed)

        if self.x > self.screen.get_width():
            lazers_to_be_removed.append(self)