import pygame
import settings
import ui


def level_1(screen, draw_pig=True):
    pig = ui.Pig()
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))


def level_2(screen, draw_pig=True):
    pig = ui.Pig()
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_3(screen, draw_pig=True):
    pig = ui.Pig()
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_4(screen, draw_pig=True):
    pig = ui.Pig()
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

def level_5(screen, draw_pig=True):
    pig = ui.Pig()
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))