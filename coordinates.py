"""
coordinates.py

Coordinate objects used throughout the engine.
"""

from dataclasses import dataclass

from constants import ALL_BOARDS


@dataclass(frozen=True)
class Coordinate:
    board: str
    file: str
    rank: int

    def __post_init__(self):

        if self.board not in ALL_BOARDS:
            raise ValueError(f"Unknown board '{self.board}'")

        if len(self.file) != 1:
            raise ValueError("File must be one letter")

        object.__setattr__(self, "file", self.file.upper())

    def __str__(self):
        return f"{self.board} {self.file}{self.rank}"

    def overlaps(self):
        """
        Returns all coordinates sharing this vertical column.
        Attack boards only overlap themselves.
        """

        if self.board in ("WL", "NL", "BL"):

            return [
                Coordinate("WL", self.file, self.rank),
                Coordinate("NL", self.file, self.rank),
                Coordinate("BL", self.file, self.rank),
            ]

        return [self]