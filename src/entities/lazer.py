import pygame

# create a lazer class extending pygame.Rect
class Lazer(pygame.Rect):
    def __init__(self, screen, x, y, width, height):
        super().__init__(x, y, width, height)
        self.screen = screen

    def move(self):
        self.x += 5

    def draw(self):
        pygame.draw.rect(self.screen, 'Red', self)
    
    def handle_collision(self, enemies, score, lazers_to_be_removed):
        for enemy in enemies:
            if self.colliderect(enemy):
                lazers_to_be_removed.append(self)
                enemies.remove(enemy)
                score += 10
        return score

    def update(self, lazers_to_be_removed, enemies, score):
        self.move()
        self.draw()

        score = self.handle_collision(enemies, score, lazers_to_be_removed)

        if self.x > self.screen.get_width():
            lazers_to_be_removed.append(self)
        
        return score