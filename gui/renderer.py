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
    WHITE_PIECE,
    BLACK_PIECE,
)

from gui.piece_symbols import get_symbol



class Renderer:


    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont(
            "arial",
            18,
        )

        self.piece_font = pygame.font.SysFont(
            "arial",
            36,
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


        #
        # Pieces last
        #

        self.draw_pieces(
            board,
            layout,
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



    def draw_pieces(
        self,
        board,
        layout,
    ):

        for coordinate, piece in board.squares.items():

            if piece is None:
                continue


            visual = layout.get(
                coordinate.board
            )


            size = visual.size

            tile_w = visual.rect.width / size
            tile_h = visual.rect.height / size


            col = self.file_to_col(
                coordinate.file,
                coordinate.board,
            )


            row = self.rank_to_row(
                coordinate.rank,
                coordinate.board,
            )


            x = (
                visual.rect.x
                +
                col * tile_w
                +
                tile_w / 2
            )

            y = (
                visual.rect.y
                +
                row * tile_h
                +
                tile_h / 2
            )


            #
            # Choose piece color
            #

            if piece.color.name == "WHITE":

                piece_color = WHITE_PIECE

            else:

                piece_color = BLACK_PIECE


            symbol = self.piece_font.render(
                get_symbol(piece),
                True,
                piece_color,
            )


            symbol_rect = symbol.get_rect(
                center=(
                    x,
                    y,
                )
            )


            self.screen.blit(
                symbol,
                symbol_rect,
            )



    def file_to_col(
        self,
        file,
        board_name,
    ):

        """
        Converts Tri-D file coordinates
        into visual columns.
        """


        # Main 4x4 boards

        if board_name in (
            "WL",
            "NL",
            "BL",
        ):

            return {
                "A": 0,
                "B": 1,
                "C": 2,
                "D": 3,
            }[file]


        # Left attack boards
        #
        # Coordinates:
        #
        # Z A
        #
        # Z moves one tile left
        # A stays one tile right

        if board_name in (
            "WKL",
            "BKL",
        ):

            return {
                "Z": 0,
                "A": 1,
            }[file]


        # Right attack boards
        #
        # Coordinates:
        #
        # D E
        #
        # D stays left
        # E moves one tile right

        if board_name in (
            "WQL",
            "BQL",
        ):

            return {
                "D": 0,
                "E": 1,
            }[file]


        return 0



    def rank_to_row(
        self,
        rank,
        board_name,
    ):

        """
        Converts Tri-D ranks into rows.
        """


        if board_name == "WL":
            return 3 - (rank - 1)


        if board_name == "NL":
            return 3 - (rank - 3)


        if board_name == "BL":
            return 3 - (rank - 5)


        if board_name in (
            "WKL",
            "WQL",
        ):

            return 1 - rank


        if board_name in (
            "BKL",
            "BQL",
        ):

            return 9 - rank


        return 0