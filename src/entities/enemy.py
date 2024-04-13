from pygame import Rect


# create an enemy class extending pygame.Rect
class Enemy(Rect):
    def __init__(self, pygame, screen, x, y, width, height):
        super().__init__(x, y, width, height)
        self.pygame = pygame
        self.screen = screen
        self.sprite = self.pygame.image.load("assets/enemy_ship_1.png").convert_alpha()

    def move(self):
        self.x -= 5

    def draw(self):
        self.screen.blit(self.sprite, self)

    def update(self, current_hp, enemies_to_be_removed):
        self.move()
        self.draw()

        if self.x < 0:
            enemies_to_be_removed.append(self)

        return current_hp
