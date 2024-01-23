import pygame
import random
import time

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
    [70, 50],
    [60, 50],
    [50, 50],
    [40, 50],
    [30, 50],
    [20, 50],
    [10, 50],
]

score = 0
font = pygame.font.SysFont(None, 36)

food_position = [random.randint(1, (WIDTH // 10)) * 10,
                 random.randint(1, (HEIGHT // 10)) * 10]


def game_over():
    my_font = pygame.font.SysFont(None, 80)
    game_over_text = my_font.render(f"Your Score: {score}", True, "red")
    screen.blit(game_over_text, (130, 280))
    pygame.display.flip()
    time.sleep(2)
    exit()


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

    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_position = [random.randint(1, (WIDTH // 10)) * 10,
                         random.randint(1, (HEIGHT // 10)) * 10]
    else:
        snake_body.pop()

    screen.fill("black")
    for pos in snake_body:
        pygame.draw.rect(screen, "green", pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, "White", pygame.Rect(food_position[0], food_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    text = font.render(f"Score: {score}", 1, "white")
    screen.blit(text, (10, 10))

    speed_text = font.render(f"Speed: {snake_speed + score}", 1, "white")
    screen.blit(speed_text, (10, 40))
    pygame.display.update()
    fps.tick(snake_speed + score)
pygame.quit()
