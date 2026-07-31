"""
ray.py

Ray traversal for Tri-D Chess movement.

A ray represents one sliding movement path.

This file does not know about:
- pieces
- captures
- friendly/enemy rules
- legal moves

It only tracks movement through space.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from engine.coordinate import Coordinate
from engine.vector import apply_vector



@dataclass
class Ray:

    """
    Represents a moving ray.

    Example:

        Start:
            WL:A1

        Direction:
            UP

        Path:
            WL:A2
            WL:A3
            NL:A3
            ...

    visited_boards stores boards that the ray
    has already LEFT.

    The current board is not included until
    the ray transitions away from it.
    """

    position: Coordinate

    direction: object


    visited_boards: set[str] = field(
        default_factory=set
    )


    path: list[Coordinate] = field(
        default_factory=list
    )


    active: bool = True



    def advance(self):
        """
        Move the ray one step.

        Returns:
            Coordinate if movement succeeds

        Returns:
            None if the ray terminates
        """

        if not self.active:

            return None



        new_position = apply_vector(
            self.position,
            self.direction,
        )



        #
        # If entering a different board,
        # check whether that board was
        # already left earlier.
        #

        if (
            new_position.board
            != self.position.board
            and
            new_position.board
            in self.visited_boards
        ):

            self.active = False

            return None



        #
        # If leaving the current board,
        # record the board we are leaving.
        #

        if (
            new_position.board
            != self.position.board
        ):

            self.visited_boards.add(
                self.position.board
            )



        #
        # Store movement
        #

        self.path.append(
            new_position
        )


        #
        # Update position
        #

        self.position = new_position


        return new_position



    def stop(self):
        """
        Stop the ray.
        """

        self.active = False