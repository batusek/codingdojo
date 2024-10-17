import unittest
from demo.commas import NumberFormatter

class NumberFormatterTest(unittest.TestCase):
    def test_one_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(1),"1")

    def test_ten_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(10),"10")

    def test_hundred_prints_without_comma(self):
        self.assertEqual(NumberFormatter().format(100),"100")

    def test_thousand_prints_with_comma(self):
        self.assertEqual(NumberFormatter().format(1000),"1,000")
