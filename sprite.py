import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, speed, *args, **kwargs):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed


player1 = Player(100, 100)
player2 = Player(100, 100)
player3 = Player(300, 300)

screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(player1.image, (player1.rect.x, player1.rect.y))
    screen.blit(player2.image, (player2.rect.x, player2.rect.y))
    screen.blit(player3.image, (player3.rect.x, player3.rect.y))
    pygame.display.update()
    player1.update(5)
    player2.update(10)
    player3.update(10)
    clock.tick(60)

pygame.quit()
sprite1 = pygame.sprite.Sprite()
sprite1.rect = pygame.Rect(20, 20, 10, 10)
sprite2 = pygame.sprite.Sprite()
sprite2.rect = pygame.Rect(20, 20, 10, 10)

sprite3 = pygame.sprite.Sprite()

collision = pygame.sprite.collide_rect(sprite1, sprite2, )
print(collision)
