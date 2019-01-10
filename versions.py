import random

from shapes import Shapes


class BaseVersion:
    def __init__(self):
        self.interactions = {}
        self.matchups = {}
        self.shortcuts = {}

    def get_shapes(self):
        return list(self.matchups.keys())

    def get_interaction(self, winner, loser):
        if (winner, loser) in self.interactions:
            return self.interactions[(winner, loser)]

    def get_result(self, first, second):
        if first == second:
            return None, None
        if first not in self.matchups or second not in self.matchups:
            raise ValueError

        if self.matchups[first] == second:
            return first, second
        return second, first

    def get_random_shape(self):
        return random.choice(self.get_shapes())


class ClassicVersion(BaseVersion):
    def __init__(self):
        super().__init__()
        interactions = {
            (Shapes.SCISSORS, Shapes.PAPER): "cuts",
            (Shapes.PAPER, Shapes.ROCK): "covers",
            (Shapes.ROCK, Shapes.SCISSORS): "crushes"
        }
        self.interactions.update(interactions)

        matchups = {
            Shapes.SCISSORS: Shapes.PAPER,
            Shapes.ROCK: Shapes.SCISSORS,
            Shapes.PAPER: Shapes.ROCK,
        }
        self.matchups.update(matchups)

        shortcuts = {
            's': Shapes.SCISSORS,
            'p': Shapes.PAPER,
            'r': Shapes.ROCK
        }
        self.shortcuts.update(shortcuts)
