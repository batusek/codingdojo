from unittest import TestCase

from clean_code.scrabble import Scrabble


class TestScrabble(TestCase):
    def test_a_counts_as_one(self):
        self.assertEqual(Scrabble().score("a"),1)
