import pygame
from sys import exit

# Core 
pygame.init()
screen = pygame.display.set_mode((1600,1000))
clock = pygame.time.Clock()
def handle_exit():
     # Exit game
    for event in pygame.event.get():
        # If player closes the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



#map_background = pygame.image.load('graphics/background.png').convert_alpha()

test_grid = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
]

test_grid2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

testing_grid = test_grid2
testing_tile = 'graphics/isometric_tile-test2.png'

tiles = []
tile = pygame.image.load(testing_tile).convert_alpha()

for height_i in range(len(testing_grid)):
    for width_j in range(len(testing_grid[height_i])):
        tiles.append(pygame.image.load(testing_tile).convert_alpha())




while True:
    # Handle exit of game
    handle_exit()
        
    # Handle background
    #screen.blit(map_background,(0,0))    
    count = 0
    for height_i in range(len(testing_grid)):
        y = height_i
        for width_j in range(len(testing_grid[height_i])):
            x = width_j

            dist_x = x*0.5*tile.get_width() + y*-0.5*tile.get_width()
            dist_y = x*0.25*tile.get_height()*1.46 + y*0.25*tile.get_height()*1.46

            screen.blit(tiles[count],((dist_x-tile.get_width()/2)+len(testing_grid[height_i])/2*tile.get_width(),dist_y))
            count += 1


    # Update screen
    pygame.display.update()
    clock.tick(60)


