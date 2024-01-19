import datetime
import pygame

class ScreenNames:
    choose_level = 'choose level'
    pause = "pause"
    game = "game"


def get_distance(first, second):
    return ((first[0] - second[0])**2 + (first[1] - second[1])**2)**0.5


def get_angle_trigonometry(first, second):
    x = abs(second[0] - first[0])
    y = abs(second[1] - first[1])
    gip = get_distance(first, second)
    trigonometry = {
        'sin': y / gip,
        'cos': x / gip,
        'tg': y / x,
        'ctg': x / y
    }
    return trigonometry

def write_level_results_to_txt(level_number, level_time):
    with open('logs.txt', 'a') as logs_file:
        logs_file.write(f'В {datetime.datetime.now()} пройден уровень {level_number + 1}. Получено {level_time} очков')


def print_points(points, screen):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(f'Заработано {points} очков', False, (0, 0, 0))
    screen.blit(text_surface, (500, 500))

class Button:
    def check_button_pressed(self, pos):
        pass

