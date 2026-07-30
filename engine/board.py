"""
board.py

Core board representation for Star Trek Tri-D Chess.

This file contains game state only.
It does not contain rendering logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from engine.coordinate import Coordinate


# All playable boards
PLAYABLE_BOARDS = (
    "WL",
    "NL",
    "BL",
    "WKL",
    "WQL",
    "BKL",
    "BQL",
)


# Coordinate ranges for each board
BOARD_COORDINATES = {

    # White main board
    "WL": (
        ("A", "B", "C", "D"),
        range(1, 5),
    ),

    # Neutral board
    "NL": (
        ("A", "B", "C", "D"),
        range(3, 7),
    ),

    # Black main board
    "BL": (
        ("A", "B", "C", "D"),
        range(5, 9),
    ),

    # White attack boards
    "WKL": (
        ("Z", "A"),
        range(0, 2),
    ),

    "WQL": (
        ("D", "E"),
        range(0, 2),
    ),

    # Black attack boards
    "BKL": (
        ("Z", "A"),
        range(8, 10),
    ),

    "BQL": (
        ("D", "E"),
        range(8, 10),
    ),
}


@dataclass
class Board:

    """
    Stores the current state of all Tri-D Chess squares.
    """

    squares: Dict[Coordinate, object] = field(
        default_factory=dict
    )


    def __post_init__(self):

        self.create_empty_board()


    # -------------------------------------------------

    def create_empty_board(self):

        """
        Create every playable square.
        """

        for board_name in PLAYABLE_BOARDS:

            files, ranks = BOARD_COORDINATES[board_name]

            for file in files:

                for rank in ranks:

                    coordinate = Coordinate(
                        board_name,
                        file,
                        rank,
                    )

                    self.squares[coordinate] = None


    # -------------------------------------------------

    def get_piece(
        self,
        coordinate: Coordinate,
    ):

        return self.squares.get(
            coordinate
        )


    # -------------------------------------------------

    def set_piece(
        self,
        coordinate: Coordinate,
        piece,
    ):

        self.squares[coordinate] = piece


    # -------------------------------------------------

    def remove_piece(
        self,
        coordinate: Coordinate,
    ):

        self.squares[coordinate] = None


    # -------------------------------------------------

    def contains(
        self,
        coordinate: Coordinate,
    ):

        return coordinate in self.squares

    # -------------------------------------------------

    def move_piece(
        self,
        start: Coordinate,
        end: Coordinate,
    ):
        """
        Move a piece from one square to another.

        This does not check legality.
        """

        if start not in self.squares:
            raise ValueError(
                f"Invalid starting square: {start}"
            )

        if end not in self.squares:
            raise ValueError(
                f"Invalid ending square: {end}"
            )


        piece = self.get_piece(start)


        if piece is None:
            raise ValueError(
                f"No piece at {start}"
            )


        # Update piece location
        piece.position = end
        piece.has_moved = True

        # Move piece on board
        self.squares[end] = piece

        # Clear old square
        self.squares[start] = None
    # -------------------------------------------------

    def make_move(
        self,
        move,
    ):
        """
        Execute a Move object.

        Legality checking will be added later.
        """

        self.move_piece(
            move.start,
            move.end,
        )
    def clear(self):
        """
        Remove all pieces from the board.
        """

        for coordinate in self.squares:

            self.squares[coordinate] = None
    # -------------------------------------------------

    def all_squares(self):

        return self.squares.keys()


    # -------------------------------------------------

    def occupied_squares(self):

        return {
            coordinate: piece
            for coordinate, piece
            in self.squares.items()
            if piece is not None
        }