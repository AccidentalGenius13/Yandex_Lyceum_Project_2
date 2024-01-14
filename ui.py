import math

import pygame
import settings

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.bird_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.bird_rect_x
        self.rect.y = settings.bird_rect_y


class Pig(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.pig_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.pig_rect_x
        self.rect.y = settings.pig_rect_y
        self.was_explosion = False

    def explosion(self, object_2):
        if self.rect.colliderect(object_2):
            if not self.was_explosion:
                self.time_appear = pygame.time.get_ticks()
                print(self.time_appear)
                self.was_explosion = True
            return False, self.time_appear
        else:
            return True, math.inf

class Boom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.boom_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.boom_rect_x
        self.rect.y = settings.boom_rect_y
        self.remove = False

    def update(self):
        if self.remove:
            self.kill()

def bird_check_pos(bird, position):
    x = bird.rect[0]
    y = bird.rect[1]
    bird_width = bird.rect[2]
    bird_height = bird.rect[3]

    return x <= position[0] <= x + bird_width and \
            y <= position[1] <= y + bird_height

def bird_pulling(mouse_pos, bird):
    bird.rect.center = mouse_pos
    basic_center_x = settings.bird_rect_x + (bird.rect[2] // 2)
    basic_center_y = settings.bird_rect_y + (bird.rect[3] // 2)

    left_border = basic_center_x - 100
    right_border = basic_center_x + 100
    bottom_border = basic_center_y + 100
    top_border = basic_center_y - 100

    """if mouse_pos[0] < left_border:
        mouse_pos = (left_border, mouse_pos[1])
    if mouse_pos[0] > right_border:
        mouse_pos = (right_border, mouse_pos[1])
    if mouse_pos[1] > bottom_border:
        mouse_pos = (mouse_pos[0], bottom_border)
    if mouse_pos[1] < top_border:
        mouse_pos = (mouse_pos[0], top_border)"""
    bird.rect.center = mouse_pos
    return mouse_pos


class StartButton((pygame.sprite.Sprite)):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.start_button_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.start_button_rect_x
        self.rect.y = settings.start_button_rect_y

    def check_start_button_pressed(self, position):
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
                button_y <= mouse_y <= button_y + button_height

class level_button(pygame.sprite.Sprite):
    def __init__(self, level_number):
        super().__init__()
        self.level_number = level_number
        image_path = f'images/level_{self.level_number}.jpg' if settings.levels_acessibility[self.level_number - 1] == 1 else 'images/block_level.jpg'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.levels_base_x + (settings.image_width + settings.levels_space) * self.level_number - 1
        self.rect.y = settings.levels_y

def draw_levels_chooise(screen, background, levels_objects):
    screen.blit(background, (0, 0))
    for each_level in levels_objects:
        screen.blit(each_level.image, (each_level.rect.x, each_level.rect.y))

def draw_start_page(screen, background, button):
    screen.blit(background, (0, 0))
    screen.blit(button, (settings.start_button_rect_x, settings.start_button_rect_y))


