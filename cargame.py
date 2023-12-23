import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)

road_w = int(width / 1.6)
roadmark_w = int(width / 80)

right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")
screen.fill((0, 255, 0))

pygame.display.update()

# load car
car = pygame.image.load("car.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  yo'l chizish
    pygame.draw.rect(
        screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height)
    )
    # center line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )
    # right line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height)
    )

    # left line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height)
    )

    screen.blit(car, (400, 550))
    pygame.display.update()
