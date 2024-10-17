import unittest
from demo.commas import NumberFormatter

# See https://www.codewars.com/kata/5274e122fc75c0943d000148
class NumberFormatterTest(unittest.TestCase):
    def test_one_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(1),"1")

    def test_ten_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(10),"10")

    def test_hundred_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(100),"100")

    def test_thousand_prints_with_comma(self):
        self.assertEqual(NumberFormatter().format(1000),"1,000")

    def test_million_prints_with_two_commas(self):
        self.assertEqual(NumberFormatter().format(1000000),"1,000,000")

    def test_a_high_number_needs_many_commas(self):
        self.assertEqual(NumberFormatter().format(35235235),"35,235,235")
