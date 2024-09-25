import unittest
from tooling.leapyear import isLeapYear


class LeapYearTest(unittest.TestCase):
    def test_normal_year_is_not_leap_year(self):
        self.assertFalse(isLeapYear(1789))

    # After start
    def test_every_4_years_there_is_a_leap_year(self):
        self.assertTrue(isLeapYear(1780))

    def test_every_100_years_there_is_not_a_leap_year(self):
        self.assertFalse(isLeapYear(1700))

    def test_every_400_years_there_is_a_leap_year(self):
        self.assertTrue(isLeapYear(1600))
    # After end
    