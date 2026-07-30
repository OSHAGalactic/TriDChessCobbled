"""
renderer.py

Pygame renderer.
"""

import pygame

from gui.colors import (
    BACKGROUND,
    LIGHT_SQUARE,
    DARK_SQUARE,
    TEXT,
)



class Renderer:


    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont(
            "arial",
            18,
        )


    def draw(self, board, layout):

        self.screen.fill(
            BACKGROUND
        )


        #
        # Attack boards first
        #

        for name in (
            "BKL",
            "BQL",
            "WKL",
            "WQL",
        ):

            self.draw_board(
                layout.get(name),
                True,
            )


        #
        # Main boards second
        #

        for name in (
            "BL",
            "NL",
            "WL",
        ):

            self.draw_board(
                layout.get(name),
                False,
            )


        pygame.display.flip()



    def draw_board(
        self,
        visual,
        attack=False,
    ):

        rect = pygame.Rect(
            visual.rect.x,
            visual.rect.y,
            visual.rect.width,
            visual.rect.height,
        )


        pygame.draw.rect(
            self.screen,
            visual.color,
            rect,
        )


        pygame.draw.rect(
            self.screen,
            (0,0,0),
            rect,
            3 if attack else 5,
        )


        self.draw_squares(
            visual
        )


        label = self.font.render(
            visual.name,
            True,
            TEXT,
        )


        self.screen.blit(
            label,
            (
                visual.rect.x + 5,
                visual.rect.y + 5,
            ),
        )



    def draw_squares(self, visual):

        size = visual.size

        tile_w = visual.rect.width / size

        tile_h = visual.rect.height / size


        for row in range(size):

            for col in range(size):

                color = (
                    LIGHT_SQUARE
                    if
                    (row + col) % 2 == 0
                    else
                    DARK_SQUARE
                )


                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        visual.rect.x + col * tile_w,
                        visual.rect.y + row * tile_h,
                        tile_w,
                        tile_h,
                    ),
                )