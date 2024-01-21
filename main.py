import pygame
import settings
import ui
import levels
import helper


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    background = pygame.image.load(settings.start_bg)
    bird = ui.Bird()
    pig = ui.Pig()

    victory = False
    ground = False
    flyght = False
    mouse_pressed = False
    level_number = None
    existence = True
    moving = False
    running = True
    current_screen = 'Start page'
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


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
                logout_button = ui.LogoutButton(x=settings.logout_button_rect_x + 650,
                                                 y=settings.logout_button_rect_y + 300)
                background = pygame.image.load(settings.choose_level_bg)
                levels_objects = [level_button(i) for i in range(1, 4)]
                ui.draw_levels_chooise(screen, background, levels_objects, logout_button.image)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level_pressed = [levels_objects[i].check_level_button_pressed(event.pos) for i in range(3)]
                    if True in level_pressed:
                        level_number = level_pressed.index(True)
                        if settings.levels_acessibility[level_number] == 1:
                            current_screen = helper.ScreenNames.game
                            bird.rect.x = settings.bird_rect_x
                            bird.rect.y = settings.bird_rect_y
                            mouse_pressed = False
                            existence = True
                            level_start_time = pygame.time.get_ticks()
                    if logout_button.check_logout_button_pressed(event.pos):
                        running = False

            if current_screen == helper.ScreenNames.game:
                background = pygame.image.load(settings.bg)
                screen.blit(background, (0, 0))
                screen.blit(bird.image, (bird.rect.x, bird.rect.y))

                if level_number + 1 == 1:
                    current_level_ui = levels.level_1
                if level_number + 1 == 2:
                    current_level_ui = levels.level_2
                if level_number + 1 == 3:
                    current_level_ui = levels.level_3
                    victory = True
                if victory:
                    current_screen = "victory"

                pause_button = ui.PauseButton()

                pig = current_level_ui(screen, existence)

                current_level_ui(screen, existence)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.check_pause_button_pressed(event.pos):
                       current_screen = helper.ScreenNames.pause

                    if ui.bird_check_pos(bird, event.pos):
                        moving = True
                        mouse_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    moving = False
                    if mouse_pressed:
                        mouse_pressed = False
                        flyght = True
                        if (bird.rect.x, bird.rect.y) != (settings.bird_rect_x, settings.bird_rect_y):
                            k, b = helper.get_line_formula((bird.rect.x, bird.rect.y), (settings.bird_rect_x, settings.bird_rect_y))
                            for _ in range(2000):
                                if bird.out_of_screen():
                                    flyght = False
                                    current_screen = helper.ScreenNames.gameover
                                    break
                                explosion_result = pig.explosion(bird)
                                if explosion_result and existence:
                                    current_level_ui(screen)
                                else:
                                    current_level_ui(screen, False)
                                    level_finish_time = pygame.time.get_ticks()
                                    time_for_level = level_finish_time - level_start_time
                                    existence = False
                                    current_screen = "menu"
                                    break
                                bird.rect.x += 2
                                bird.rect.y = k * bird.rect.x + b

                                screen.blit(background, (0, 0))
                                screen.blit(bird.image, bird.rect)
                                current_level_ui(screen)
                                pygame.display.flip()


                if event.type == pygame.MOUSEMOTION and moving:
                    bird.rect.center = ui.bird_pulling(event.pos, bird)
                    screen.blit(background, (0, 0))
                    screen.blit(bird.image, bird.rect)
                explosion_result = pig.explosion(bird)
                if explosion_result and existence:
                    current_level_ui(screen)
                else:
                    current_level_ui(screen, False)
                    level_finish_time = pygame.time.get_ticks()
                    time_for_level = level_finish_time - level_start_time
                    existence = False
                    current_screen = "menu"

            if current_screen == 'menu':
                next_level_button = ui.NextLevel()
                logout_button = ui.LogoutButton(
                    x=settings.logout_button_rect_x + 650,
                    y=settings.logout_button_rect_y + 300
                )
                background = pygame.image.load(settings.choose_level_bg)
                ui.draw_menu_page(screen, background, next_level_button.image, logout_button.image, time_for_level)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if logout_button.check_logout_button_pressed(event.pos):
                        running = False
                    if next_level_button.check_next_level_button_pressed(event.pos):
                        current_screen = helper.ScreenNames.choose_level
                        settings.levels_acessibility[level_number + 1] = 1

            if current_screen == "gameover":
                start_over_button = ui.StartOver()
                go_to_menu_button = ui.GoToMenu(settings.go_to_menu_button_rect_x + 400, settings.go_to_menu_button_rect_y)
                background = pygame.image.load(settings.choose_level_bg)
                ui.draw_gameover_page(screen, background, start_over_button.image, go_to_menu_button.image)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_over_button.check_button_pressed(event.pos):
                        bird.rect.x = settings.bird_rect_x
                        bird.rect.y = settings.bird_rect_y
                        current_screen = helper.ScreenNames.game
                    if go_to_menu_button.check_button_pressed(event.pos):
                        current_screen = helper.ScreenNames.choose_level

            if current_screen == "victory":
                logout_button = ui.LogoutButton(
                    x=settings.logout_button_rect_x + 650,
                    y=settings.logout_button_rect_y + 300
                )
                background = pygame.image.load(settings.choose_level_bg)
                victory = pygame.image.load(settings.victory)
                ui.draw_victory_page(screen, background, logout_button.image, victory)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if logout_button.check_logout_button_pressed(event.pos):
                        running = False

            if current_screen == 'pause':
                continue_button = ui.ContinueButton()
                go_to_menu = ui.GoToMenu()
                ui.draw_pause_screen(screen, background, continue_button.image, go_to_menu.image)

                if event.type == pygame.MOUSEBUTTONDOWN:
                   if continue_button.check_button_pressed(event.pos):
                       current_screen = helper.ScreenNames.game
                   if go_to_menu.check_button_pressed(event.pos):
                       current_screen = "choose level"
            if moving:
                pygame.draw.line(screen, (0, 0, 0), [bird.rect.x + 10, bird.rect.y + 26],
                                 [settings.slingshot_rect_x + 20, settings.slingshot_rect_y + 28], 3)
                pygame.draw.line(screen, (0, 0, 0), [bird.rect.x + 48, bird.rect.y + 26],
                                 [settings.slingshot_rect_x + 55, settings.slingshot_rect_y + 32], 3)

        pygame.display.flip()
    pygame.quit()