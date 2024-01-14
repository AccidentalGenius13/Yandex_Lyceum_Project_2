import pygame
import settings
def level_1(screen):
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

def start_window():
    screen = pygame.display.set_mode((300, 300))
    screen.fill((0, 0, 0))

    start_button = pygame.image.load(settings.start_button_image_path)
    screen.blit(start_button, (settings.start_button_rect_x, settings.start_button_rect_y))

    logout_button = pygame.image.load(settings.logout_button_image_path)
    screen.blit(logout_button, (settings.logout_button_rect_x, settings.logout_button_rect_y))


