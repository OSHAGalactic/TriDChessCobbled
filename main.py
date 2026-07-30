import sys

import pygame

from constants import *
from engine.board import Board


def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.RESIZABLE,
    )

    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    board = Board()

    print(board)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

    sys.exit()


if __name__ == "__main__":
    main()