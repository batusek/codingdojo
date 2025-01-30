from unittest import TestCase

from python.clean_code.scrabble import Scrabble


class TestScrabble(TestCase):
    def test_a_counts_as_one(self):
        self.assertEqual(Scrabble().score("a"),1)

    def test_b_counts_as_three(self):
        self.assertEqual(Scrabble().score("b"),3)

    def test_z_counts_as_ten(self):
        self.assertEqual(Scrabble().score("z"),10)

    def test_letter_values_are_summed_for_the_word(self):
        self.assertEqual(Scrabble().score("cat"),5)

    def test_letter_before_asterisk_is_doubled(self):
        self.assertEqual(Scrabble().score("z*ebra"),26)

    def test_letter_before_two_asterisks_is_tripled(self):
        self.assertEqual(Scrabble().score("z**ebra"),36)

    def test_d_in_brackets_means_double_word(self):
        self.assertEqual(Scrabble().score("hippo(d)"),24)

    def test_t_in_brackets_means_triple_word(self):
        self.assertEqual(Scrabble().score("hippo(t)"),36)