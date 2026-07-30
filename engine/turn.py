"""
turn.py

Tracks player turns.
"""

from engine.piece import Color


class TurnManager:


    def __init__(self):

        self.current = Color.WHITE



    def get_turn(self):

        return self.current



    def next_turn(self):

        if self.current == Color.WHITE:

            self.current = Color.BLACK

        else:

            self.current = Color.WHITE