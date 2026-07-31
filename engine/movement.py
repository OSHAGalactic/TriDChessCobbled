"""
movement.py

Contains Tri-D Chess movement rules.

This file determines whether a piece can move
from one square to another.

It does not:
- generate all possible moves
- change board state
- check king safety
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



def can_capture(
    board,
    piece,
    destination,
):
    """
    Returns True if the piece may capture
    an enemy piece on the destination square.
    """

    target = board.get_piece(
        destination
    )


    if target is None:

        return False


    return target.color != piece.color



def is_blocked(
    board,
    destination,
    color,
):
    """
    Returns True if a friendly piece
    occupies the destination.
    """

    target = board.get_piece(
        destination
    )


    if target is None:

        return False


    return target.color == color



def pawn_can_move(
    board,
    pawn,
    destination,
):

    start = pawn.position


    #
    # White moves upward
    #

    if pawn.color == Color.WHITE:

        if destination.board != start.board:
            return False

        if destination.file != start.file:
            return False

        return destination.rank == start.rank + 1



    #
    # Black moves downward
    #

    else:

        if destination.board != start.board:
            return False

        if destination.file != start.file:
            return False

        return destination.rank == start.rank - 1