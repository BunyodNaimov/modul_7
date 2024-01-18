import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake Game!")

snake_speed = 15
fps = pygame.time.Clock()

direction = "RIGHT"
change_to = direction

snake_position = [200, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

food_position = [random.randint(1, (WIDTH // 10)) * 10, random.randint(1, (HEIGHT // 10)) * 10]


def game_over():
    pygame.quit()


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    screen.fill("black")
    for pos in snake_body:
        pygame.draw.rect(screen, "green", pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.draw.rect(screen, "White", pygame.Rect(food_position[0], food_position[1], 20, 20))

    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        game_over()

    pygame.display.update()
    fps.tick(snake_speed)
pygame.quit()
