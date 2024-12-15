from pygame import *

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Прокачка автомобиля")

# Загрузка текстур
car_images = [
    pygame.image.load('png-clipart-car-graphic-design-vehicles-compact-car-car-thumbnail-removebg-preview.png'),
    pygame.image.load('pngtree-realistic-black-sedan-vector-car-template-flat-vector-vector-png-image_1247295.jpg'),
    pygame.image.load('images__2_-removebg-preview.png'),
    pygame.image.load('images.png')
]

# Загрузка звуков
click_sound = pygame.mixer.Sound('knopka-schelchok-chetkii-myagkii1.wav')
pygame.mixer.music.load('24b0d8ed4ae4cb2.mp3')
pygame.mixer.music.play(-1)  # Зацикливание музыки

# Игровые переменные
car_stage = 0
level = 1
coins = 0
font = pygame.font.Font(None, 36)
car_rect = car_images[car_stage].get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Основное меню
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        title_text = font.render("Прокачка автомобиля", True, (0, 0, 0))
        start_text = font.render("Нажмите ENTER, чтобы начать", True, (0, 0, 0))
        exit_text = font.render("Нажмите ESC, чтобы выйти", True, (0, 0, 0))
        shop_text = font.render("Нажмите S, чтобы открыть магазин", True, (0, 0, 0))

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 40))
        screen.blit(shop_text, (WIDTH // 2 - shop_text.get_width() // 2, HEIGHT // 2 + 80))

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game_loop()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_s]:
            puzzle_game()

# Основной цикл игры
def game_loop():
    global car_stage, level, coins, car_rect
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    coins += 1
                    click_sound.play()  # Воспроизведение звука клика
                    if coins >= 70:
                        coins = 0  # Сбрасываем монеты на 0 при прокачке
                        car_stage += 1
                        if car_stage >= len(car_images):  # Если достигли последней стадии
                            car_stage = 0
                            level += 1  # Увеличиваем уровень прокачки
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Открытие меню
                    main_menu()

        # Заполнение фона
        screen.fill((255, 255, 255))

        # Рисуем автомобиль
        screen.blit(car_images[car_stage], car_rect)

        # Отображение количества монет и уровня прокачки
        coins_text = font.render(f"Монеты: {coins}", True, (0, 0, 0))
        level_text = font.render(f"Уровень: {level}", True, (0, 0, 0))
        screen.blit(coins_text, (10, 10))
        screen.blit(level_text, (10, 50))

        # Обновляем экран
        pygame.display.flip()
        clock.tick(30)

# Мини-игра с нажатием на изображение
def puzzle_game():
    clock = pygame.time.Clock()
    puzzle_image = pygame.image.load('kjdkf.jpg')  # Используем первую стадию как изображение
    puzzle_rect = puzzle_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    mini_game_active = True

    while mini_game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    if puzzle_rect.collidepoint(event.pos):
                        global coins
                        coins += 30  # Даем монеты за нажатие
                        mini_game_active = False  # Завершаем мини-игру

        # Заполнение фона
        screen.fill((255, 255, 255))

        # Рисуем изображение
        screen.blit(puzzle_image, puzzle_rect)

        # Обновляем экран
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()