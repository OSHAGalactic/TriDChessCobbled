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

from engine.sliding import (
    rook_moves,
    bishop_moves,
)



def pawn_attacks(
    board,
    pawn,
):
    """
    Return squares attacked by a pawn.

    Pawn movement and pawn attacks are different.

    TODO:
        Add Tri-D Chess pawn attack direction.
    """

    attacks = []

    return attacks



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