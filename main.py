import pygame
import settings
import ui
import Yandex_Lyceum



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    bird = ui.Bird()
    pig = ui.Pig()
    boom = ui.Boom()

    boom_time = 10000000

    existence = True
    moving = False
    running = True
    current_screen = 'Start page'
    while running:
        now = pygame.time.get_ticks()
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
                        print(current_screen)
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
                            current_screen = f'level {level_number + 1}'

            if current_screen == 'level 1':
                background = pygame.image.load(settings.bg)
                screen.blit(background, (0, 0))
                screen.blit(bird.image, (settings.bird_rect_x, settings.bird_rect_y))
                Yandex_Lyceum.level_1(screen)

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ui.bird_check_pos(bird, event.pos):
                    moving = True
            if event.type == pygame.MOUSEBUTTONUP:
                moving = False
            if event.type == pygame.MOUSEMOTION and moving:
                bird.rect.center = ui.bird_pulling(event.pos, bird)
                screen.blit(background, (0, 0))
                screen.blit(bird.image, bird.rect)
                explosion_result = pig.explosion(bird)
                if explosion_result[0] and existence:
                    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))
                else:
                    existence = False
                    screen.blit(boom.image, (settings.boom_rect_x, settings.boom_rect_y))
                    boom_time = explosion_result[1]
                Yandex_Lyceum.level_1(screen)
            if now - boom_time > 3000:
                screen.blit(background, (0, 0))
                screen.blit(bird.image, bird.rect)
                Yandex_Lyceum.level_1(screen)

        pygame.display.flip()
    pygame.quit()