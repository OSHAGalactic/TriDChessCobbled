"""
piece_symbols.py

Maps Tri-D Chess pieces to display symbols.

Currently uses text letters for easy debugging.
This can later be replaced with images or 3D models.
"""

from engine.piece import PieceType, Color



SYMBOLS = {

    # White pieces

    (Color.WHITE, PieceType.KING): "K",
    (Color.WHITE, PieceType.QUEEN): "Q",
    (Color.WHITE, PieceType.ROOK): "R",
    (Color.WHITE, PieceType.BISHOP): "B",
    (Color.WHITE, PieceType.KNIGHT): "N",
    (Color.WHITE, PieceType.PAWN): "P",


    # Black pieces

    (Color.BLACK, PieceType.KING): "k",
    (Color.BLACK, PieceType.QUEEN): "q",
    (Color.BLACK, PieceType.ROOK): "r",
    (Color.BLACK, PieceType.BISHOP): "b",
    (Color.BLACK, PieceType.KNIGHT): "n",
    (Color.BLACK, PieceType.PAWN): "p",

}



def get_symbol(piece):

    """
    Return the display symbol for a piece.
    """

    return SYMBOLS[
        (
            piece.color,
            piece.piece_type,
        )
    ]