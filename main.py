import pygame
import settings
import ui



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size=settings.size)
    background = pygame.image.load(settings.bg)
    screen.blit(background, (0, 0))
    bird = ui.Bird()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bird.image, (settings.bird_rect_x, settings.bird_rect_y))
        pygame.display.update()

