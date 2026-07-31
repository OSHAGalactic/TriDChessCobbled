"""
legalmoves.py

Filters raw piece movement into legal chess moves.

This file handles:
- occupancy filtering
- move creation
- move simulation
- king safety pruning

It does not handle:
- turns
- checkmate
- stalemate
"""


from engine.piece import PieceType

from engine.move import Move

from engine.check import is_in_check

from engine.sliding import (
    rook_moves,
    bishop_moves,
)

from engine.knight import knight_moves
from engine.king import king_moves
from engine.pawn import pawn_moves



def raw_moves(
    board,
    piece,
):
    """
    Get movement squares without:
    - occupancy rules
    - king safety
    """


    if piece.piece_type == PieceType.PAWN:

        return pawn_moves(
            board,
            piece,
        )


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



# -------------------------------------------------


def get_destination(
    move,
):
    """
    Extract destination coordinate
    from either:
    - Move
    - RayResult
    """

    if isinstance(
        move,
        Move,
    ):

        return move.end


    return move.coordinate



# -------------------------------------------------


def occupancy_filter(
    board,
    piece,
    moves,
):
    """
    Remove moves blocked by friendly pieces.

    Enemy occupied squares remain
    as captures.
    """

    legal = []


    for move in moves:

        destination = get_destination(
            move
        )


        target = board.get_piece(
            destination
        )


        #
        # Empty square
        #

        if target is None:

            legal.append(
                destination
            )

            continue



        #
        # Enemy capture
        #

        if target.color != piece.color:

            legal.append(
                destination
            )



    return legal



# -------------------------------------------------


def legal_moves(
    board,
    piece,
):
    """
    Return only moves that:
    - obey occupancy rules
    - leave the player's king safe

    Returns:
        list[Move]
    """

    legal = []


    moves = raw_moves(
        board,
        piece,
    )


    #
    # Pawns already return complete Move objects.
    #
    # Sliding pieces, knights, and kings
    # return RayResults.
    #

    if piece.piece_type == PieceType.PAWN:

        candidates = moves


    else:

        destinations = occupancy_filter(
            board,
            piece,
            moves,
        )


        candidates = [
            Move(
                piece.position,
                destination,
                piece,
                board.get_piece(destination),
            )

            for destination in destinations
        ]



    for move in candidates:


        test_board = board.copy()


        test_board.make_move(
            move
        )


        #
        # Ignore incomplete boards
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
        # King safety
        #

        if not is_in_check(
            test_board,
            piece.color,
        ):

            legal.append(
                move
            )


    return legal