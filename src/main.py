import pygame
from sys import exit
import random


# Game variables
screen_width = 600
screen_height = 480

player_width = 50
player_height = 35

player_shoot_cooldown = 0
enemy_spawn_rate = 0

lazer_width = 35
lazer_height = 5

player_x = 100
player_y = 100

max_hp = 100
current_hp = max_hp

points = 0

lazers = []
enemies = []

game_running = True


# Core game initialization
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
bg_1 = pygame.image.load('assets/background.png').convert_alpha()
bg_1_x = 0
bg_2 = pygame.image.load('assets/background.png').convert_alpha()
bg_2_x =  bg_1.get_width()
clock = pygame.time.Clock()


# Main game loop
while True:

    # Check for exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if game_running:

        # Create the player    
        rect = pygame.Rect(player_x, player_y, player_width, player_height)


        # Check for player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y = player_y - 5
            if player_y < 0:
                player_y = 0

        if keys[pygame.K_DOWN]:
            player_y = player_y + 5
            if player_y > screen_height - player_height:
                player_y = screen_height - player_height
        
        if keys[pygame.K_SPACE]:
            if player_shoot_cooldown == 0:
                lazer = pygame.Rect(rect.midright[0], rect.midright[1], lazer_width, lazer_height)
                lazers.append(lazer)
                player_shoot_cooldown = 10


        # Handle the shoot cooldown 
        if player_shoot_cooldown != 0:
            player_shoot_cooldown -= 1


        # Draw the screen
        screen.fill('White')
        screen.blit(bg_1, (bg_1_x,0))
        screen.blit(bg_2, (bg_2_x,0))
        bg_1_x -= 2
        bg_2_x -= 2

        if bg_1_x < ( -bg_1.get_width()):
            bg_1_x = bg_1.get_width() - 40
        
        elif bg_2_x < ( -bg_1.get_width()):
            bg_2_x =  bg_1.get_width() - 40

        pygame.draw.rect(screen, 'Pink', rect)
        

        # Draw the interface
        font = pygame.font.Font(None, 36) 
        hp_surface = font.render('HP: ' + str(current_hp), True, 'White')
        point_surface = font.render('Points: ' + str(points), True, 'White')
        screen.blit(hp_surface, (20, 20))
        screen.blit(point_surface, (20, 45))


        # Handle the enemies
        if enemy_spawn_rate == 0:
            enemy_y = random.randint(30, screen_height-player_height-30)
            enemy = pygame.Rect(screen_width, enemy_y, player_width, player_height)
            enemies.append(enemy)
            enemy_spawn_rate = 60

        elif enemy_spawn_rate != 0:
            enemy_spawn_rate -= 1   

        # Handle the lazers
        enemies_to_be_removed = []
        lazers_to_be_removed = []
        for lazer in lazers:
            pygame.draw.rect(screen, 'Purple', lazer)
            lazer.x = lazer.x + 10

            for enemy in enemies:
                if lazer.colliderect(enemy):
                    enemies_to_be_removed.append(enemy)
                    lazers_to_be_removed.append(lazer)
                    points += 10

            if lazer.x > screen_width:
                lazers_to_be_removed.append(lazer)

        for lazer_tbr in lazers_to_be_removed:
            lazers.remove(lazer_tbr)


        for enemy in enemies:
            pygame.draw.rect(screen, 'Green', enemy)
            enemy.x = enemy.x - 5

            if enemy.x < 0:
                current_hp -= 20
                #screen.fill((255,0,0,15))
                enemies_to_be_removed.append(enemy)
        
        for enemy in enemies_to_be_removed:
            enemies.remove(enemy)



        if current_hp == 0:
            game_running = False


        
    else:
        screen.fill('Red')
        font = pygame.font.Font(None, 36) 
        hp_surface = font.render('Game Over!', True, 'Black')
        text_rect = hp_surface.get_rect()
        text_rect.center = (screen_width/2, screen_height/2)
        screen.blit(hp_surface, text_rect)

    # Update the game window
    pygame.display.update()
    clock.tick(60)


