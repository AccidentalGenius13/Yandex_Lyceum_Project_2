import pygame
import settings
import ui
import Yandex_Lyceum



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    bird = ui.Bird()
    pig = ui.Pig()

    background = pygame.image.load(settings.bg)
    screen.blit(background, (0, 0))

    screen.blit(bird.image, (settings.bird_rect_x, settings.bird_rect_y))
    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))

    Yandex_Lyceum.level_1(screen)

    time_delay = 3000
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, time_delay)

    existence = True
    moving = False
    running = True
    while running:
        for event in pygame.event.get():
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
                if pig.explosion(bird) and existence:
                    screen.blit(pig.image, (settings.pig_rect_x, settings.pig_rect_y))
                else:
                    existence = False
                    boom = pygame.image.load(settings.boom_image_path)
                    screen.blit(boom, (settings.boom_rect_x, settings.boom_rect_y))
                Yandex_Lyceum.level_1(screen)
        pygame.display.flip()