"""
king.py

Movement generation for kings.

Kings:
- move one square in any direction
- may move between overlapping platforms
- do not handle check here

This file does not know:
- captures
- turns
- check
"""

from engine.coordinate import Coordinate
from engine.direction import Direction
from engine.vector import apply_vector
from engine.space import get_boards_at
from engine.raycaster import RayResult



KING_DIRECTIONS = (

    Direction.UP,
    Direction.DOWN,
    Direction.LEFT,
    Direction.RIGHT,

    Direction.UP_LEFT,
    Direction.UP_RIGHT,
    Direction.DOWN_LEFT,
    Direction.DOWN_RIGHT,

)



def king_moves(
    board,
    piece,
):
    """
    Generate king moves ignoring check.

    Returns:
        list[RayResult]
    """

    results = []

    seen = set()


    for direction in KING_DIRECTIONS:


        #
        # Move one physical square
        #

        location = apply_vector(
            piece.position,
            direction.value,
        )


        #
        # Find all boards containing
        # this physical location
        #

        boards = get_boards_at(
            location.file,
            location.rank,
        )


        for board_name in boards:


            destination = Coordinate(
                board_name,
                location.file,
                location.rank,
            )


            if destination not in seen:

                results.append(
                    RayResult(
                        destination
                    )
                )

                seen.add(
                    destination
                )


    return results