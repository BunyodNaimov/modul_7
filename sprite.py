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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
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


group_players = pygame.sprite.Group()
group_players.add(Player(100, 500), Player(400, 500))

group_enemies = pygame.sprite.Group()
group_enemies.add(Enemy(100, 100), Enemy(200, 100))

screen = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    group_players.draw(screen)

    group_enemies.draw(screen)

    pygame.display.update()

    group_players.update(5)

    clock.tick(60)

pygame.quit()
