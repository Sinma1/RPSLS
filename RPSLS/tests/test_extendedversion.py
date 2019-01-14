"""
File contains tests for Extended Version of this game.
"""
import unittest
from collections import Counter

from versions import ExtendedVersion
from shapes import Shapes


class TestClassic(unittest.TestCase):
    """
    Class contains tests for extended version of this game.
    """
    def test_get_shapes(self):
        ver = ExtendedVersion()
        func = ver.get_shapes
        data = [Shapes.SCISSORS, Shapes.PAPER, Shapes.ROCK, Shapes.SPOCK, Shapes.LIZARD]

        self.assertEqual(Counter(func()), Counter(data))

    def test_interactions(self):
        ver = ExtendedVersion()
        func = ver.get_interaction

        self.assertEqual(func(Shapes.SPOCK, Shapes.ROCK), "vaporizes")
        self.assertEqual(func(Shapes.SPOCK, Shapes.SCISSORS), "smashes")
        self.assertEqual(func(Shapes.LIZARD, Shapes.PAPER), "eats")

    def test_results(self):
        ver = ExtendedVersion()
        func = ver.get_result

        self.assertTupleEqual(
            func(Shapes.LIZARD, Shapes.SPOCK),
            (Shapes.LIZARD, Shapes.SPOCK)
        )

        self.assertEqual(
            func(Shapes.PAPER, Shapes.SPOCK),
            (Shapes.PAPER, Shapes.SPOCK)
        )

        self.assertNotEqual(
            func(Shapes.PAPER, Shapes.SPOCK),
            (Shapes.SPOCK, Shapes.PAPER)
        )
