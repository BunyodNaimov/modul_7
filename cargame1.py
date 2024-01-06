# tutorial: https://www.youtube.com/watch?v=W-QOtdD3qx4

import pygame
from pygame.locals import *
import random

# shape parameters
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
# animation parameters
speed = 1

# initiallize the app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("Car game")
# set background colour
screen.fill((60, 220, 0))
# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("car.png")
# resize image
# car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

# load enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

counter = 0
# Игровой цикл
while running:
    counter += 1

    # Увеличение сложности игры со временем
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Уровень повышен", speed)

    # Анимация вражеской машины
    car2_loc.y += speed
    if car2_loc.y > height:
        # Случайный выбор полосы
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # Логика завершения игры
    if car_loc.colliderect(car2_loc):
        print("ИГРА ОКОНЧЕНА! ВЫ ПРОИГРАЛИ!")
        break

    # Обработчики событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                # Переместить машину игрока влево
                car_loc.x -= int(road_w / 2)
                # Ограничение позиции машины в пределах дороги
                if car_loc.left < width / 2 - road_w / 2 + roadmark_w * 2:
                    car_loc.left = width / 2 - road_w / 2 + roadmark_w * 2
            if event.key in [K_d, K_RIGHT]:
                # Переместить машину игрока вправо
                car_loc.x += int(road_w / 2)
                # Ограничение позиции машины в пределах дороги
                if car_loc.right > width / 2 + road_w / 2 - roadmark_w * 3:
                    car_loc.right = width / 2 + road_w / 2 - roadmark_w * 3
    # draw road
    screen.fill((60, 220, 0))  # Очистка экрана
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()
