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

    def test_pair_scores_as_sum_of_two_highest_matching_dice(self):
        self.assertEquals(12,Yahtsee().score(Category.PAIR,[2,3,6,6,6]))

    def test_pair_scores_zero_if_no_two_dice_match(self):
        self.assertEquals(0,Yahtsee().score(Category.PAIR,[2,3,4,5,6]))

    def test_two_pairs_score_zero_if_there_are_less_than_two_pairs(self):
        self.assertEquals(0,Yahtsee().score(Category.TWOPAIRS,[2,2,4,5,6]))

    def test_two_pairs_score_sum_of_two_pairs_dice(self):
        self.assertEquals(14,Yahtsee().score(Category.TWOPAIRS,[2,2,4,5,5]))

    def test_three_of_a_kind_scores_zero_if_three_matching_dice_not_present(self):
        self.assertEquals(0,Yahtsee().score(Category.THREEOFAKIND,[2,3,3,5,6]))

    def test_three_of_a_kind_scores_sum_of_three_matching_dice(self):
        self.assertEquals(9,Yahtsee().score(Category.THREEOFAKIND,[2,3,3,3,6]))


if __name__ == '__main__':
    unittest.main()
