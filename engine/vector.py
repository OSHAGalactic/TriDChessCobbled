"""
vector.py

Functions for applying movement vectors to coordinates.

This file handles coordinate math only.

It does not determine whether a square exists.
That is handled by Board.
"""

from engine.coordinate import Coordinate



# -----------------------------------------
# File movement
# -----------------------------------------

FILE_ORDER = (
    "Y",
    "Z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
)



def shift_file(
    file,
    amount,
):
    """
    Shift a file left or right.

    Does not check whether the
    resulting file is playable.
    """

    index = FILE_ORDER.index(file)

    new_index = index + amount


    if new_index < 0:

        return "X"


    if new_index >= len(FILE_ORDER):

        return "G"


    return FILE_ORDER[new_index]



# -----------------------------------------
# Apply vector
# -----------------------------------------

def apply_vector(
    coordinate,
    vector,
):
    """
    Apply a vector to a coordinate.

    The resulting coordinate may not
    exist on the real board.

    The board validates that later.
    """


    new_file = shift_file(
        coordinate.file,
        vector.file_change,
    )


    new_rank = (
        coordinate.rank
        +
        vector.rank_change
    )


    return Coordinate(
        coordinate.board,
        new_file,
        new_rank,
    )