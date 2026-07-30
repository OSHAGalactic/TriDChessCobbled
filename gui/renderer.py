"""
renderer.py

Pygame renderer for Star Trek Tri-D Chess.

The renderer draws the current visual state.
It does not contain game logic.
"""

from __future__ import annotations

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


    # -------------------------------------------------

    def draw(self, board, layout):

        """
        Draw the entire game view.
        """

        self.screen.fill(BACKGROUND)

        self._draw_attack_boards(
            layout
        )

        self._draw_main_boards(
            layout
        )

        pygame.display.flip()


    # -------------------------------------------------

    def _draw_main_boards(self, layout):

        """
        Draw WL, NL, BL.

        These are drawn after attack boards
        so attack boards visually sit behind.
        """

        for name in (
            "BL",
            "NL",
            "WL",
        ):

            visual = layout.get(name)

            self._draw_board(
                visual,
                label=name,
            )


    # -------------------------------------------------

    def _draw_attack_boards(self, layout):

        for name in (
            "BKL",
            "BQL",
            "WKL",
            "WQL",
        ):

            visual = layout.get(name)

            self._draw_board(
                visual,
                label=name,
                attack=True,
            )


    # -------------------------------------------------

    def _draw_board(
        self,
        visual,
        label=None,
        attack=False,
    ):

        rect = visual.rect

        pygame_rect = pygame.Rect(
            rect.x,
            rect.y,
            rect.width,
            rect.height,
        )


        pygame.draw.rect(
            self.screen,
            visual.color,
            pygame_rect,
        )


        if attack:

            border_width = 3

        else:

            border_width = 5


        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            pygame_rect,
            border_width,
        )


        self._draw_squares(
            visual,
        )


        if label:

            self._draw_label(
                label,
                rect.x,
                rect.y,
            )


    # -------------------------------------------------

    def _draw_squares(self, visual):

        size = visual.size

        tile_width = visual.rect.width / size
        tile_height = visual.rect.height / size


        for row in range(size):

            for col in range(size):

                x = (
                    visual.rect.x
                    +
                    col * tile_width
                )

                y = (
                    visual.rect.y
                    +
                    row * tile_height
                )


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
                        x,
                        y,
                        tile_width,
                        tile_height,
                    ),
                )


    # -------------------------------------------------

    def _draw_label(
        self,
        text,
        x,
        y,
    ):

        surface = self.font.render(
            text,
            True,
            TEXT,
        )

        self.screen.blit(
            surface,
            (
                x + 5,
                y + 5,
            ),
        )