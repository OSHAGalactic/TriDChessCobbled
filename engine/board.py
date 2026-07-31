"""
board.py

Core board representation for Star Trek Tri-D Chess.

This file contains game state only.
It does not contain rendering logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from engine.coordinate import Coordinate
from engine.piece import PieceType



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

    "WL": (
        ("A", "B", "C", "D"),
        range(1, 5),
    ),

    "NL": (
        ("A", "B", "C", "D"),
        range(3, 7),
    ),

    "BL": (
        ("A", "B", "C", "D"),
        range(5, 9),
    ),

    "WKL": (
        ("Z", "A"),
        range(0, 2),
    ),

    "WQL": (
        ("D", "E"),
        range(0, 2),
    ),

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

    def contains(
        self,
        coordinate: Coordinate,
    ):

        return coordinate in self.squares



    # -------------------------------------------------

    def get_piece(
        self,
        coordinate: Coordinate,
    ):

        return self.squares.get(
            coordinate
        )



    # -------------------------------------------------

    def add_piece(
        self,
        piece,
    ):
        """
        Place a piece on the board.
        """

        self.squares[piece.position] = piece



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
        """
        Remove a piece from a square.
        """

        self.squares[coordinate] = None



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


        #
        # Move piece
        #

        self.squares[end] = piece
        self.squares[start] = None


        #
        # Update piece data
        #

        piece.position = end
        piece.has_moved = True



    # -------------------------------------------------

    def make_move(
        self,
        move,
    ):
        """
        Execute a Move object.

        Handles:
        - captures
        - moving pieces

        Does not handle:
        - legality
        - turns
        """


        #
        # Remove captured piece
        #

        if move.captured is not None:

            self.remove_piece(
                move.end
            )


        #
        # Move attacking piece
        #

        self.move_piece(
            move.start,
            move.end,
        )



    # -------------------------------------------------

    def find_king(
        self,
        color,
    ):
        """
        Find a king of the given color.
        """

        for piece in self.squares.values():

            if piece is None:
                continue


            if (
                piece.piece_type == PieceType.KING
                and piece.color == color
            ):

                return piece


        return None



    # -------------------------------------------------

    def all_pieces(self):

        """
        Return every piece currently
        on the board.
        """

        return [
            piece
            for piece in self.squares.values()
            if piece is not None
        ]



    # -------------------------------------------------

    def copy(self):
        """
        Create an independent copy of the board.

        Used for:
        - move simulation
        - check detection
        - legality testing
        """

        new_board = Board()


        for coordinate, piece in self.squares.items():

            if piece is None:

                continue


            copied_piece = type(piece)(
                piece.piece_type,
                piece.color,
                coordinate,
            )


            copied_piece.has_moved = (
                piece.has_moved
            )


            new_board.set_piece(
                coordinate,
                copied_piece,
            )


        return new_board



    # -------------------------------------------------

    def clear(self):
        """
        Remove all pieces.
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