"""
piece.py

Defines chess pieces for Tri-D Chess.

This file contains piece data only.
Movement rules will be added later.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from engine.coordinate import Coordinate


class PieceType(Enum):

    KING = "king"
    QUEEN = "queen"
    BISHOP = "bishop"
    KNIGHT = "knight"
    ROOK = "rook"
    PAWN = "pawn"



class Color(Enum):

    WHITE = "white"
    BLACK = "black"



@dataclass
class Piece:

    piece_type: PieceType
    color: Color
    position: Coordinate
    has_moved: bool = False

    def __repr__(self):

        return (
            f"{self.color.value} "
            f"{self.piece_type.value} "
            f"({self.position})"
        )