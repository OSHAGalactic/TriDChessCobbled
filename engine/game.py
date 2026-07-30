"""
game.py

Controls a running game of Tri-D Chess.

Connects:
- Board
- Movement rules
- Turns
- Moves
"""

from engine.turn import TurnManager
from engine.movement import can_move
from engine.piece import Color


class Game:


    def __init__(self, board):

        self.board = board

        self.turns = TurnManager()



    def attempt_move(
        self,
        move,
    ):

        """
        Attempt to perform a move.

        Returns True if successful.
        """

        
        piece = self.board.get_piece(
            move.start
        )


        # No piece there

        if piece is None:
            return False



        # Wrong player's turn

        if piece.color != self.turns.get_turn():

            return False



        # Check movement rules

        if not can_move(
            self.board,
            piece,
            move.end,
        ):

            return False



            # Check if destination has friendly piece

        target = self.board.get_piece(
            move.end
        )

        if target is not None:

            if target.color == piece.color:
                return False


        # Perform move

        self.board.move_piece(
            move.start,
            move.end,
        )


        # Switch player

        self.turns.next_turn()


        return True