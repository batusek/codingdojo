from unittest import TestCase

from clean_code.scrabble import Scrabble


class TestScrabble(TestCase):
    def test_a_counts_as_one(self):
        self.assertEqual(Scrabble().score("a"),1)

    def test_f_counts_as_four(self):
        self.assertEqual(Scrabble().score("f"),4)

    def test_at_counts_as_two(self):
        self.assertEqual(Scrabble().score("at"),2)

    def test_street_counts_as_six(self):
        self.assertEqual(Scrabble().score("street"), 6)

    def test_quirky_counts_as_22(self):
        self.assertEqual(Scrabble().score("quirky"), 22)

    def test_empty_string_counts_as_zero(self):
        self.assertEqual(Scrabble().score(""), 0)

    def test_double_letter_bonus(self):
        self.assertEqual(Scrabble().score("a*"), 2)

    def test_triple_letter_bonus(self):
        self.assertEqual(Scrabble().score("a**"), 3)

    def test_long_word_with_bonuses(self):
        self.assertEqual(Scrabble().score("he*l**lo"), 11)

    def test_double_word_bonus(self):
        self.assertEqual(Scrabble().score("hippo(d)"), 24)
