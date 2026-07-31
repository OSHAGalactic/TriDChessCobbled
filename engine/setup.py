"""
setup.py

Creates the starting position for Star Trek Tri-D Chess.

This file places pieces onto a Board.
It does not contain movement logic.
"""

from engine.coordinate import Coordinate
from engine.piece import Piece, PieceType, Color



def place_piece(
    board,
    piece_type,
    color,
    board_name,
    file,
    rank,
):
    """
    Place a piece at a coordinate.
    """

    coordinate = Coordinate(
        board_name,
        file,
        rank,
    )


    if board.get_piece(coordinate) is not None:

        raise ValueError(
            f"Square already occupied: {coordinate}"
        )


    board.set_piece(
        coordinate,
        Piece(
            piece_type,
            color,
            coordinate,
        ),
    )



def setup_starting_position(board):

    """
    Creates the official Tri-D Chess starting setup.
    """

    # =================================================
    # WHITE
    # =================================================

    # -------------------------
    # White pawns (main board)
    # -------------------------

    for file in (
        "A",
        "B",
        "C",
        "D",
    ):

        place_piece(
            board,
            PieceType.PAWN,
            Color.WHITE,
            "WL",
            file,
            2,
        )


    # -------------------------
    # White minor pieces
    # -------------------------

    place_piece(
        board,
        PieceType.KNIGHT,
        Color.WHITE,
        "WL",
        "A",
        1,
    )

    place_piece(
        board,
        PieceType.KNIGHT,
        Color.WHITE,
        "WL",
        "D",
        1,
    )


    place_piece(
        board,
        PieceType.BISHOP,
        Color.WHITE,
        "WL",
        "B",
        1,
    )

    place_piece(
        board,
        PieceType.BISHOP,
        Color.WHITE,
        "WL",
        "C",
        1,
    )


    # -------------------------
    # White attack platform pieces
    # -------------------------

    # King

    place_piece(
        board,
        PieceType.KING,
        Color.WHITE,
        "WKL",
        "A",
        0,
    )


    # Queen

    place_piece(
        board,
        PieceType.QUEEN,
        Color.WHITE,
        "WQL",
        "D",
        0,
    )


    # Rooks

    place_piece(
        board,
        PieceType.ROOK,
        Color.WHITE,
        "WKL",
        "Z",
        0,
    )

    place_piece(
        board,
        PieceType.ROOK,
        Color.WHITE,
        "WQL",
        "E",
        0,
    )


    # Attack platform pawns

    for board_name, file, rank in (
        ("WKL", "Z", 1),
        ("WKL", "A", 1),
        ("WQL", "D", 1),
        ("WQL", "E", 1),
    ):

        place_piece(
            board,
            PieceType.PAWN,
            Color.WHITE,
            board_name,
            file,
            rank,
        )



    # =================================================
    # BLACK
    # =================================================

    # -------------------------
    # Black pawns (main board)
    # -------------------------

    for file in (
        "A",
        "B",
        "C",
        "D",
    ):

        place_piece(
            board,
            PieceType.PAWN,
            Color.BLACK,
            "BL",
            file,
            7,
        )


    # -------------------------
    # Black minor pieces
    # -------------------------

    place_piece(
        board,
        PieceType.KNIGHT,
        Color.BLACK,
        "BL",
        "A",
        8,
    )

    place_piece(
        board,
        PieceType.KNIGHT,
        Color.BLACK,
        "BL",
        "D",
        8,
    )


    place_piece(
        board,
        PieceType.BISHOP,
        Color.BLACK,
        "BL",
        "B",
        8,
    )

    place_piece(
        board,
        PieceType.BISHOP,
        Color.BLACK,
        "BL",
        "C",
        8,
    )


    # -------------------------
    # Black attack platform pieces
    # -------------------------

    # King

    place_piece(
        board,
        PieceType.KING,
        Color.BLACK,
        "BKL",
        "A",
        9,
    )


    # Queen

    place_piece(
        board,
        PieceType.QUEEN,
        Color.BLACK,
        "BQL",
        "D",
        9,
    )


    # Rooks

    place_piece(
        board,
        PieceType.ROOK,
        Color.BLACK,
        "BKL",
        "Z",
        9,
    )

    place_piece(
        board,
        PieceType.ROOK,
        Color.BLACK,
        "BQL",
        "E",
        9,
    )


    # Attack platform pawns

    for board_name, file, rank in (
        ("BKL", "Z", 8),
        ("BKL", "A", 8),
        ("BQL", "D", 8),
        ("BQL", "E", 8),
    ):

        place_piece(
            board,
            PieceType.PAWN,
            Color.BLACK,
            board_name,
            file,
            rank,
        )


    return board