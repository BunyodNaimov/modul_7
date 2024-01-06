import pygame

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
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_a, pygame.K_LEFT]:
                car_loc.left -= int(road_w / 2)
                if car_loc.left <= 150:
                    car_loc.left = 150

                print(f"chap {car_loc.left}\n chap {car_loc.right}")

            if event.key in [pygame.K_d, pygame.K_RIGHT]:
                car_loc.right += int(road_w / 2)
                if car_loc.right >= 650:
                    car_loc.right = 650

                print(f"o'ng {car_loc.left}\n o'ng {car_loc.right}")

    screen.fill((60, 220, 0))
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

    screen.blit(car, car_loc)
    pygame.display.update()
