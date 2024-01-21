import pygame
import numpy
import settings


class ScreenNames:
    choose_level = 'choose level'
    pause = "pause"
    game = "game"
    gameover = "gameover"
    victory = "victory"


def get_distance(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5


all_points = 0


def print_points(points, screen):
    global all_points
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(f'Заработано {points} очков', False, (0, 0, 0))
    all_points += points
    screen.blit(text_surface, (600, 100))


def print_all_points(screen):
    global all_points
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(f'За всю игру заработано {sum(settings.levels_points)} очков', False, (0, 0, 0))
    screen.blit(text_surface, (520, 300))


def get_points_by_time(time):
    return round(1 / time * 1000000)


def get_line_formula(first, second):
    m_1 = numpy.array([[float(first[0]), 1.], [float(second[0]), 1.]])
    v_1 = numpy.array([float(first[1]), float(second[1])])
    res = numpy.linalg.solve(m_1, v_1)
    return res[0], res[1]
