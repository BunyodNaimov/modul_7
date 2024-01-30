import pygame
import random

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 500))

sound = pygame.mixer.Sound("K3RDDQG-coins.mp3")

pygame.mixer.music.load("Gustixa_Rhianne_-_Somewhere_Only_We_Know_74895930.mp3")

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)


class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("photo_2024-01-25_16-56-05.jpg")

        # self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 480)
        self.rect.y = -25

    def update(self):
        self.rect.y += 5
        if self.rect.top > 500:
            self.kill()


all_sprites = pygame.sprite.Group()
rects = pygame.sprite.Group()

player = pygame.sprite.Sprite()

player.image = pygame.image.load("jet.png")
player.rect = player.image.get_rect()
player.rect.center = (240, 240)
all_sprites.add(player)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.rect.x -= 3
    if keys[pygame.K_d]:
        player.rect.x += 3
    if keys[pygame.K_w]:
        player.rect.y -= 3
    if keys[pygame.K_s]:
        player.rect.y += 3

    if player.rect.left <= 0:
        player.rect.left = 0
    if player.rect.right >= 500:
        player.rect.right = 500
    if player.rect.top <= 0:
        player.rect.top = 0
    if player.rect.bottom >= 500:
        player.rect.bottom = 500

    if random.randint(0, 100) < 2:
        rect = Rect()
        all_sprites.add(rect)
        rects.add(rect)

    all_sprites.update()
    for rect in rects:
        if pygame.sprite.collide_rect(rect, player):
            pass
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
