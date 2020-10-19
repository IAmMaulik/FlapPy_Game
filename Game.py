import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_pos_x, 630))
    screen.blit(floor_surface, (floor_pos_x + 500, 630))

pygame.init()
screen = pygame.display.set_mode((500, 750))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()

floor_surface = pygame.image.load('assets/base.png').convert()
floor_pos_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0,0))
    floor_pos_x -= 1
    draw_floor()
    if floor_pos_x <= -500:
        floor_pos_x = 0

    pygame.display.update()
    clock.tick(60)