import pygame
import settings
import ui


def level_1(screen, draw_pig=True):
    pig = ui.Pig()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_2(screen):
    pig = ui.Pig()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_3(screen):
    pig = ui.Pig()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_4(screen):
    pig = ui.Pig()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_5(screen):
    pig = ui.Pig()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))


