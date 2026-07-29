"""
constants.py

Global constants for the Star Trek Tri-D Chess engine.
"""

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
FPS = 60

TITLE = "Star Trek Tri-D Chess"

BACKGROUND = (25, 25, 30)

WHITE = (245, 245, 245)
BLACK = (35, 35, 35)

BOARD_GREEN = (92, 143, 82)
BOARD_RED = (145, 72, 72)
BOARD_NEUTRAL = (120, 120, 120)

LIGHT_SQUARE = (222, 213, 189)
DARK_SQUARE = (102, 83, 63)

FILES = ["Z", "A", "B", "C", "D", "E"]

RANKS = list(range(10))

MAIN_BOARDS = [
    "WL",
    "NL",
    "BL",
]

ATTACK_BOARDS = [
    "WKL",
    "WQL",
    "BKL",
    "BQL",
]

ALL_BOARDS = MAIN_BOARDS + ATTACK_BOARDS