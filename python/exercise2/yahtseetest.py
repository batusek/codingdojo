import unittest
from yahtsee import Yahtsee, Category


class NumberTest(unittest.TestCase):
    def test_if_no_number_exists_score_is_zero(self):
        self.assertEquals(0,Yahtsee().score(Category.ONES,[2,3,2,4,5]))

    def test_score_to_ones_is_equal_to_sum_of_dice_that_read_one(self):
        self.assertEquals(2,Yahtsee().score(Category.ONES,[1,3,1,4,5]))

    def test_score_to_twos_is_equal_to_sum_of_dice_that_read_two(self):
        self.assertEquals(4,Yahtsee().score(Category.TWOS,[2,3,2,4,5]))

    def test_score_to_sixes_is_equal_to_sum_of_dice_that_read_six(self):
        self.assertEquals(18,Yahtsee().score(Category.SIXES,[2,3,6,6,6]))


if __name__ == '__main__':
    unittest.main()
