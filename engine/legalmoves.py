"""
legalmoves.py

Filters raw piece movement into legal chess moves.

This file handles:
- occupancy filtering
- move simulation
- king safety pruning

It does not handle:
- turns
- checkmate
- stalemate
"""


from engine.piece import PieceType

from engine.check import is_in_check

from engine.sliding import (
    rook_moves,
    bishop_moves,
)

from engine.knight import knight_moves
from engine.king import king_moves



def raw_moves(
    board,
    piece,
):
    """
    Get movement squares without:
    - occupancy rules
    - king safety
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


    if piece.piece_type == PieceType.KNIGHT:

        return knight_moves(
            board,
            piece,
        )


    if piece.piece_type == PieceType.KING:

        return king_moves(
            board,
            piece,
        )


    return []



def occupancy_filter(
    board,
    piece,
    moves,
):
    """
    Remove moves blocked by friendly pieces.

    Enemy occupied squares remain as
    possible captures.
    """

    legal = []


    for move in moves:

        target = board.get_piece(
            move.coordinate
        )


        #
        # Empty square
        #

        if target is None:

            legal.append(
                move
            )

            continue



        #
        # Enemy piece:
        # capture allowed
        #

        if target.color != piece.color:

            legal.append(
                move
            )



    return legal



def legal_moves(
    board,
    piece,
):
    """
    Return only moves that:
    - obey occupancy rules
    - leave the player's king safe
    """

    legal = []


    moves = raw_moves(
        board,
        piece,
    )


    moves = occupancy_filter(
        board,
        piece,
        moves,
    )



    for move in moves:


        test_board = board.copy()


        test_board.move_piece(
            piece.position,
            move.coordinate,
        )


        #
        # Ignore incomplete test boards
        # without kings.
        #

        king = test_board.find_king(
            piece.color
        )


        if king is None:

            legal.append(
                move
            )

            continue



        #
        # Keep only moves that do
        # not expose the king.
        #

        if not is_in_check(
            test_board,
            piece.color,
        ):

            legal.append(
                move
            )


    return legal