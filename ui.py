import pygame
import helper
import settings



class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.bird_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.bird_rect_x
        self.rect.y = settings.bird_rect_y

    def out_of_screen(self):
        if self.rect.x < 0 or self.rect.x > settings.width:
            return True
        if self.rect.y < 0 or self.rect.y > settings.height:
            return True
        return False


class Pig(pygame.sprite.Sprite):
    def __init__(self, x=settings.pig_rect_x, y=settings.pig_rect_y):
        super().__init__()
        self.image = pygame.image.load(settings.pig_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.was_explosion = False

    def explosion(self, object_2):
        if self.rect.colliderect(object_2):
            if not self.was_explosion:
                self.was_explosion = True
            return False
        else:
            return True



def bird_check_pos(bird, position):
    print(bird.rect, position)
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
    right_border = basic_center_x + 10
    bottom_border = basic_center_y + 100
    top_border = basic_center_y - 300

    if mouse_pos[0] < left_border:
        mouse_pos = (left_border, mouse_pos[1])
    if mouse_pos[0] > right_border:
        mouse_pos = (right_border, mouse_pos[1])
    if mouse_pos[1] > bottom_border:
        mouse_pos = (mouse_pos[0], bottom_border)
    if mouse_pos[1] < top_border:
        mouse_pos = (mouse_pos[0], top_border)
    bird.rect.center = mouse_pos
    return mouse_pos

class ColumnVertical(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.column_vertical_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.column_vertical_rect_x
        self.rect.y = settings.column_vertical_rect_y

class ColumnHorizontal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.column_horizontal_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.column_horizontal_rect_x
        self.rect.y = settings.column_horizontal_rect_y

class StartButton(pygame.sprite.Sprite):
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

class LogoutButton(pygame.sprite.Sprite):
    def __init__(self, x=settings.logout_button_rect_x, y=settings.logout_button_rect_y):
        super().__init__()
        self.image = pygame.image.load(settings.logout_button_image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_logout_button_pressed(self, position):
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height


class LevelButton(pygame.sprite.Sprite):
    def __init__(self, level_number):
        super().__init__()
        self.level_number = level_number
        image_path = f'images/level_{self.level_number}.jpg' \
            if settings.levels_acessibility[self.level_number - 1] == 1 else 'images/block_level.jpg'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = settings.levels_base_x + (settings.image_width + settings.levels_space) * self.level_number - 1
        self.rect.y = settings.levels_y

    def check_level_button_pressed(self, position):
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height


class PauseButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.pause_button)
        self.rect = self.image.get_rect()
        self.rect.x = settings.pause_button_rect_x
        self.rect.y = settings.pause_button_rect_y

    def check_pause_button_pressed(self, position):
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height

class NextLevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.next_level_button)
        self.rect = self.image.get_rect()
        self.rect.x = settings.next_level_button_rect_x
        self.rect.y = settings.next_level_button_rect_y

    def check_next_level_button_pressed(self, position):
        print(self.rect, position)
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height

class ContinueButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.continue_button)
        self.rect = self.image.get_rect()
        self.rect.x = settings.continue_button_rect_x
        self.rect.y = settings.continue_button_rect_y

    def check_button_pressed(self, position):
        print('here', self.rect, position)
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height

class StartOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(settings.start_over_button)
        self.rect = self.image.get_rect()
        self.rect.x = settings.start_over_button_rect_x
        self.rect.y = settings.start_over_button_rect_y

    def check_button_pressed(self, position):
        print('here', self.rect, position)
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height


class GoToMenu(pygame.sprite.Sprite):
    def __init__(self, x=settings.logout_button_rect_x, y=settings.logout_button_rect_y):
        super().__init__()
        self.image = pygame.image.load(settings.go_to_menu_button)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_button_pressed(self, position):
        print('here', self.rect, position)
        mouse_x = position[0]
        mouse_y = position[1]
        button_x = self.rect.x
        button_y = self.rect.y
        button_width = self.rect[2]
        button_height = self.rect[3]
        return button_x <= mouse_x <= button_x + button_width and \
            button_y <= mouse_y <= button_y + button_height

def draw_levels_chooise(screen, background, levels_objects, logout_btn):
    screen.blit(background, (0, 0))
    for each_level in levels_objects:
        screen.blit(each_level.image, (each_level.rect.x, each_level.rect.y))
    screen.blit(logout_btn, (settings.logout_button_rect_x + 650, settings.logout_button_rect_y + 300))


def draw_start_page(screen, background, button, logout_btn):
    screen.blit(background, (0, 0))
    screen.blit(button, (settings.start_button_rect_x, settings.start_button_rect_y))
    screen.blit(logout_btn, (settings.logout_button_rect_x, settings.logout_button_rect_y))

def draw_pause_screen(screen, background, play_button, go_to_menu_button):
    screen.blit(background, (0, 0))
    screen.blit(play_button, (settings.continue_button_rect_x, settings.continue_button_rect_y))
    screen.blit(go_to_menu_button, (settings.go_to_menu_button_rect_x, settings.go_to_menu_button_rect_y))

def draw_menu_page(screen, background, button, logout_btn, points):
    screen.blit(background, (0, 0))
    screen.blit(button, (settings.next_level_button_rect_x, settings.next_level_button_rect_y))
    screen.blit(logout_btn, (settings.logout_button_rect_x + 650, settings.logout_button_rect_y + 300))
    helper.print_points(round(1 / points * 1000000), screen)

def draw_gameover_page(screen, background, start_over, go_to_menu):
    screen.blit(background, (0, 0))
    screen.blit(start_over, (settings.start_over_button_rect_x, settings.start_over_button_rect_y))
    screen.blit(go_to_menu, (settings.go_to_menu_button_rect_x + 400, settings.go_to_menu_button_rect_y))