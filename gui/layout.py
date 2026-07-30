"""
layout.py

Screen layout for Star Trek Tri-D Chess.

The layout knows NOTHING about pieces or drawing.

It simply computes where each board should appear.

Current mode:
    Standard 2D

Future:
    Overlapped 2D
    3D
"""

from __future__ import annotations

from dataclasses import dataclass


# ---------------------------------------------------------
# Rectangle
# ---------------------------------------------------------

@dataclass(slots=True)
class Rect:

    x: float
    y: float

    width: float
    height: float


# ---------------------------------------------------------
# Board Visual
# ---------------------------------------------------------

@dataclass(slots=True)
class BoardVisual:

    board: str

    rect: Rect

    color: tuple[int, int, int]


# ---------------------------------------------------------
# Standard Layout
# ---------------------------------------------------------

class StandardLayout:
    """
    Standard 2D layout.

        BKL     BL     BQL

               NL

        WKL     WL     WQL

    Attack platforms sit visually outside the
    main boards exactly like the physical board.
    """

    def __init__(self):

        self.visuals = {}

    # -----------------------------------------------------

    def build(self, width: int, height: int):

        self.visuals.clear()

        #
        # Overall board sizing.
        #

        board_size = min(width, height) * 0.23

        attack_size = board_size / 2

        horizontal_gap = board_size * 0.30

        vertical_gap = board_size * 0.55

        center_x = width / 2

        center_y = height / 2

        #
        # Main boards
        #

        wl_x = center_x - board_size / 2
        wl_y = center_y + vertical_gap

        nl_x = center_x - board_size / 2
        nl_y = center_y - board_size / 2

        bl_x = center_x - board_size / 2
        bl_y = center_y - board_size - vertical_gap

        #
        # Attack platforms
        #

        wkl_x = wl_x - attack_size - horizontal_gap
        wkl_y = wl_y

        wql_x = wl_x + board_size + horizontal_gap
        wql_y = wl_y

        bkl_x = bl_x - attack_size - horizontal_gap
        bkl_y = bl_y

        bql_x = bl_x + board_size + horizontal_gap
        bql_y = bl_y

        self.visuals["WL"] = BoardVisual(
            "WL",
            Rect(
                wl_x,
                wl_y,
                board_size,
                board_size,
            ),
            (80, 145, 85),
        )

        self.visuals["NL"] = BoardVisual(
            "NL",
            Rect(
                nl_x,
                nl_y,
                board_size,
                board_size,
            ),
            (130, 130, 130),
        )

        self.visuals["BL"] = BoardVisual(
            "BL",
            Rect(
                bl_x,
                bl_y,
                board_size,
                board_size,
            ),
            (150, 80, 80),
        )

        self.visuals["WKL"] = BoardVisual(
            "WKL",
            Rect(
                wkl_x,
                wkl_y,
                attack_size,
                attack_size,
            ),
            (185, 185, 185),
        )

        self.visuals["WQL"] = BoardVisual(
            "WQL",
            Rect(
                wql_x,
                wql_y,
                attack_size,
                attack_size,
            ),
            (185, 185, 185),
        )

        self.visuals["BKL"] = BoardVisual(
            "BKL",
            Rect(
                bkl_x,
                bkl_y,
                attack_size,
                attack_size,
            ),
            (185, 185, 185),
        )

        self.visuals["BQL"] = BoardVisual(
            "BQL",
            Rect(
                bql_x,
                bql_y,
                attack_size,
                attack_size,
            ),
            (185, 185, 185),
        )

        return self.visuals

    # -----------------------------------------------------

    def board(self, board_name: str):

        return self.visuals[board_name]

    # -----------------------------------------------------

    def all_boards(self):

        return self.visuals.values()