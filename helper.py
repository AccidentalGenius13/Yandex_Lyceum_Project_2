import pygame
import numpy

class ScreenNames:
    choose_level = 'choose level'
    pause = "pause"
    game = "game"
    gameover = "gameover"


def get_distance(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5


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


def print_points(points, screen):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(f'Заработано {points} очков', False, (0, 0, 0))
    screen.blit(text_surface, (600, 100))

def get_line_formula(first, second):
    m_1 = numpy.array([[float(first[0]), 1.], [float(second[0]), 1.]])
    v_1 = numpy.array([float(first[1]), float(second[1])])
    res = numpy.linalg.solve(m_1, v_1)
    return res[0], res[1]

