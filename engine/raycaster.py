"""
raycaster.py

Controls ray generation for Tri-D Chess.

A raycaster:
- creates rays
- advances rays
- clones rays across overlapping platforms
- tracks visited board history
- passes through void spaces

It does not know:
- pieces
- captures
- turns
- check
"""

from __future__ import annotations

from dataclasses import dataclass

from engine.ray import Ray
from engine.coordinate import Coordinate
from engine.vector import apply_vector
from engine.space import (
    get_boards_at,
    is_traversable_space,
)



@dataclass
class RayResult:

    """
    Stores one reachable square.
    """

    coordinate: Coordinate



class Raycaster:


    def __init__(
        self,
        board,
    ):

        self.board = board



    def cast(
        self,
        starts,
        direction,
    ):

        active = []


        for start in starts:

            active.append(
                Ray(
                    start,
                    direction,
                )
            )


        results = []

        seen_results = set()

        seen_states = set()



        while active:

            next_generation = []


            for ray in active:


                #
                # Find next real physical location.
                #
                # Void squares are skipped.
                #

                current = ray.position


                while True:


                    moved = apply_vector(
                        Coordinate(
                            "WL",
                            current.file,
                            current.rank,
                        ),
                        direction,
                    )


                    next_file = moved.file
                    next_rank = moved.rank



                    boards = get_boards_at(
                        next_file,
                        next_rank,
                    )


                    #
                    # Found a real square.
                    #

                    if boards:

                        break



                    #
                    # Void square:
                    # continue searching.
                    #

                    if is_traversable_space(
                        next_file,
                        next_rank,
                    ):

                        current = Coordinate(
                            current.board,
                            next_file,
                            next_rank,
                        )

                        continue



                    #
                    # Completely outside board.
                    #

                    boards = []
                    break



                if not boards:

                    continue



                #
                # Create child rays for every
                # board at this location.
                #

                for board_name in boards:


                    destination = Coordinate(
                        board_name,
                        next_file,
                        next_rank,
                    )



                    #
                    # Cannot return to a board
                    # already left.
                    #

                    if (
                        destination.board
                        in ray.visited_boards
                    ):

                        continue



                    child = Ray(
                        destination,
                        direction,
                    )


                    child.visited_boards = (
                        ray.visited_boards.copy()
                    )



                    #
                    # Leaving a board adds it
                    # to history.
                    #

                    if (
                        destination.board
                        != ray.position.board
                    ):

                        child.visited_boards.add(
                            ray.position.board
                        )



                    #
                    # Record move.
                    #

                    if destination not in seen_results:

                        results.append(
                            RayResult(destination)
                        )

                        seen_results.add(destination)



                    #
                    # Prevent duplicate states.
                    #

                    state = (
                        destination,
                        frozenset(
                            child.visited_boards
                        ),
                    )


                    if state in seen_states:

                        continue


                    seen_states.add(state)


                    next_generation.append(child)



            active = next_generation



        return results