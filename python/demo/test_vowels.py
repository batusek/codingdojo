from unittest import TestCase

from python.demo.vowels import VowelCounter


# See https://www.codewars.com/kata/54ff3102c1bad923760001f3
class VowelCounterTest(TestCase):
    def test_empty_string_has_no_vowels(self):
        self.assertEqual(VowelCounter().count_vowels(""),0)

    def test_string_with_consonants_has_no_vowels(self):
        self.assertEqual(VowelCounter().count_vowels("psst"),0)

    def test_string_with_a_has_one_vowel(self):
        self.assertEqual(VowelCounter().count_vowels("cat"),1)

    def test_string_with_two_a_has_two_vowels(self):
        self.assertEqual(VowelCounter().count_vowels("madam"),2)

    def test_string_with_a_and_e_has_two_vowels(self):
        self.assertEqual(VowelCounter().count_vowels("eat"),2)

    def test_string_with_all_vowels_has_five_vowels(self):
        self.assertEqual(VowelCounter().count_vowels("education"),5)

    def test_y_doesnt_count_as_vowel(self):
        self.assertEqual(VowelCounter().count_vowels("year"),2)

    def test_capital_letters_count_as_vowels(self):
        self.assertEqual(VowelCounter().count_vowels("Air"),2)

    def test_cat_has_three_letters(self):
        self.assertEqual(VowelCounter().count_letters("cat"),3)
