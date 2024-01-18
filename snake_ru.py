# импорт необходимых библиотек
import pygame
import time
import random

# скорость движения змейки
snake_speed = 15

# размер окна
window_x = 720
window_y = 480

# определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Инициализация pygame
pygame.init()

# Инициализация игрового окна
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS (кадров в секунду)
fps = pygame.time.Clock()

# Задание начальной позиции змейки
snake_position = [100, 50]

# Задание первых 4 блоков тела змейки
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Позиция фрукта
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# Задание начального направления движения змейки (вправо)
direction = 'RIGHT'
change_to = direction

# Начальный счет
score = 0


# Функция отображения счета
def show_score(choice, color, font, size):
    # Создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

    # Создание поверхности для отображения счета
    score_surface = score_font.render('Счет: ' + str(score), True, color)

    # Создание прямоугольника для текстовой поверхности
    score_rect = score_surface.get_rect()

    # Отображение текста
    game_window.blit(score_surface, score_rect)


# Функция окончания игры
def game_over():
    # Создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # Создание текстовой поверхности с сообщением о счете
    game_over_surface = my_font.render(
        'Ваш счет: ' + str(score), True, red)

    # Создание прямоугольника для текстовой поверхности
    game_over_rect = game_over_surface.get_rect()

    # Установка позиции текста
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # Отображение текста
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Пауза в 2 секунды перед завершением программы
    time.sleep(2)

    # Деактивация библиотеки pygame
    pygame.quit()

    # Завершение программы
    quit()


# Основная функция
while True:

    # Обработка событий клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Если две клавиши нажаты одновременно,
    # мы не хотим, чтобы змейка двигалась в двух
    # направлениях одновременно
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Движение змейки
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Механизм увеличения тела змейки
    # если змейка сталкивается с фруктом, то счет увеличивается на 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Условия завершения игры
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Столкновение с телом змейки
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Отображение счета
    show_score(1, white, 'times new roman', 20)

    # Обновление экрана игры
    pygame.display.update()

    # Частота обновления экрана (кадров в секунду)
    fps.tick(snake_speed)
