import unittest
from demo.commas import NumberFormatter

class NumberFormatterTest(unittest.TestCase):
    def test_blah(self):
        self.assertEqual(NumberFormatter().format(1),"1")
