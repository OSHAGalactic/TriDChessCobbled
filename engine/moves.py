"""
moves.py

Generates possible moves for pieces.

This file does not change board state.
"""

from engine.movement import can_move


def get_possible_moves(
    board,
    piece,
):
    """
    Return all legal destinations
    for a piece.
    """

    moves = []


    for square in board.all_squares():

        if can_move(
            board,
            piece,
            square,
        ):

            moves.append(square)


    return moves