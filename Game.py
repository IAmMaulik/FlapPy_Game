import pygame, sys

pygame.init()
screen = pygame.display.set_mode((576, 840))
clock = pygame.time.Clock()

bg_surface = pygame.image.load()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)