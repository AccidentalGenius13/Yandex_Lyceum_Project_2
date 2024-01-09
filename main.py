import pygame
import settings
import ui



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    bird = ui.Bird()

    background = pygame.image.load(settings.bg)
    screen.blit(background, (0, 0))

    screen.blit(bird.image, (settings.bird_rect_x, settings.bird_rect_y))

    ui.level_1(screen)

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
                bird.rect.center = event.pos
                ui.bird_pulling(event.pos)
                screen.blit(background, (0, 0))
                screen.blit(bird.image, bird.rect)
                ui.level_1(screen)
        pygame.display.flip()

