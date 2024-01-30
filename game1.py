import pygame
import random
from pygame.locals import *

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("jet.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        print("OK")
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("missile.png")
        self.image.set_colorkey((255, 255, 255))
        self.speed = random.randint(2, 6)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()
enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

FPS = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()



    for i in all_sprites:
        screen.blit(i.image, i.rect)
    player.update(pressed_keys)
    enemies.update()

    pygame.display.flip()

    pygame.display.update()

    clock.tick(FPS)
