import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

snack_coords = [(400, 300)]
food_coords = (random.randint(50, 750), random.randint(50, 550))
snack_speed = 5
direction = (1, 0)

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            print("按键:", event.key)
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    screen.fill((0, 0, 0))

    snack_head = (snack_coords[0][0] + direction[0] * snack_speed, snack_coords[0][1] + direction[1] * snack_speed)
    if(snack_head[0] < 0):
        snack_head = (800, snack_head[1])
    if(snack_head[0] > 800):
        snack_head = (0, snack_head[1])
    if(snack_head[1] < 0):
        snack_head = (snack_head[0], 600)
    if(snack_head[1] > 600):
        snack_head = (snack_head[0], 0)
    
    snack_coords.insert(0, snack_head)
    for i, segment in enumerate(snack_coords):
        pygame.draw.circle(screen, (0, 255, 0), segment, 15)

    if(snack_head[0] + 7.5 > food_coords[0] - 10 and snack_head[0] - 7.5 < food_coords[0] + 10 and snack_head[1] + 7.5 > food_coords[1] - 10 and snack_head[1] - 7.5 < food_coords[1] + 10):
        food_coords = (random.randint(50, 750), random.randint(50, 550))
    else:
        snack_coords.pop()

    pygame.draw.circle(screen, ((255, 0, 0)), food_coords, 10)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
