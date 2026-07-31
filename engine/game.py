"""
game.py

Controls a running game of Tri-D Chess.

Connects:
- Board
- Legal move generation
- Turns
- Moves
- Check detection
- Game status
"""


from engine.turn import TurnManager
from engine.legalmoves import legal_moves

from engine.status import (
    game_over,
    is_checkmate,
    is_stalemate,
)

from engine.check import is_in_check



class Game:


    def __init__(
        self,
        board,
    ):

        self.board = board

        self.turns = TurnManager()

        self.move_history = []

        self.finished = False

        self.result = None



    # -------------------------------------------------

    def attempt_move(
        self,
        move,
    ):
        """
        Attempt to perform a move.

        Returns:
            True if successful
            False otherwise
        """


        #
        # Game already ended
        #

        if self.finished:

            return False



        piece = self.board.get_piece(
            move.start
        )


        #
        # No piece
        #

        if piece is None:

            return False



        #
        # Wrong player's turn
        #

        if piece.color != self.turns.get_turn():

            return False



        #
        # Get legal moves
        #

        possible_moves = legal_moves(
            self.board,
            piece,
        )


        legal_move = None


        for possible in possible_moves:

            if possible.end == move.end:

                legal_move = possible
                break



        #
        # Illegal destination
        #

        if legal_move is None:

            return False



        #
        # Execute validated move
        #

        self.board.make_move(
            legal_move
        )



        #
        # Store history
        #

        self.move_history.append(
            legal_move
        )



        #
        # Change player
        #

        self.turns.next_turn()



        #
        # Update game state
        #

        self.update_status()



        return True



    # -------------------------------------------------

    def update_status(
        self,
    ):
        """
        Update whether the game has ended.

        Safe for incomplete test boards.
        """


        current_player = (
            self.turns.get_turn()
        )


        #
        # Allow development boards
        # without kings.
        #

        if self.board.find_king(
            current_player
        ) is None:

            return



        if game_over(
            self.board,
            current_player,
        ):

            self.finished = True


            if is_checkmate(
                self.board,
                current_player,
            ):

                self.result = "checkmate"



            elif is_stalemate(
                self.board,
                current_player,
            ):

                self.result = "stalemate"



    # -------------------------------------------------

    def status(
        self,
    ):
        """
        Return current game status.

        Possible values:
        - playing
        - check
        - checkmate
        - stalemate
        """


        if self.finished:

            return self.result



        current_player = (
            self.turns.get_turn()
        )


        #
        # Development boards may not
        # contain kings yet.
        #

        if self.board.find_king(
            current_player
        ) is None:

            return "playing"



        if is_in_check(
            self.board,
            current_player,
        ):

            return "check"



        return "playing"