"""
File contains tests for Classic Version of this game.
"""
import unittest
from collections import Counter

from versions import ClassicVersion
from shapes import Shapes


class TestClassic(unittest.TestCase):
    """
    Class contains tests for classic version of this game.
    """
    def test_get_shapes(self):
        ver = ClassicVersion()
        func = ver.get_shapes
        data = [Shapes.SCISSORS, Shapes.PAPER, Shapes.ROCK]

        self.assertEqual(Counter(func()), Counter(data))

    def test_interactions(self):
        ver = ClassicVersion()
        func = ver.get_interaction

        self.assertEqual(func(Shapes.SCISSORS, Shapes.PAPER), "cuts")
        self.assertEqual(func(Shapes.PAPER, Shapes.ROCK), "covers")
        self.assertEqual(func(Shapes.ROCK, Shapes.SCISSORS), "crushes")

    def test_results(self):
        ver = ClassicVersion()
        func = ver.get_result

        self.assertTupleEqual(
            func(Shapes.PAPER, Shapes.ROCK),
            (Shapes.PAPER, Shapes.ROCK)
        )

        self.assertEqual(
            func(Shapes.SCISSORS, Shapes.ROCK),
            (Shapes.ROCK, Shapes.SCISSORS)
        )

        self.assertNotEqual(
            func(Shapes.SCISSORS, Shapes.ROCK),
            (Shapes.SCISSORS, Shapes.ROCK)
        )
