"""
File containing Shapes which inherit from Enum
"""
from enum import Enum


class Shapes(Enum):
    """
    Class Shapes which inherits from Enum.
    This class contains possible shapes in game and their
    respective user-friendly name
    """
    ROCK = "Rock"
    SCISSORS = "Scissors"
    PAPER = "Paper"
    LIZARD = "Lizard"
    SPOCK = "Spock"
