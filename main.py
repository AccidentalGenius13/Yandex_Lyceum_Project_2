import pygame
import settings
import ui
import Yandex_Lyceum



if __name__ == '__main__':
    pygame.init()
    Yandex_Lyceum.start_window()
    screen = pygame.display.set_mode(size=settings.size)
    bird = ui.Bird()
    pig = ui.Pig()
    boom = ui.Boom()

    background = pygame.image.load(settings.bg)
    screen.blit(background, (0, 0))

    screen.blit(bird.image, (settings.bird_rect_x, settings.bird_rect_y))
    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

    Yandex_Lyceum.level_1(screen)

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
                background = pygame.image.load(settings.start_bg)
                button = pygame.image.load(settings.start_button_image_path)
                ui.draw_start_page(screen, background, button)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.check_start_button_pressed(event.pos):
                        current_screen = 'choose level'
                        print(current_screen)

            if current_screen == 'choose level':
                background = pygame.image.load(settings.start_bg)
                levels_objects = [ui.level_button(i) for i in range(1, 3)]
                ui.draw_levels_chooise(screen, background, levels_objects)

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