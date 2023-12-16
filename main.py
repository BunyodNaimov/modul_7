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


# import pygame
#
# window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         window.fill('white')
#
#         # boshi
#         pygame.draw.circle(window, 'orange', [220, 60], 40, 0)
#         # ko'zlari
#         pygame.draw.rect(window, 'black', [200, 40, 10, 10])
#         pygame.draw.rect(window, 'black', [230, 40, 10, 10])
#
#         # og'zi
#         pygame.draw.rect(window, 'red', [200, 70, 40, 10])
#
#         # tanasi
#         pygame.draw.line(window, 'blue', [220, 100], [220, 350], 7)
#
#         pygame.draw.line(window, 'orange', [220, 150], [120, 230], 7)
#         pygame.draw.line(window, 'orange', [220, 150], [320, 230], 7)
#
#         pygame.draw.line(window, 'black', [220, 350], [120, 470], 7)
#         pygame.draw.line(window, 'black', [220, 350], [320, 470], 7)
#
#         pygame.display.update()
#
# pygame.quit()

# import pygame
# pygame.init()
#
# # Set up the display
# screen = pygame.display.set_mode((640, 480))
#
# # Start the event loop
# running = True
# while running:
#     # Check for new events
#     for event in pygame.event.get():
#         # Handle the event
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             # Print information about the key press
#             print("Klavish bosildi: ", event.key, event.unicode, event.mod)
#         elif event.type == pygame.KEYUP:
#             # Print information about the key release
#             print("Klavish qo`yib yuborildi:", event.key)
#
# # Quit Pygame
# pygame.quit()


# import pygame
#
# pygame.init()
#
# MY_EVENT = pygame.USEREVENT + 1
# my_event = pygame.event.Event(MY_EVENT, message="Hello D13")
#
# pygame.event.post(my_event)
#
# window = pygame.display.set_mode((500, 600))
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running == False
#
#         if event.type == MY_EVENT:
#             print(event.message)
#         # elif event.type == pygame.KEYDOWN:
#         #     print(f"Klaviatura bosildi: {event.key}")
#         #
#         # elif event.type == pygame.KEYUP:
#         #     print(f"Klaviatura qo'yib yuborildi: {event.unicode}")
#
#         # elif event.type == pygame.MOUSEBUTTONDOWN:
#         #
#         #     print(f"Sichqoncha bosildi! {event.pos}")
#         # elif event.type == pygame.MOUSEBUTTONUP:
#         #     print(f"Sichqoncha qo'yib yuborildi! {event.pos}")
#         #
#         # elif event.type == pygame.MOUSEMOTION:
#         #     print(f"Sichqoncha harakatda: {event.pos, event.rel}")
#
#         window.fill('black')
#
#         pygame.display.update()
#
# pygame.quit()

import pygame
import random

pygame.init()

window = pygame.display.set_mode((400, 400))

balloons_color = ['green', 'blue', 'red', ]
balloon_width = 20
balloon_height = 30
balloon_num = 10

balloons = []

for i in range(balloon_num):
    x = random.randint(0, window.get_width() - balloon_width)
    y = random.randint(window.get_height() // 2, window.get_height() - balloon_height)
    color = random.choice(balloons_color)
    balloon_rect = pygame.draw.ellipse(window, color, (x, y, balloon_width, balloon_height))

    tail_start_x = x + balloon_width // 2
    tail_start_y = y + balloon_height
    tail_end_x = tail_start_x
    tail_end_y = tail_start_y + random.randint(10, +20)
    pygame.draw.line(window, color, (tail_start_x, tail_start_y), (tail_end_x, tail_end_y))

    balloons.append((balloon_rect, color))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i in range(len(balloons)):
                balloon_rect, color = balloons[i]
                if balloon_rect.collidepoint(mouse_pos):
                    balloons.pop(i)
                    # counter
                    break

    for i in range(len(balloons)):
        balloon_rect, color = balloons[i]
        balloon_rect.move_ip(0, -5)
        if balloon_rect.bottom < 0:
            balloon_rect.bottom = window.get_height()

    window.fill('white')

    for i in range(len(balloons)):
        balloon_rect, color = balloons[i]
        pygame.draw.ellipse(window, color, balloon_rect)

        tail_start_x = balloon_rect.x + balloon_width // 2
        tail_start_y = balloon_rect.y + balloon_height
        tail_end_x = tail_start_x
        tail_end_y = tail_start_y + random.randint(10, +20)
        pygame.draw.line(window, color, (tail_start_x, tail_start_y), (tail_end_x, tail_end_y))

    pygame.display.flip()
    pygame.time.wait(100)
