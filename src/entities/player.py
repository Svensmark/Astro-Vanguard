from pygame import Rect
from entities.lazer import Lazer
import math

class Player(Rect):
    def __init__(self, pygame, screen, x, y, width, height):
        super().__init__(x, y, width, height)
        self.pygame = pygame
        self.screen = screen
        self.sprite = self.pygame.image.load('assets/heroship_1.png').convert_alpha()
        self.velocity = [0, 0]  # Initial velocity
        self.acceleration = 1  # Acceleration factor
        self.max_speed = 10  # Maximum speed
        self.friction = 0.15  # Friction factor
        self.shoot_cooldown = 0  # Shoot cooldown timer

    def move(self, keys):
        if keys[self.pygame.K_w]:
            self.velocity[1] -= self.acceleration
        if keys[self.pygame.K_s]:
            self.velocity[1] += self.acceleration
        if keys[self.pygame.K_a]:
            self.velocity[0] -= self.acceleration
        if keys[self.pygame.K_d]:
            self.velocity[0] += self.acceleration

        # Apply friction
        self.velocity[0] *= (1 - self.friction)
        self.velocity[1] *= (1 - self.friction)

        # Limit speed
        self.velocity[0] = max(-self.max_speed, min(self.velocity[0], self.max_speed))
        self.velocity[1] = max(-self.max_speed, min(self.velocity[1], self.max_speed))

        # Update position based on velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Ensure player stays within screen boundaries
        self.x = max(0, min(self.x, self.screen.get_width() - self.width))
        self.y = max(0, min(self.y, self.screen.get_height() - self.height))

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
