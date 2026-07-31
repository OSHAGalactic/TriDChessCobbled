"""
pawn.py

Pawn movement generation for Tri-D Chess.

Handles:
- one-square movement
- two-square opening movement
- diagonal captures
- pawn attack squares

Does not handle:
- turns
- check
- promotion
"""


from engine.coordinate import Coordinate
from engine.vector import apply_vector
from engine.direction import Vector
from engine.piece import Color
from engine.move import Move
from engine.space import get_boards_at



# -------------------------------------------------
# Direction
# -------------------------------------------------


def pawn_direction(pawn):
    """
    Return pawn movement direction.
    """

    if pawn.color == Color.WHITE:
        return 1

    return -1



# -------------------------------------------------
# Physical stepping helper
# -------------------------------------------------


def pawn_step(
    board,
    positions,
    vector,
    require_empty=True,
):
    """
    Move all possible positions one
    physical square using topology.

    require_empty:
        True  = normal movement
        False = attack generation
    """

    results = []


    for position in positions:

        moved = apply_vector(
            position,
            vector,
        )


        boards = get_boards_at(
            moved.file,
            moved.rank,
        )


        for board_name in boards:

            destination = Coordinate(
                board_name,
                moved.file,
                moved.rank,
            )


            if not board.contains(destination):

                continue


            if require_empty:

                if board.get_piece(destination) is not None:
                    continue


            results.append(
                destination
            )


    return results



# -------------------------------------------------
# Forward movement
# -------------------------------------------------


def pawn_forward_moves(
    board,
    pawn,
):
    """
    One-square pawn movement.
    """

    vector = Vector(
        0,
        pawn_direction(pawn),
    )


    return [
        Move(
            pawn.position,
            destination,
        )

        for destination in pawn_step(
            board,
            [pawn.position],
            vector,
            True,
        )
    ]



# -------------------------------------------------
# Two-square movement
# -------------------------------------------------


def pawn_double_moves(
    board,
    pawn,
):
    """
    Two-square opening move.

    Requires:
    - pawn has not moved
    - both squares are empty

    Uses topology stepping.
    """

    if pawn.has_moved:

        return []


    vector = Vector(
        0,
        pawn_direction(pawn),
    )


    first_steps = pawn_step(
        board,
        [pawn.position],
        vector,
        True,
    )


    second_steps = pawn_step(
        board,
        first_steps,
        vector,
        True,
    )


    return [
        Move(
            pawn.position,
            destination,
        )

        for destination in second_steps
    ]



# -------------------------------------------------
# Diagonal attack geometry
# -------------------------------------------------


def pawn_diagonal_squares(
    board,
    pawn,
):
    """
    Generate diagonal pawn attack squares.

    Does not care if a piece exists.

    Used by:
    - captures
    - check detection
    """

    direction = pawn_direction(
        pawn
    )


    vectors = [

        # forward-left
        Vector(
            -1,
            direction,
        ),

        # forward-right
        Vector(
            1,
            direction,
        ),
    ]


    results = []


    for vector in vectors:

        results.extend(
            pawn_step(
                board,
                [pawn.position],
                vector,
                False,
            )
        )


    return results



# -------------------------------------------------
# Captures
# -------------------------------------------------


def pawn_capture_moves(
    board,
    pawn,
):
    """
    Generate diagonal pawn captures.
    """

    moves = []


    for destination in pawn_diagonal_squares(
        board,
        pawn,
    ):

        target = board.get_piece(
            destination
        )


        if target is None:

            continue


        if target.color != pawn.color:

            moves.append(
                Move(
                    pawn.position,
                    destination,
                    pawn,
                    target,
                )
            )


    return moves



# -------------------------------------------------
# Attack generation
# -------------------------------------------------


def pawn_attacks(
    board,
    pawn,
):
    """
    Generate squares attacked by a pawn.

    Unlike capture moves:
    - empty squares count
    - occupancy does not matter
    """

    return pawn_diagonal_squares(
        board,
        pawn,
    )



# -------------------------------------------------
# Combined movement
# -------------------------------------------------


def pawn_moves(
    board,
    pawn,
):
    """
    Generate all pawn moves.
    """

    moves = []


    moves.extend(
        pawn_forward_moves(
            board,
            pawn,
        )
    )


    moves.extend(
        pawn_double_moves(
            board,
            pawn,
        )
    )


    moves.extend(
        pawn_capture_moves(
            board,
            pawn,
        )
    )


    return moves