import unittest
from tooling.leapyear import isLeapYear

# Kata instructions: http://codingdojo.org/kata/LeapYears/

class LeapYearTest(unittest.TestCase):
    def test_normal_year_is_not_leap_year(self):
        self.assertFalse(isLeapYear(1789))

    