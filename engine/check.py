"""
check.py

Handles king safety detection.

This file answers:

"Is this king currently attacked?"

It does not:
- generate player moves
- handle turns
- determine checkmate
"""


from engine.piece import Color, PieceType

from engine.attacks import (
    pawn_attacks,
    knight_attacks,
    king_attacks,
    sliding_attacks,
)



def is_in_check(
    board,
    color,
):
    """
    Returns True if the given color's king
    is under attack.
    """

    king = board.find_king(color)

    if king is None:

        raise ValueError(
            "King not found"
        )



    enemy_color = (
        Color.BLACK
        if color == Color.WHITE
        else Color.WHITE
    )



    for coordinate, piece in board.occupied_squares().items():


        #
        # Only enemy pieces can attack
        # this king.
        #

        if piece.color != enemy_color:

            continue



        #
        # Select attack generator
        #

        if piece.piece_type == PieceType.PAWN:

            attacks = pawn_attacks(
                board,
                piece,
            )


        elif piece.piece_type == PieceType.KNIGHT:

            attacks = knight_attacks(
                board,
                piece,
            )


        elif piece.piece_type == PieceType.KING:

            attacks = king_attacks(
                board,
                piece,
            )


        else:

            attacks = sliding_attacks(
                board,
                piece,
            )



        #
        # See if any attack reaches
        # the king.
        #

        for attack in attacks:

            if attack.coordinate == king.position:

                return True



    return False