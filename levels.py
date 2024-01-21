import pygame
import settings
import ui


def level_1(screen, draw_pig=True):
    pig = ui.Pig(x=settings.pig_rect_x,
                        y=settings.pig_rect_y)
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
    return pig


def level_2(screen, draw_pig=True):
    pig = ui.Pig(x=settings.pig_rect_x - 10,
                        y=settings.pig_rect_y - 160)
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        for j in 0, 78, 156:
            screen.blit(column_vertical.image,
                        (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y - j))

    for i in 0, 78, 156:
        screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y - i))
    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x - 10, settings.pig_rect_y - 160))
    return pig

def level_3(screen, draw_pig=True):
    pig = ui.Pig(x=settings.pig_rect_x - 5,
                        y=settings.pig_rect_y - 350)
    pause_button = ui.PauseButton()
    column_vertical = ui.ColumnVertical()
    column_horizontal = ui.ColumnHorizontal()
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        for j in 0, 78, 156:
            screen.blit(column_vertical.image,
                        (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y - j))
    for j in 234, 300, 366:
        screen.blit(column_vertical.image, (settings.column_vertical_rect_x + 50, settings.column_vertical_rect_y - j))

    for i in 0, 78, 156:
        screen.blit(column_horizontal.image, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y - i))

    screen.blit(pause_button.image, (settings.pause_button_rect_x, settings.pause_button_rect_y))

    if draw_pig:
        screen.blit(pig.image, (settings.pig_rect_x - 5, settings.pig_rect_y - 350))
    return pig

