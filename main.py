import sys

import pygame

from constants import *

from engine.board import Board
from engine.setup import setup_starting_position

from gui.layout import StandardLayout
from gui.renderer import Renderer



def main():

    pygame.init()


    screen = pygame.display.set_mode(
        (
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
        ),
        pygame.RESIZABLE,
    )


    pygame.display.set_caption(
        TITLE
    )


    clock = pygame.time.Clock()


    board = Board()

    setup_starting_position(
        board
    )


    layout = StandardLayout()

    layout.build(
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
    )


    renderer = Renderer(
        screen
    )


    running = True


    while running:


        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                running = False


            elif event.type == pygame.VIDEORESIZE:

                layout.build(
                    event.w,
                    event.h,
                )


        renderer.draw(
            board,
            layout,
        )


        clock.tick(FPS)


    pygame.quit()

    sys.exit()



if __name__ == "__main__":

    main()