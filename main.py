# import pygame
#
# pygame.init()
# pygame.display.set_caption("My_Game")
#
# screen = pygame.display.set_mode((400, 500), pygame.RESIZABLE)
#
# icon = pygame.image.load("C:\\Users\\hacker\\PycharmProjects\\modul_7\\img.png")
# pygame.display.set_icon(icon)
# white = pygame.Color("yellow")
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         screen.fill(white)
#         pygame.display.update()
#
# pygame.quit()


# import pygame
#
# window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         window.fill('white')
#
#         # pygame.draw.rect(window, 'green', [0, 500, 400, 500])
#         pygame.draw.rect(window, 'green', [0, 400, 500, 120], 0)
#
#         # left tree
#         pygame.draw.rect(window, 'brown', [50, 300, 30, 100])
#         pygame.draw.rect(window, '#008000', [50, 280, 30, 30])
#         # right tree
#         pygame.draw.rect(window, 'brown', [420, 300, 30, 100])
#         pygame.draw.rect(window, '#008000', [420, 280, 30, 30])
#
#         # House
#         pygame.draw.rect(window, '#5F9EA0', [100, 120, 300, 280])
#
#         # uyni tomi
#         pygame.draw.polygon(window, 'red', [[65, 120], [430, 120], [245, 5]])
#         # uyni oynalari
#         pygame.draw.rect(window, 'black', [125, 140, 30, 30])
#         pygame.draw.rect(window, 'black', [230, 140, 30, 30])
#         pygame.draw.rect(window, 'black', [330, 140, 30, 30])
#
#         pygame.draw.rect(window, 'black', [125, 200, 30, 30])
#         pygame.draw.rect(window, 'black', [230, 200, 30, 30])
#         pygame.draw.rect(window, 'black', [330, 200, 30, 30])
#
#         pygame.draw.rect(window, 'black', [125, 260, 30, 30])
#         pygame.draw.rect(window, 'black', [230, 260, 30, 30])
#         pygame.draw.rect(window, 'black', [330, 260, 30, 30])
#
#         # Uyni eshiklari
#         pygame.draw.rect(window, 'white', [190, 335, 30, 65])
#         pygame.draw.rect(window, 'white', [290, 335, 30, 65])
#
#         pygame.draw.rect(window, 'black', [200, 360, 20, 10])
#         pygame.draw.rect(window, 'black', [290, 360, 20, 10])
#
#
#         pygame.display.update()
#
# pygame.quit()


import pygame

window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        window.fill('white')

        # boshi
        pygame.draw.circle(window, 'orange', [220, 60], 40, 0)
        # ko'zlari
        pygame.draw.rect(window, 'black', [200, 40, 10, 10])
        pygame.draw.rect(window, 'black', [230, 40, 10, 10])

        # og'zi
        pygame.draw.rect(window, 'red', [200, 70, 40, 10])

        # tanasi
        pygame.draw.line(window, 'blue', [220, 100], [220, 350], 7)

        pygame.draw.line(window, 'orange', [220, 150], [120, 230], 7)
        pygame.draw.line(window, 'orange', [220, 150], [320, 230], 7)

        pygame.draw.line(window, 'black', [220, 350], [120, 470], 7)
        pygame.draw.line(window, 'black', [220, 350], [320, 470], 7)

        pygame.display.update()

pygame.quit()
