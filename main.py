import pygame
import settings
import ui
import Yandex_Lyceum



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    background = pygame.image.load(settings.start_bg)
    bird = ui.Bird()
    pig = ui.Pig()

    mouse_pressed = False
    level_number = None
    existence = True
    moving = False
    running = True
    current_screen = 'Start page'
    while running:
        for event in pygame.event.get():
            if current_screen == 'Start page':
                start_button = ui.StartButton()
                logout_button = ui.LogoutButton()
                background = pygame.image.load(settings.start_bg)
                button = pygame.image.load(settings.start_button_image_path)
                logout = pygame.image.load(settings.logout_button_image_path)
                ui.draw_start_page(screen, background, button, logout)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.check_start_button_pressed(event.pos):
                        current_screen = 'choose level'
                    if logout_button.check_logout_button_pressed(event.pos):
                        running = False

            if current_screen == 'choose level':
                level_button = ui.LevelButton
                background = pygame.image.load(settings.choose_level_bg)
                levels_objects = [level_button(i) for i in range(1, 6)]
                ui.draw_levels_chooise(screen, background, levels_objects)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level_pressed = [levels_objects[i].check_level_button_pressed(event.pos) for i in range(5)]
                    if True in level_pressed:
                        level_number = level_pressed.index(True)
                        if settings.levels_acessibility[level_number] == 1:
                            current_screen = 'game'

            if event.type == pygame.QUIT:
                running = False



            if current_screen == 'game':
                background = pygame.image.load(settings.bg)
                screen.blit(background, (0, 0))
                screen.blit(bird.image, (bird.rect.x, bird.rect.y))

                if level_number + 1 == 1:
                    current_level_ui = Yandex_Lyceum.level_1
                if level_number + 1 == 2:
                    current_level_ui = Yandex_Lyceum.level_2
                if level_number + 1 == 3:
                    current_level_ui = Yandex_Lyceum.level_3
                if level_number + 1 == 4:
                    current_level_ui = Yandex_Lyceum.level_4
                if level_number + 1 == 5:
                    current_level_ui = Yandex_Lyceum.level_5

                current_level_ui(screen, existence)

                """pause_button = ui.PauseButton()
                button = pygame.image.load(settings.pause_button)
                ui.draw_pause_screen(screen, background, button)

                current_level_ui(screen, existence)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.check_pause_button_pressed(event.pos):
                        current_screen = 'pause'"""


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ui.bird_check_pos(bird, event.pos):
                        moving = True
                        mouse_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    moving = False
                    if mouse_pressed:
                        #bird.flyght(event.pos, screen)
                        mouse_pressed = False
                if event.type == pygame.MOUSEMOTION and moving:
                    bird.rect.center = ui.bird_pulling(event.pos, bird)
                    screen.blit(background, (0, 0))
                    screen.blit(bird.image, bird.rect)
                    explosion_result = pig.explosion(bird)
                    if explosion_result and existence:
                        current_level_ui(screen)
                    else:
                        current_level_ui(screen, False)
                        existence = False
                        current_screen = "menu"

            if current_screen == 'menu':
                next_level_button = ui.NextLevel()
                logout_button = ui.LogoutButton()
                background = pygame.image.load(settings.choose_level_bg)
                button = pygame.image.load(settings.next_level_button)
                logout = pygame.image.load(settings.logout_button_image_path)
                ui.draw_menu_page(screen, background, button, logout)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if logout_button.check_logout_button_pressed(event.pos):
                        running = False
                    if next_level_button.check_next_level_button_pressed(event.pos):
                        current_screen = 'level'


        pygame.display.flip()
    pygame.quit()