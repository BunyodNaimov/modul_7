import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Coin Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

player_image = pygame.image.load("basket.jpeg")
coin_image = pygame.image.load("coin.png")

player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player_image.get_rect()
player.rect.x = 250
player.rect.y = 460

coins = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 570)
        self.rect.y = -25

    def update(self):
        self.rect.y += speed
        if self.rect.top > 600:
            self.kill()


def play_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


speed = 5
score = 0
time_live = 30
fps = 60

font = pygame.font.SysFont(None, 36)

running = True

sound = pygame.mixer.Sound("K3RDDQG-coins.mp3")
pygame.mixer.music.set_volume(0.5)

# Orqa fonga musiqa qo'yish
pygame.mixer.music.load("Gustixa_Rhianne_-_Somewhere_Only_We_Know_74895930.mp3")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pygame.mixer.music.play(-1)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    if keys[pygame.K_5]:
        play_music()

    if player.rect.left <= 0:
        player.rect.left = 0
    if player.rect.right >= 600:
        player.rect.right = 600

    if random.randint(1, 15) == 1:
        coins.add(Coin())
    coins.update()

    hit_list = pygame.sprite.spritecollide(player, coins, dokill=True)
    for i in hit_list:
        speed += 0.1
        score += 1
        sound.play()
        print(score)

    time_live -= 1 / fps
    if time_live <= 0:
        running = False

    text = font.render(f"Time Live {int(time_live)}", True, BLACK)
    score_text = font.render(f"Score : {score}", True, BLACK)

    screen.fill(WHITE)

    screen.blit(text, (440, 40))
    screen.blit(score_text, (440, 10))

    screen.blit(player.image, player.rect)

    coins.draw(screen)

    pygame.display.update()

    clock.tick(fps)
