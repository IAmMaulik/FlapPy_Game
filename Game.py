import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_pos_x, 630))
    screen.blit(floor_surface, (floor_pos_x + 500, 630))

pygame.init()
screen = pygame.display.set_mode((500, 750))
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

# sprites
bg_surface = pygame.image.load('assets/background-day.png').convert()

floor_surface = pygame.image.load('assets/base.png').convert()
floor_pos_x = 0

bird_surface = pygame.image.load('assets/bluebird-downflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 325))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_pos_x -= 1
    draw_floor()
    if floor_pos_x <= -500:
        floor_pos_x = 0

    pygame.display.update()
    clock.tick(60)