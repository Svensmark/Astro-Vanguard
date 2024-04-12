from pygame import Rect
from lazer import Lazer

# create a player class extending pygame.Rect
class Player(Rect):
    def __init__(self, pygame, screen, x, y, width, height):
        super().__init__(x, y, width, height)
        self.pygame = pygame
        self.shoot_cooldown = 0
        self.screen = screen
        self.sprite = self.pygame.image.load('assets/heroship_1.png').convert_alpha()

    def move(self, keys):
        if keys[self.pygame.K_w]:
            self.y = self.y - 5
            if self.y < 0:
                self.y = 0

        if keys[self.pygame.K_s]:
            self.y = self.y + 5
            if self.y > self.screen.get_height() - self.height:
                self.y = self.screen.get_height() - self.height

    def shoot(self, keys, lazers):
        if keys[self.pygame.K_SPACE]:
            if self.shoot_cooldown == 0:
                lazers.append(Lazer(self.screen, self.midright[0], self.midright[1], 20, 5))
                self.shoot_cooldown = 15

    def cooldown(self):
        if self.shoot_cooldown != 0:
            self.shoot_cooldown -= 1

    def draw(self):
        self.screen.blit(self.sprite, self)

    def update(self, keys, lazers):
        self.draw()
        self.move(keys)
        self.shoot(keys, lazers)
        self.cooldown()