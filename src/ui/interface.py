# Create an interface class
class Interface:
    def __init__(self, pygame, screen, player_data):
        self.pygame = pygame
        self.screen = screen
        self.hp_bar = pygame.Rect(20, 20, player_data.current_hp, 20)
        self.hp_bar_background = pygame.Rect(18, 18, player_data.current_hp + 4, 24)

    def update_hp(self, player_data):
        self.hp_bar.update(
            self.hp_bar.left,
            self.hp_bar.top,
            player_data.current_hp,
            self.hp_bar.height,
        )

    def draw_ui(self, game_data):
        font = self.pygame.font.Font(None, 36)
        point_surface = font.render("Points: " + str(game_data.score), True, "White")
        self.pygame.draw.rect(self.screen, (255, 255, 255), self.hp_bar_background)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hp_bar)
        self.screen.blit(point_surface, (20, 45))

    def update(self, player_data, game_data):
        self.update_hp(player_data)
        self.draw_ui(game_data)
