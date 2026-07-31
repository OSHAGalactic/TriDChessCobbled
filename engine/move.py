"""
move.py

Represents a chess move.

A Move stores:
- where a piece starts
- where it ends
- what piece moved
- what piece was captured

It does not:
- execute moves
- validate legality
- handle turns
"""


class Move:


    def __init__(
        self,
        start,
        end,
        piece=None,
        captured=None,
    ):

        self.start = start
        self.end = end

        self.piece = piece
        self.captured = captured



    @property
    def is_capture(self):
        """
        Returns True if this move captures
        another piece.
        """

        return self.captured is not None



    def __repr__(self):

        if self.is_capture:

            return (
                f"{self.start} -> {self.end} "
                f"(captures {self.captured})"
            )


        return (
            f"{self.start} -> {self.end}"
        )