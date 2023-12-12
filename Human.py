import pygame

# initialize game engine
pygame.init()

clock = pygame.time.Clock()

size = [500, 500]
global screen
surface = pygame.display.set_mode(size)

# Initialize values for color (RGB format)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

HEAD = (214, 195, 54)

dead = False
surface.fill(WHITE)

global positionMove
positionMove = 0

while (dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        surface.fill(WHITE)

        # Draw head
        pygame.draw.circle(surface, HEAD, [220, 60], 40, 0)
        pygame.draw.line(surface, BLUE, [220, 100], [220, 350], 5)

        # Draw hands
        pygame.draw.line(surface, HEAD, [220, 150], [120, 230], 5)
        pygame.draw.line(surface, HEAD, [220, 150], [320, 230], 5)

        # Draw legs
        pygame.draw.line(surface, BLACK, [220, 350], [120, 470], 5)
        pygame.draw.line(surface, BLACK, [220, 350], [320, 470], 5)

        # Draw Eyes
        pygame.draw.rect(surface, BLACK, [200, 40, 10, 10], 0)
        pygame.draw.rect(surface, BLACK, [230, 40, 10, 10], 0)

        # Draw lips
        pygame.draw.rect(surface, RED, [200, 70, 40, 10], 0)

        # Draw Name
        font = pygame.font.SysFont('Calibri', 25, True, True)
        text = font.render("I am Kiran", True, GREEN)

        positionMove += 5
        if (positionMove == 350):
            positionMove = 5
        surface.blit(text, [positionMove, 0])

        pygame.display.flip()
        clock.tick(5)

# Shutdown display module
pygame.display.quit()
