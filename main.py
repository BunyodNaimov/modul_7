import pygame

pygame.init()
pygame.display.set_caption("My_Game")

screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)

icon = pygame.image.load("C:\\Users\\hacker\\PycharmProjects\\modul_7\\img.png")
pygame.display.set_icon(icon)
white = pygame.Color("yellow")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(white)
        pygame.display.update()

pygame.quit()
