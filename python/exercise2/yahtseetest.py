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

    def test_four_of_a_kind_scores_zero_if_four_matching_dice_not_present(self):
        self.assertEquals(0,Yahtsee().score(Category.FOUROFAKIND,[2,3,3,5,3]))

    def test_four_of_a_kind_scores_sum_of_four_matching_dice(self):
        self.assertEquals(12,Yahtsee().score(Category.FOUROFAKIND,[2,3,3,3,3]))

    def test_yahtsee_scores_zero_if_five_matching_dice_not_present(self):
        self.assertEquals(0,Yahtsee().score(Category.YAHTSEE,[2,3,3,3,3]))

    def test_yahtsee_scores_50_if_five_matching_dice_present(self):
        self.assertEquals(50,Yahtsee().score(Category.YAHTSEE,[3,3,3,3,3]))

    def test_small_straight_scores_30_if_four_consecutive_dice_present(self):
        self.assertEquals(30,Yahtsee().score(Category.SMALL,[1,2,3,4,6]))

    def test_small_straight_scores_0_if_four_consecutive_dice_not_present(self):
        self.assertEquals(30,Yahtsee().score(Category.SMALL,[1,2,3,5,6]))

    def test_large_straight_scores_40_if_five_consecutive_dice_present(self):
        self.assertEquals(40,Yahtsee().score(Category.LARGE,[1,2,3,4,5]))

    def test_chance_sums_all_dice(self):
        self.assertEquals(16,Yahtsee().score(Category.CHANCE,[1,2,2,5,6]))

if __name__ == '__main__':
    unittest.main()
