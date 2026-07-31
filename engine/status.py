"""
status.py

Determines the current state of a Tri-D Chess game.

This file handles:
- check
- checkmate
- stalemate
- game over detection

It does not:
- make moves
- handle turns
- modify the board
"""


from engine.legalmoves import legal_moves
from engine.check import is_in_check



def has_legal_moves(
    board,
    color,
):
    """
    Returns True if the player has
    at least one legal move.
    """


    for piece in board.all_pieces():

        if piece.color != color:

            continue


        if legal_moves(
            board,
            piece,
        ):

            return True


    return False



# -------------------------------------------------


def is_checkmate(
    board,
    color,
):
    """
    Checkmate occurs when:
    - king is in check
    - no legal moves exist
    """


    if not is_in_check(
        board,
        color,
    ):

        return False



    return not has_legal_moves(
        board,
        color,
    )



# -------------------------------------------------


def is_stalemate(
    board,
    color,
):
    """
    Stalemate occurs when:
    - king is NOT in check
    - no legal moves exist
    """


    if is_in_check(
        board,
        color,
    ):

        return False



    return not has_legal_moves(
        board,
        color,
    )



# -------------------------------------------------


def game_over(
    board,
    color,
):
    """
    Returns True if the game has ended.
    """


    return (
        is_checkmate(
            board,
            color,
        )
        or
        is_stalemate(
            board,
            color,
        )
    )