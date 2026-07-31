"""
space.py

Provides information about Tri-D Chess platform locations.

This file answers:

"Which boards have a playable square at this file/rank?"

It also identifies:
- void spaces that rays may pass through
- but pieces may not land on

It does not handle:
- pieces
- movement
- captures
- legality
"""


from engine.board import BOARD_COORDINATES



def get_boards_at(
    file,
    rank,
):
    """
    Returns a list of boards containing
    a playable square at the given file/rank.

    Example:

        get_boards_at("A", 3)

    returns:

        ["WL", "NL"]

    """

    boards = []


    for board_name, (files, ranks) in BOARD_COORDINATES.items():

        if (
            file in files
            and
            rank in ranks
        ):

            boards.append(
                board_name
            )


    return boards



def is_void_space(
    file,
    rank,
):
    """
    Returns True if this coordinate is a
    pass-through void square.

    Void squares:
    - exist in coordinate space
    - cannot be landed on
    - can be crossed by sliding pieces

    Current void squares:
        B0
        C0
        B9
        C9
    """

    file = file.upper()

    return (
        rank in (0, 9)
        and file in ("B", "C")
    )
def is_traversable_space(
    file,
    rank,
):
    """
    Returns True if a ray may continue through
    this physical coordinate.

    This includes:
    - playable squares
    - vertical gaps between platforms
    - void-hop squares

    It does not mean a piece may land here.
    """

    #
    # Coordinates inside the overall Tri-D space
    #

    if file.upper() not in (
        "Z",
        "A",
        "B",
        "C",
        "D",
        "E",
    ):
        return False


    if rank < 0 or rank > 9:
        return False


    return True