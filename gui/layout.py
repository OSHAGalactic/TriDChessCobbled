"""
layout.py

Defines the visual placement of all Tri-D Chess boards.

This file contains no rendering logic.
"""

from dataclasses import dataclass
from pygame import Rect


@dataclass
class BoardVisual:

    name: str
    rect: Rect
    color: tuple
    size: int = 4



class StandardLayout:


    def __init__(self):

        self.visuals = {}



    def build(self, width, height):

        self.visuals.clear()


        # -----------------------------------------
        # Board sizing
        # -----------------------------------------

        gap = 20

        board_size = min(
            width * 0.22,
            height * 0.22,
        )

        board_size = int(board_size)

        attack_size = board_size // 2

        center_x = width // 2


        total_height = (
            board_size * 3
            +
            gap * 2
        )


        top = (
            height - total_height
        ) // 2



        # -----------------------------------------
        # Main boards
        # -----------------------------------------

        x = center_x - board_size // 2


        self.visuals["BL"] = BoardVisual(
            "BL",
            Rect(
                x,
                top,
                board_size,
                board_size,
            ),
            (155,80,80),
        )


        self.visuals["NL"] = BoardVisual(
            "NL",
            Rect(
                x,
                top + board_size + gap,
                board_size,
                board_size,
            ),
            (130,130,130),
        )


        wl_y = top + (board_size + gap) * 2


        self.visuals["WL"] = BoardVisual(
            "WL",
            Rect(
                x,
                wl_y,
                board_size,
                board_size,
            ),
            (90,150,95),
        )



        # -----------------------------------------
        # Attack boards
        #
        # Attached to corners of main boards,
        # shifted by one game tile:
        #
        # Left boards: move left 1 tile
        # Right boards: move right 1 tile
        # Black boards: move up 1 tile
        # White boards: move down 1 tile
        # -----------------------------------------

        tile = attack_size // 2


        # Black attack boards

        self.visuals["BKL"] = BoardVisual(
            "BKL",
            Rect(
                x - attack_size - tile,
                top - tile,
                attack_size,
                attack_size,
            ),
            (155,80,80),
            size=2,
        )


        self.visuals["BQL"] = BoardVisual(
            "BQL",
            Rect(
                x + board_size + tile,
                top - tile,
                attack_size,
                attack_size,
            ),
            (155,80,80),
            size=2,
        )


                # White attack boards
        #
        # Moved up 2 game squares

        self.visuals["WKL"] = BoardVisual(
            "WKL",
            Rect(
                x - attack_size - tile,
                wl_y + board_size - tile,
                attack_size,
                attack_size,
            ),
            (90,150,95),
            size=2,
        )


        self.visuals["WQL"] = BoardVisual(
            "WQL",
            Rect(
                x + board_size + tile,
                wl_y + board_size - tile,
                attack_size,
                attack_size,
            ),
            (90,150,95),
            size=2,
        )


        return self.visuals



    def get(self, name):

        return self.visuals[name]



    def board(self, name):

        return self.visuals[name]



    def all(self):

        return self.visuals.values()