import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_pos_x, 630))
    screen.blit(floor_surface, (floor_pos_x + 500, 630))

def CreatePipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    return new_pipe

def MovePipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def DrawPipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

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

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Possible Heights for pipes
pipe_height = [400, 500, 300]

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10
        if event.type == SPAWNPIPE:
            pipe_list.append(CreatePipe())

    screen.blit(bg_surface, (0,0))
    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = MovePipe(pipe_list)
    DrawPipe(pipe_list)

    #Floor
    floor_pos_x -= 1
    draw_floor()
    if floor_pos_x <= -500:
        floor_pos_x = 0

    pygame.display.update()
    clock.tick(60)