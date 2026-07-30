"""
rules.py

Game rule validation for Tri-D Chess.

This file decides whether moves are allowed.
It does not draw anything.
"""

from engine.piece import Color
from engine.movement import can_move


class Rules:


    def __init__(self, board):

        self.board = board



    def validate_move(
        self,
        move,
        turn,
    ):
        """
        Returns True if a move is legal.
        """

        start = move.start
        end = move.end


        # -------------------------------
        # Check starting square
        # -------------------------------

        piece = self.board.get_piece(start)


        if piece is None:
            return False



        # -------------------------------
        # Check player's turn
        # -------------------------------

        if piece.color != turn:
            return False



        # -------------------------------
        # Check movement rules
        # -------------------------------

        if not can_move(
            self.board,
            piece,
            end,
        ):
            return False



        # -------------------------------
        # Check destination
        # -------------------------------

        destination_piece = self.board.get_piece(end)


        # Cannot capture own pieces

        if destination_piece is not None:

            if destination_piece.color == piece.color:
                return False



        return True



    def make_move(
        self,
        move,
        turn,
    ):
        """
        Validates and executes a move.
        """

        if not self.validate_move(
            move,
            turn,
        ):
            raise ValueError(
                "Illegal move"
            )


        self.board.move_piece(
            move.start,
            move.end,
        )