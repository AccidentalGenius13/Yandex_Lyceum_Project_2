import pygame
import settings

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.bird_image_path)
        self.rect = self.image.get_rect()

def bird_check_pos(bird, position):
    bird_width = bird.rect[2]
    bird_height = bird.rect[3]
    return settings.bird_rect_x <= position[0] <= settings.bird_rect_x + bird_width and \
            settings.bird_rect_y <= position[1] <= settings.bird_rect_y + bird_height

def bird_pulling(mouse_pos):
    bird = Bird()
    left_border = settings.bird_rect_x - 100
    right_border = settings.bird_rect_x + 20
    bottom_border = settings.bird_rect_y + 20
    top_border = settings.bird_rect_y - 100

    print("left_border", left_border)
    print("right_border", right_border)
    print("bottom_border", bottom_border)
    print("top_border", top_border)
    print("mouse_pos[0]", mouse_pos[0])

    if mouse_pos[0] < left_border:
        bird.rect.center = (left_border, mouse_pos[1])
    if mouse_pos[0] > right_border:
        bird.rect.centerx = right_border
    if mouse_pos[1] > bottom_border:
        bird.rect.centery = bottom_border
    if mouse_pos[1] < top_border:
        bird.rect.centery = top_border


def level_1(screen):
    slingshot = pygame.image.load(settings.slingshot_image_path)
    screen.blit(slingshot, (settings.slingshot_rect_x, settings.slingshot_rect_y))

    for i in 0, 105:
        column_vertical = pygame.image.load(settings.column_vertical_image_path)
        screen.blit(column_vertical, (settings.column_vertical_rect_x + i, settings.column_vertical_rect_y))

    column_horizontal = pygame.image.load(settings.column_horizontal_image_path)
    screen.blit(column_horizontal, (settings.column_horizontal_rect_x, settings.column_horizontal_rect_y))

    pig = pygame.image.load(settings.pig_image_path)
    screen.blit(pig, (settings.pig_rect_x, settings.pig_rect_y))
