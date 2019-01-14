"""
File cointains logic of the game with base class
and classes that inherit from that base with expanded functionality.
"""
import random

from shapes import Shapes


class BaseVersion:
    """
    Base class which only contains function for performing game actions.
    Derived class should extend this class with interactions, matchups and shortcuts.
    """
    def __init__(self):
        self.interactions = {}
        self.matchups = {}
        self.shortcuts = {}

    def get_shapes(self):
        return list(self.matchups.keys())

    def get_interaction(self, winner, loser):
        if (winner, loser) in self.interactions:
            return self.interactions[(winner, loser)]
        raise ValueError

    def get_result(self, first, second):
        if first == second:
            return None, None
        if first not in self.matchups or second not in self.matchups:
            raise ValueError

        if second in self.matchups[first]:
            return first, second
        return second, first

    def get_random_shape(self):
        return random.choice(self.get_shapes())


class ClassicVersion(BaseVersion):
    """
    Class that inherit from BaseVersion and implements
    login and shapes from classic version of this game.
    """
    def __init__(self):
        super().__init__()
        interactions = {
            (Shapes.SCISSORS, Shapes.PAPER): "cuts",
            (Shapes.PAPER, Shapes.ROCK): "covers",
            (Shapes.ROCK, Shapes.SCISSORS): "crushes"
        }
        self.interactions = interactions

        matchups = {
            Shapes.SCISSORS: [Shapes.PAPER],
            Shapes.ROCK: [Shapes.SCISSORS],
            Shapes.PAPER: [Shapes.ROCK],
        }
        self.matchups = matchups

        shortcuts = {
            's': Shapes.SCISSORS,
            'p': Shapes.PAPER,
            'r': Shapes.ROCK
        }
        self.shortcuts = shortcuts


class ExtendedVersion(ClassicVersion):
    """
    Class that extend ClassicVersion with more interactions,
    matchups, shortcuts and shapes.
    """
    def __init__(self):
        super().__init__()
        interactions = {
            (Shapes.ROCK, Shapes.LIZARD): "crushes",
            (Shapes.LIZARD, Shapes.SPOCK): "poisons",
            (Shapes.SPOCK, Shapes.SCISSORS): "smashes",
            (Shapes.SCISSORS, Shapes.LIZARD): "decapitates",
            (Shapes.LIZARD, Shapes.PAPER): "eats",
            (Shapes.PAPER, Shapes.SPOCK): "disproves",
            (Shapes.SPOCK, Shapes.ROCK): "vaporizes",
        }
        self.interactions.update(interactions)

        matchups = {
            Shapes.SCISSORS: [Shapes.LIZARD, Shapes.PAPER],
            Shapes.PAPER: [Shapes.SPOCK, Shapes.ROCK],
            Shapes.ROCK: [Shapes.LIZARD, Shapes.SCISSORS],
            Shapes.LIZARD: [Shapes.SPOCK, Shapes.PAPER],
            Shapes.SPOCK: [Shapes.SCISSORS, Shapes.ROCK]
        }
        self.matchups = matchups

        shortcuts = {
            'sp': Shapes.SPOCK,
            'l': Shapes.LIZARD
        }
        self.shortcuts.update(shortcuts)
