"""
direction.py

Defines movement vectors for Tri-D Chess.

This file contains only movement direction data.
It does not contain board logic or movement validation.
"""

from dataclasses import dataclass
from enum import Enum



@dataclass(frozen=True)
class Vector:

    """
    Represents a change in file and rank.

    file_change:
        -1 = left
         0 = same file
        +1 = right

    rank_change:
        -1 = down
         0 = same rank
        +1 = up
    """

    file_change: int
    rank_change: int



class Direction(Enum):

    """
    Standard sliding-piece directions.

    Used by:
        - Rooks
        - Bishops
        - Queens

    Each direction contains:
        (file change, rank change)
    """


    # Straight directions

    UP = Vector(
        0,
        1,
    )


    DOWN = Vector(
        0,
        -1,
    )


    LEFT = Vector(
        -1,
        0,
    )


    RIGHT = Vector(
        1,
        0,
    )



    # Diagonal directions

    UP_LEFT = Vector(
        -1,
        1,
    )


    UP_RIGHT = Vector(
        1,
        1,
    )


    DOWN_LEFT = Vector(
        -1,
        -1,
    )


    DOWN_RIGHT = Vector(
        1,
        -1,
    )



# -------------------------------------------------
# Piece movement groups
# -------------------------------------------------


ROOK_DIRECTIONS = (

    Direction.UP,
    Direction.DOWN,
    Direction.LEFT,
    Direction.RIGHT,

)



BISHOP_DIRECTIONS = (

    Direction.UP_LEFT,
    Direction.UP_RIGHT,
    Direction.DOWN_LEFT,
    Direction.DOWN_RIGHT,

)



QUEEN_DIRECTIONS = (

    *ROOK_DIRECTIONS,
    *BISHOP_DIRECTIONS,

)



# -------------------------------------------------
# Knight movement
# -------------------------------------------------


KNIGHT_VECTORS = (

    # Two up, one sideways

    Vector(
        1,
        2,
    ),

    Vector(
        -1,
        2,
    ),


    # Two down, one sideways

    Vector(
        1,
        -2,
    ),

    Vector(
        -1,
        -2,
    ),


    # Two sideways, one up

    Vector(
        2,
        1,
    ),

    Vector(
        -2,
        1,
    ),


    # Two sideways, one down

    Vector(
        2,
        -1,
    ),

    Vector(
        -2,
        -1,
    ),

)