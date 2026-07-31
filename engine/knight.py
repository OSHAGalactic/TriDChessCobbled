"""
knight.py

Movement generation for knights.

Knights:
- jump directly to destinations
- ignore intermediate squares
- may land on any board occupying
  the destination coordinate

This file does not know:
- pieces
- captures
- turns
- check
"""
from engine.raycaster import RayResult
from engine.coordinate import Coordinate
from engine.vector import apply_vector
from engine.direction import KNIGHT_VECTORS
from engine.space import get_boards_at



def knight_moves(
    board,
    piece,
):
    """
    Generate all knight moves.
    """

    results = []

    seen = set()


    for vector in KNIGHT_VECTORS:


        #
        # Calculate physical destination
        #

        location = apply_vector(
            piece.position,
            vector,
        )


        #
        # Find all boards containing
        # this physical square
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
                    RayResult(destination)
                )

                seen.add(
                    destination
                )


    return results