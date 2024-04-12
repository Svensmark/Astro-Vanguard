# create a background class
class Background:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        # self.bg_1 = self.pygame.image.load('assets/background.png').convert_alpha()
        self.bg_1 = self.pygame.transform.scale(self.pygame.image.load('assets/background.png').convert_alpha(), (self.screen.get_width(), self.screen.get_height()))
        self.bg_2 = self.pygame.transform.scale(self.pygame.image.load('assets/background.png').convert_alpha(), (self.screen.get_width(), self.screen.get_height()))
        self.bg_1_x = 0
        self.bg_2_x =  self.screen.get_width()

    def draw(self):
        self.screen.fill('White')
        self.screen.blit(self.bg_1, (self.bg_1_x,0))
        self.screen.blit(self.bg_2, (self.bg_2_x,0))
        self.bg_1_x -= 2
        self.bg_2_x -= 2

        if self.bg_1_x < ( -self.screen.get_width()):
            self.bg_1_x = self.screen.get_width() - 2
        
        elif self.bg_2_x < ( -self.screen.get_width()):
            self.bg_2_x =  self.screen.get_width() - 2