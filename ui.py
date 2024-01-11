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

    def explosion(self, object_2):
        if self.rect.colliderect(object_2):
            return False
        else:
            return True
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

