"""
layout.py

Calculates where each board appears on screen.

Contains no pygame code.
"""

from dataclasses import dataclass

from gui.colors import (
    WHITE_BOARD,
    BLACK_BOARD,
    NEUTRAL_BOARD,
)


@dataclass
class Rect:

    x: float
    y: float
    width: float
    height: float



@dataclass
class BoardVisual:

    name: str
    rect: Rect
    color: tuple
    size: int



class StandardLayout:

    def __init__(self):

        self.boards = {}


    def build(self, width, height):

        self.boards.clear()


        tile = min(width, height) / 18

        main_size = tile * 4

        attack_size = tile * 2

        gap = tile

        center_x = width / 2

        center_y = height / 2


        main_x = center_x - main_size / 2


        #
        # Main boards
        #

        wl_y = center_y + main_size * 1.25

        nl_y = center_y - main_size / 2

        bl_y = center_y - main_size * 2.25


        self.boards["WL"] = BoardVisual(
            "WL",
            Rect(
                main_x,
                wl_y,
                main_size,
                main_size,
            ),
            WHITE_BOARD,
            4,
        )


        self.boards["NL"] = BoardVisual(
            "NL",
            Rect(
                main_x,
                nl_y,
                main_size,
                main_size,
            ),
            NEUTRAL_BOARD,
            4,
        )


        self.boards["BL"] = BoardVisual(
            "BL",
            Rect(
                main_x,
                bl_y,
                main_size,
                main_size,
            ),
            BLACK_BOARD,
            4,
        )


        #
        # Attack boards
        #

        horizontal_offset = main_size + gap


        self.boards["WKL"] = BoardVisual(
            "WKL",
            Rect(
                main_x - attack_size - horizontal_offset,
                wl_y + main_size + gap,
                attack_size,
                attack_size,
            ),
            WHITE_BOARD,
            2,
        )


        self.boards["WQL"] = BoardVisual(
            "WQL",
            Rect(
                main_x + main_size + horizontal_offset,
                wl_y + main_size + gap,
                attack_size,
                attack_size,
            ),
            WHITE_BOARD,
            2,
        )


        self.boards["BKL"] = BoardVisual(
            "BKL",
            Rect(
                main_x - attack_size - horizontal_offset,
                bl_y - attack_size - gap,
                attack_size,
                attack_size,
            ),
            BLACK_BOARD,
            2,
        )


        self.boards["BQL"] = BoardVisual(
            "BQL",
            Rect(
                main_x + main_size + horizontal_offset,
                bl_y - attack_size - gap,
                attack_size,
                attack_size,
            ),
            BLACK_BOARD,
            2,
        )


        return self.boards



    def get(self, name):

        return self.boards[name]



    def all(self):

        return self.boards.values()

    def get(self, name):

        return self.boards[name]