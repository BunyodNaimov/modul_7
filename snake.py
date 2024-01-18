import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake Game!")

clock = pygame.time.Clock()
fps = 60

snake_position = [200, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake_position[0] -= 10
    if keys[pygame.K_RIGHT]:
        snake_position[0] += 10
    if keys[pygame.K_DOWN]:
        snake_position[1] += 10
    if keys[pygame.K_UP]:
        snake_position[1] -= 10

    snake_body.insert(0, list(snake_position))

    screen.fill("black")
    for pos in snake_body:
        pygame.draw.rect(screen, "green", pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
