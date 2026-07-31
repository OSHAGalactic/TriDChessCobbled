"""
sliding.py

Movement generation for Tri-D Chess sliding pieces.

Sliding pieces:
- rook
- bishop
- queen

This file handles:
- ray traversal
- friendly blockers
- enemy captures

It does not handle:
- turns
- check
- checkmate
"""


from engine.raycaster import Raycaster

from engine.direction import (
    ROOK_DIRECTIONS,
    BISHOP_DIRECTIONS,
    QUEEN_DIRECTIONS,
)



def sliding_moves(
    board,
    piece,
    directions,
):
    """
    Generate sliding moves in given directions.

    Stops when:
    - friendly piece is encountered
    - enemy piece is encountered after adding capture
    """

    raycaster = Raycaster(board)

    results = []


    for direction in directions:


        ray_results = raycaster.cast(
            [piece.position],
            direction.value,
        )


        for result in ray_results:


            target = board.get_piece(
                result.coordinate
            )


            #
            # Empty square:
            # continue moving.
            #

            if target is None:

                results.append(
                    result
                )

                continue



            #
            # Enemy piece:
            # capture square is valid,
            # but stop this direction.
            #

            if target.color != piece.color:

                results.append(
                    result
                )


            #
            # Friendly piece:
            # cannot move here.
            #

            break



    return results



def rook_moves(
    board,
    piece,
):

    return sliding_moves(
        board,
        piece,
        ROOK_DIRECTIONS,
    )



def bishop_moves(
    board,
    piece,
):

    return sliding_moves(
        board,
        piece,
        BISHOP_DIRECTIONS,
    )



def queen_moves(
    board,
    piece,
):

    return sliding_moves(
        board,
        piece,
        QUEEN_DIRECTIONS,
    )