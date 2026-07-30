"""
board.py

Core board model for Star Trek Tri-D Chess.

The Board owns:
    • Every physical square
    • Every attack platform
    • Current platform locations

Rendering is handled elsewhere.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .coordinate import Coordinate, FILES, RANKS


MAIN_BOARDS = ("WL", "NL", "BL")


# ---------------------------------------------------------
# Square
# ---------------------------------------------------------

@dataclass
class Square:
    coordinate: Coordinate
    piece: Optional[object] = None


# ---------------------------------------------------------
# Attack Platform
# ---------------------------------------------------------

@dataclass
class AttackPlatform:
    """
    Represents one movable 2×2 attack platform.

    The platform's four logical squares are always:

        A1 A2
        B1 B2

    Rotation determines which physical corner each maps to.
    """

    name: str

    # Which main board currently hosts this platform.
    host_board: str

    # Which corner pin it is attached to.
    pin_file: str
    pin_rank: int

    rotated: bool = False

    moved: bool = False

    def rotate(self):

        self.rotated = not self.rotated


# ---------------------------------------------------------
# Board
# ---------------------------------------------------------

class Board:

    def __init__(self):

        self.squares: Dict[Coordinate, Square] = {}

        self.platforms: Dict[str, AttackPlatform] = {}

        self._create_main_boards()

        self._create_platforms()

    # -------------------------------------------------

    def _create_main_boards(self):

        for board in MAIN_BOARDS:

            for file in FILES:

                for rank in RANKS:

                    c = Coordinate(board, file, rank)

                    self.squares[c] = Square(c)

    # -------------------------------------------------

    def _create_platforms(self):

        self.platforms["WKL"] = AttackPlatform(
            "WKL",
            "WL",
            "A",
            0,
        )

        self.platforms["WQL"] = AttackPlatform(
            "WQL",
            "WL",
            "D",
            0,
        )

        self.platforms["BKL"] = AttackPlatform(
            "BKL",
            "BL",
            "A",
            9,
        )

        self.platforms["BQL"] = AttackPlatform(
            "BQL",
            "BL",
            "D",
            9,
        )

    # -------------------------------------------------

    def get_square(self, coordinate: Coordinate) -> Square:

        return self.squares[coordinate]

    # -------------------------------------------------

    def all_squares(self):

        return self.squares.values()

    # -------------------------------------------------

    def all_platforms(self):

        return self.platforms.values()

    # -------------------------------------------------

    def move_platform(
        self,
        name: str,
        host_board: str,
        pin_file: str,
        pin_rank: int,
        rotate: bool = False,
    ):

        platform = self.platforms[name]

        platform.host_board = host_board
        platform.pin_file = pin_file
        platform.pin_rank = pin_rank

        if rotate:
            platform.rotate()

        platform.moved = True

    # -------------------------------------------------

    def overlaps(self, coordinate: Coordinate) -> List[Coordinate]:
        """
        Returns every square currently sharing the same
        vertical column.

        For now this only returns the three main-board
        coordinates. Attack-platform overlap will be
        added once platform geometry is implemented.
        """

        return coordinate.overlaps()

    # -------------------------------------------------

    def __repr__(self):

        return (
            f"<Board "
            f"{len(self.squares)} main squares, "
            f"{len(self.platforms)} platforms>"
        )