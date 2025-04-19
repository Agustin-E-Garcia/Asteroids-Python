import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BLACK
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delta_time = 0

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updateables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(COLOR_BLACK)

        for entity in updateables:
            entity.update(delta_time)

        for entity in drawables:
            entity.draw(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()