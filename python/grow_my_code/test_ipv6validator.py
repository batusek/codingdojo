import unittest
from grow_my_code.ipv6validator import *

#Based on https://www.codewars.com/kata/54fa4e210609868fce0002bf
class IPv6ValidatorTest(unittest.TestCase):
    def test_happy_path_eight_groups_filled_with_non_zero_octets(self):
        input = "123f:123f:123f:123f:123f:123f:123f:123f"
        self.assertEquals(IPv6Validator().contract(input),input)

