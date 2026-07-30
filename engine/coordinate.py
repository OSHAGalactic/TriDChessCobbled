"""
coordinate.py

Immutable coordinate objects for Star Trek Tri-D Chess.

Coordinates consist of:

    Board
    File
    Rank

Example:

    Coordinate("WL", "C", 3)

Coordinates are hashable so they can be dictionary keys.
"""

from __future__ import annotations

from dataclasses import dataclass


# ----------------------------
# Board identifiers
# ----------------------------

MAIN_BOARDS = ("WL", "NL", "BL")

ATTACK_BOARDS = (
    "WKL",
    "WQL",
    "BKL",
    "BQL",
)

ALL_BOARDS = MAIN_BOARDS + ATTACK_BOARDS


# ----------------------------
# Files / ranks
# ----------------------------

FILES = ("Z", "A", "B", "C", "D", "E")
RANKS = tuple(range(10))


@dataclass(frozen=True, slots=True)
class Coordinate:
    """
    Immutable board coordinate.
    """

    board: str
    file: str
    rank: int

    def __post_init__(self):

        board = self.board.upper()
        file = self.file.upper()

        object.__setattr__(self, "board", board)
        object.__setattr__(self, "file", file)

        if board not in ALL_BOARDS:
            raise ValueError(f"Unknown board '{board}'")

        if file not in FILES:
            raise ValueError(f"Illegal file '{file}'")

        if self.rank not in RANKS:
            raise ValueError(f"Illegal rank '{self.rank}'")

    # --------------------------------

    def __str__(self):

        return f"{self.board}:{self.file}{self.rank}"

    def __repr__(self):

        return str(self)

    # --------------------------------

    @property
    def is_main_board(self):

        return self.board in MAIN_BOARDS

    @property
    def is_attack_board(self):

        return self.board in ATTACK_BOARDS

    # --------------------------------

    def same_column(self, other: "Coordinate") -> bool:
        """
        Returns True if two coordinates share
        the same file/rank regardless of level.
        """

        return (
            self.file == other.file
            and self.rank == other.rank
        )

    # --------------------------------

    def overlaps(self) -> tuple["Coordinate", ...]:
        """
        Returns every square occupying the same
        physical column.

        Example:

            WL:C4

        returns

            WL:C4
            NL:C4
            BL:C4

        Attack-board overlap will eventually be
        handled by the Board class because it
        depends on platform position.
        """

        if not self.is_main_board:
            return (self,)

        return (
            Coordinate("WL", self.file, self.rank),
            Coordinate("NL", self.file, self.rank),
            Coordinate("BL", self.file, self.rank),
        )

    # --------------------------------

    def with_board(self, board: str):

        return Coordinate(board, self.file, self.rank)

    def with_file(self, file: str):

        return Coordinate(self.board, file, self.rank)

    def with_rank(self, rank: int):

        return Coordinate(self.board, self.file, rank)