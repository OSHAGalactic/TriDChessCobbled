"""
board.py

Core board representation for Star Trek Tri-D Chess.

This module owns the logical geometry of the board.

It DOES NOT know anything about graphics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, List

from .coordinate import (
    Coordinate,
    MAIN_BOARDS,
    ATTACK_BOARDS,
    FILES,
    RANKS,
)


# ==========================================================
# Square
# ==========================================================

@dataclass
class Square:
    """
    Represents one physical square.

    Piece support will be added later.
    """

    coordinate: Coordinate
    piece: Optional[object] = None


# ==========================================================
# Attack Platform
# ==========================================================

@dataclass
class AttackPlatform:
    """
    Logical representation of a movable attack board.

    Only stores where the platform is attached.

    Rotation and movement rules will be added later.
    """

    name: str

    # Pin coordinate on a MAIN board.

    host_board: str

    file: str

    rank: int

    rotated: bool = False


# ==========================================================
# Board
# ==========================================================

class Board:

    def __init__(self):

        self.squares: Dict[Coordinate, Square] = {}

        self.attack_platforms: Dict[str, AttackPlatform] = {}

        self._create_main_boards()

        self._create_attack_boards()

        self._initialize_platform_positions()

    # ------------------------------------------------------

    def _create_main_boards(self):

        for board in MAIN_BOARDS:

            for file in FILES:

                for rank in RANKS:

                    coord = Coordinate(board, file, rank)

                    self.squares[coord] = Square(coord)

    # ------------------------------------------------------

    def _create_attack_boards(self):

        #
        # Attack boards are always 2x2.
        #
        # Internal coordinates:
        #
        # A,B
        # 1,2
        #

        attack_files = ("A", "B")

        attack_ranks = (1, 2)

        for board in ATTACK_BOARDS:

            for file in attack_files:

                for rank in attack_ranks:

                    coord = Coordinate(board, file, rank)

                    self.squares[coord] = Square(coord)

    # ------------------------------------------------------

    def _initialize_platform_positions(self):

        #
        # These are ONLY their initial locations.
        #
        # Exact movement comes later.
        #

        self.attack_platforms["WKL"] = AttackPlatform(
            "WKL",
            "WL",
            "A",
            0,
        )

        self.attack_platforms["WQL"] = AttackPlatform(
            "WQL",
            "WL",
            "D",
            0,
        )

        self.attack_platforms["BKL"] = AttackPlatform(
            "BKL",
            "BL",
            "A",
            9,
        )

        self.attack_platforms["BQL"] = AttackPlatform(
            "BQL",
            "BL",
            "D",
            9,
        )

    # ------------------------------------------------------

    def get_square(self, coordinate: Coordinate) -> Square:

        return self.squares[coordinate]

    # ------------------------------------------------------

    def is_valid_coordinate(self, coordinate: Coordinate) -> bool:

        return coordinate in self.squares

    # ------------------------------------------------------

    def get_piece(self, coordinate: Coordinate):

        return self.squares[coordinate].piece

    # ------------------------------------------------------

    def set_piece(self, coordinate: Coordinate, piece):

        self.squares[coordinate].piece = piece

    # ------------------------------------------------------

    def clear_square(self, coordinate: Coordinate):

        self.squares[coordinate].piece = None

    # ------------------------------------------------------

    def all_main_board_squares(self) -> List[Square]:

        return [
            square
            for square in self.squares.values()
            if square.coordinate.board in MAIN_BOARDS
        ]

    # ------------------------------------------------------

    def all_attack_board_squares(self) -> List[Square]:

        return [
            square
            for square in self.squares.values()
            if square.coordinate.board in ATTACK_BOARDS
        ]

    # ------------------------------------------------------

    def platform(self, name: str) -> AttackPlatform:

        return self.attack_platforms[name]

    # ------------------------------------------------------

    def overlapping_main_squares(
        self,
        coordinate: Coordinate,
    ) -> List[Coordinate]:
        """
        Returns every MAIN BOARD square
        sharing this vertical column.

        Attack-board overlap depends on
        platform position and will be added
        later.
        """

        if coordinate.board not in MAIN_BOARDS:

            return []

        return list(coordinate.overlaps())

    # ------------------------------------------------------

    def __len__(self):

        return len(self.squares)

    # ------------------------------------------------------

    def __repr__(self):

        return (
            f"<Board "
            f"{len(self.squares)} squares, "
            f"{len(self.attack_platforms)} platforms>"
        )