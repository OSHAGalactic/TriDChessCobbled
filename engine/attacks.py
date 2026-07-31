"""
attacks.py

Provides attack square generation.

This is used for:
- check detection
- king safety

It does not:
- move pieces
- validate turns
- handle captures
"""


from engine.piece import PieceType

from engine.knight import knight_moves
from engine.pawn import pawn_attacks as generate_pawn_attacks
from engine.raycaster import RayResult

from engine.sliding import (
    rook_moves,
    bishop_moves,
)



# -------------------------------------------------
# Pawn attacks
# -------------------------------------------------


def pawn_attacks(
    board,
    pawn,
):
    """
    Return squares attacked by a pawn.

    Converted into RayResult objects so
    all attack generators share the same interface.
    """

    return [
        RayResult(
            coordinate
        )

        for coordinate in generate_pawn_attacks(
            board,
            pawn,
        )
    ]



# -------------------------------------------------
# Knight attacks
# -------------------------------------------------


def knight_attacks(
    board,
    knight,
):
    """
    Knights attack the same squares
    they can move to.
    """

    return knight_moves(
        board,
        knight,
    )



# -------------------------------------------------
# King attacks
# -------------------------------------------------


def king_attacks(
    board,
    king,
):
    """
    Kings attack adjacent squares.

    This is separate from king_moves because
    kings cannot move into check.
    """

    from engine.king import king_moves

    return king_moves(
        board,
        king,
    )



# -------------------------------------------------
# Sliding attacks
# -------------------------------------------------


def sliding_attacks(
    board,
    piece,
):
    """
    Generate attacks for sliding pieces.

    Used by:
    - rooks
    - bishops
    - queens
    """

    if piece.piece_type == PieceType.ROOK:

        return rook_moves(
            board,
            piece,
        )


    if piece.piece_type == PieceType.BISHOP:

        return bishop_moves(
            board,
            piece,
        )


    if piece.piece_type == PieceType.QUEEN:

        return (
            rook_moves(
                board,
                piece,
            )
            +
            bishop_moves(
                board,
                piece,
            )
        )


    return []



# -------------------------------------------------
# Universal attack dispatcher
# -------------------------------------------------


def attacks(
    board,
    piece,
):
    """
    Return all squares attacked by a piece.

    Used by:
    - check detection
    - king safety
    """

    if piece.piece_type == PieceType.PAWN:

        return pawn_attacks(
            board,
            piece,
        )


    if piece.piece_type == PieceType.KNIGHT:

        return knight_attacks(
            board,
            piece,
        )


    if piece.piece_type == PieceType.KING:

        return king_attacks(
            board,
            piece,
        )


    return sliding_attacks(
        board,
        piece,
    )