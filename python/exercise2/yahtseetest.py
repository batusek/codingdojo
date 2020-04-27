import unittest
from yahtsee import Yahtsee, Category


class NumberTest(unittest.TestCase):
    def test_if_no_number_exists_score_is_zero(self):
        self.assertEquals(0,Yahtsee().score(Category.ONES,[2,3,2,4,5]))

    def test_score_to_ones_is_euqal_to_sum_of_dice_that_read_one(self):
        self.assertEquals(2,Yahtsee().score(Category.ONES,[1,3,1,4,5]))


if __name__ == '__main__':
    unittest.main()
