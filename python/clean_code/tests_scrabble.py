from unittest import TestCase

from clean_code.scrabble import Scrabble


class TestScrabble(TestCase):
    def test_a_counts_as_one(self):
        self.assertEqual(Scrabble().score("a"),1)

    def test_ab_counts_as_four(self):
        self.assertEqual(Scrabble().score("ab"),4)

    def test_hello_with_double_letter_counts_as_9(self):
        self.assertEqual(Scrabble().score("he*llo"), 9)

    def test_hello_with_triple_letter_counts_as_10(self):
        self.assertEqual(Scrabble().score("he**llo"), 10)

    def test_double_word_score(self):
        self.assertEqual(Scrabble().score("hello(d)"), 16)

    def test_triple_word_score(self):
        self.assertEqual(Scrabble().score("hello(t)"), 24)

    def test_blank_tile_scores_zero(self):
        self.assertEqual(Scrabble().score("he^llo"), 7)

    def test_seven_letter_word_bonus(self):
        self.assertEqual(Scrabble().score("amazing"), 19 + 50)
