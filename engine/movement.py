"""
movement.py

Contains Tri-D Chess movement rules.

This file determines whether a piece can move.
It does not change board state.
"""

from engine.piece import Color, PieceType


def can_move(
    board,
    piece,
    destination,
):

    if piece.piece_type == PieceType.PAWN:

        return pawn_can_move(
            board,
            piece,
            destination,
        )

    return False



def pawn_can_move(
    board,
    pawn,
    destination,
):

    start = pawn.position


    # White moves upward through ranks

    if pawn.color == Color.WHITE:

        if destination.board != start.board:
            return False

        if destination.file != start.file:
            return False

        return destination.rank == start.rank + 1


    # Black moves downward

    else:

        if destination.board != start.board:
            return False

        if destination.file != start.file:
            return False

        return destination.rank == start.rank - 1